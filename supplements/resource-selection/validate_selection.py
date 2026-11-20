#!/usr/bin/env python3
"""Validate the internal consistency of the published selection records.

This standard-library-only script reads screening.csv and panel_selection.csv
beside this file. It does not access the network, revalidate source evidence,
reconstruct the discovery search, or establish that the 20-resource panel is
optimal. The expected counts and selected IDs document the accepted panel.

Run: python validate_selection.py
Optional report: python validate_selection.py --json validation_report.json

The default invocation writes no files. Exit status is 0 for consistent records,
1 for validation/read/report errors, and 2 for invalid command-line arguments.
"""

import argparse
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit


SCREENING_COLUMNS = (
    "resource_id", "family_id", "family_name", "resource_name", "source_url",
    "s1_scope", "s2_english", "s3_public_access", "screening_outcome",
    "decision_basis", "first_nonpass",
)
PANEL_COLUMNS = (
    "resource_id", "family_id", "resource_name", "organizational_contrast",
    "relationship_and_boundary", "panel_reason", "panel_status",
)
STAGE_COLUMNS = ("s1_scope", "s2_english", "s3_public_access")
STAGES = ("S1", "S2", "S3")
FAMILY_NAMES = {
    "F1": "Classification systems",
    "F2": "Subject headings and controlled vocabularies",
    "F3": "Ontologies and formal knowledge bases",
    "F4": "Knowledge graphs and entity authorities",
    "F5": "Lexical-semantic resources",
}
FAMILY_FIELDS = (
    "initial", "after_s1", "after_s2", "advance", "selected", "alternative",
    "scope_fail", "english_fail", "english_unverified", "access_fail",
    "access_unverified",
)
EXPECTED_FAMILIES = {
    "F1": (62, 28, 25, 21, 4, 17, 34, 0, 3, 0, 4),
    "F2": (46, 16, 10, 7, 3, 4, 30, 0, 6, 1, 2),
    "F3": (69, 23, 23, 23, 3, 20, 46, 0, 0, 0, 0),
    "F4": (33, 18, 17, 13, 6, 7, 15, 0, 1, 0, 4),
    "F5": (14, 14, 13, 13, 4, 9, 0, 1, 0, 0, 0),
}
EXPECTED_SELECTED = {
    "F1-001": "DDC",
    "F1-002": "LCC",
    "F1-003": "UDC",
    "F1-049": "OpenAlex Topics",
    "F2-001": "FAST",
    "F2-002": "LCSH",
    "F2-045": "YSO",
    "F3-001": "SUMO",
    "F3-009": "CCO",
    "F3-029": "FrameBase",
    "F4-001": "DBpedia",
    "F4-002": "Wikidata",
    "F4-003": "YAGO",
    "F4-006": "ATOMIC",
    "F4-009": "ConceptNet",
    "F4-010": "CSKG",
    "F5-001": "BabelNet",
    "F5-002": "FrameNet",
    "F5-003": "HowNet / OpenHowNet",
    "F5-014": "WordNet",
}


def read_csv(path, columns, errors):
    """Read UTF-8 CSV (with or without BOM) and report malformed records."""
    records = []
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle, strict=True)
            headers = reader.fieldnames or []
            if len(headers) != len(columns) or set(headers) != set(columns):
                errors.append(
                    "{}: expected columns {}; found {}".format(
                        path.name, list(columns), headers
                    )
                )
                return records
            for row in reader:
                line = reader.line_num
                if None in row or any(value is None for value in row.values()):
                    errors.append(
                        "{}:{}: inconsistent number of CSV fields".format(
                            path.name, line
                        )
                    )
                    continue
                clean = {key: value.strip() for key, value in row.items()}
                for key in columns:
                    if key != "first_nonpass" and not clean[key]:
                        errors.append(
                            "{}:{}: {} is empty".format(path.name, line, key)
                        )
                records.append(clean)
    except (OSError, UnicodeError, csv.Error) as exc:
        errors.append("{}: {}".format(path.name, exc))
    return records


def check_equal(actual, expected, label, errors):
    if actual != expected:
        errors.append("{}: expected {!r}; found {!r}".format(label, expected, actual))


def check_id_set(actual, expected, label, errors):
    missing = sorted(expected - actual)
    unexpected = sorted(actual - expected)
    if missing or unexpected:
        errors.append(
            "{}: missing {}; unexpected {}".format(label, missing, unexpected)
        )


def validate_ids(records, label, errors):
    counts = Counter(row["resource_id"] for row in records)
    duplicates = sorted(key for key, count in counts.items() if count > 1)
    if duplicates:
        errors.append("{}: duplicate IDs {}".format(label, duplicates))
    for row in records:
        resource_id = row["resource_id"]
        if not re.fullmatch(r"F[1-5]-[0-9]{3}", resource_id):
            errors.append("{}: invalid resource ID {!r}".format(label, resource_id))
        if row["family_id"] not in FAMILY_NAMES:
            errors.append("{} {}: invalid family_id".format(label, resource_id))
        elif resource_id.split("-", 1)[0] != row["family_id"]:
            errors.append("{} {}: family_id disagrees with ID".format(label, resource_id))
    return set(counts)


def first_nonpass(row):
    for index, column in enumerate(STAGE_COLUMNS):
        if row[column] != "Pass":
            return index
    return None


def validate(screening, panel, errors):
    screening_ids = validate_ids(screening, "screening", errors)
    panel_ids = validate_ids(panel, "panel", errors)
    check_equal(len(screening), 224, "screening row count", errors)
    check_equal(len(screening_ids), 224, "unique screening IDs", errors)
    check_equal(len(panel), 77, "panel row count", errors)
    check_equal(len(panel_ids), 77, "unique panel IDs", errors)

    expected_ids = {
        "{}-{:03d}".format(family, index)
        for family, counts in EXPECTED_FAMILIES.items()
        for index in range(1, counts[0] + 1)
    }
    check_id_set(screening_ids, expected_ids, "initial candidate IDs", errors)
    nonpass = {stage: Counter() for stage in STAGES}
    supported_values = {"Pass", "Fail", "Unverified", "Not assessed"}
    for row in screening:
        resource_id = row["resource_id"]
        if row["family_id"] in FAMILY_NAMES:
            check_equal(
                row["family_name"], FAMILY_NAMES[row["family_id"]],
                resource_id + " family_name", errors,
            )
        try:
            url = urlsplit(row["source_url"])
            valid_url = url.scheme.lower() in {"http", "https"} and bool(url.hostname)
            valid_url = valid_url and not any(char.isspace() for char in row["source_url"])
        except ValueError:
            valid_url = False
        if not valid_url:
            errors.append(resource_id + ": source_url must be an absolute HTTP(S) URL")
        for column in STAGE_COLUMNS:
            if row[column] not in supported_values:
                errors.append(resource_id + ": invalid value for " + column)
        index = first_nonpass(row)
        if index is None:
            check_equal(row["screening_outcome"], "Advance", resource_id + " outcome", errors)
            check_equal(row["first_nonpass"], "", resource_id + " first_nonpass", errors)
        else:
            value = row[STAGE_COLUMNS[index]]
            nonpass[STAGES[index]][value] += 1
            if value not in {"Fail", "Unverified"}:
                errors.append(resource_id + ": the first non-Pass must be Fail or Unverified")
            check_equal(
                row["first_nonpass"], STAGES[index],
                resource_id + " first_nonpass", errors,
            )
            check_equal(
                row["screening_outcome"], "Not advanced",
                resource_id + " outcome", errors,
            )
            for column in STAGE_COLUMNS[index + 1:]:
                check_equal(row[column], "Not assessed", resource_id + " " + column, errors)

    advancing_ids = {
        row["resource_id"] for row in screening
        if row["screening_outcome"] == "Advance"
    }
    check_id_set(panel_ids, advancing_ids, "panel IDs versus Advance IDs", errors)
    screening_by_id = {row["resource_id"]: row for row in screening}
    for row in panel:
        resource_id = row["resource_id"]
        if row["panel_status"] not in {"Selected", "Alternative"}:
            errors.append(resource_id + ": invalid panel_status")
        if resource_id in screening_by_id:
            check_equal(
                row["family_id"], screening_by_id[resource_id]["family_id"],
                resource_id + " family across tables", errors,
            )
    selected_rows = [row for row in panel if row["panel_status"] == "Selected"]
    selected_ids = {row["resource_id"] for row in selected_rows}
    check_id_set(selected_ids, set(EXPECTED_SELECTED), "Selected IDs", errors)
    for row in selected_rows:
        if row["resource_id"] in EXPECTED_SELECTED:
            check_equal(
                row["resource_name"], EXPECTED_SELECTED[row["resource_id"]],
                row["resource_id"] + " selected name", errors,
            )

    totals = {
        "initial": len(screening),
        "after_s1": sum(row[STAGE_COLUMNS[0]] == "Pass" for row in screening),
        "after_s2": sum(all(row[col] == "Pass" for col in STAGE_COLUMNS[:2]) for row in screening),
        "advance": sum(all(row[col] == "Pass" for col in STAGE_COLUMNS) for row in screening),
        "selected": len(selected_rows),
        "alternative": sum(row["panel_status"] == "Alternative" for row in panel),
        "not_advanced": sum(row["screening_outcome"] == "Not advanced" for row in screening),
        "recorded_fail": sum(counts["Fail"] for counts in nonpass.values()),
        "unverified": sum(counts["Unverified"] for counts in nonpass.values()),
    }
    expected_totals = {
        "initial": 224, "after_s1": 99, "after_s2": 88, "advance": 77,
        "selected": 20, "alternative": 57, "not_advanced": 147,
        "recorded_fail": 127, "unverified": 20,
    }
    for key, expected in expected_totals.items():
        check_equal(totals[key], expected, "total " + key, errors)
    expected_nonpass = {
        "S1": {"Fail": 125},
        "S2": {"Fail": 1, "Unverified": 10},
        "S3": {"Fail": 1, "Unverified": 10},
    }
    for stage in STAGES:
        check_equal(dict(nonpass[stage]), expected_nonpass[stage], stage + " first non-pass", errors)

    families = {}
    for family, expected in EXPECTED_FAMILIES.items():
        s_rows = [row for row in screening if row["family_id"] == family]
        p_rows = [row for row in panel if row["family_id"] == family]
        values = (
            len(s_rows),
            sum(row[STAGE_COLUMNS[0]] == "Pass" for row in s_rows),
            sum(all(row[col] == "Pass" for col in STAGE_COLUMNS[:2]) for row in s_rows),
            sum(all(row[col] == "Pass" for col in STAGE_COLUMNS) for row in s_rows),
            sum(row["panel_status"] == "Selected" for row in p_rows),
            sum(row["panel_status"] == "Alternative" for row in p_rows),
            sum(first_nonpass(row) == 0 and row[STAGE_COLUMNS[0]] == "Fail" for row in s_rows),
            sum(first_nonpass(row) == 1 and row[STAGE_COLUMNS[1]] == "Fail" for row in s_rows),
            sum(first_nonpass(row) == 1 and row[STAGE_COLUMNS[1]] == "Unverified" for row in s_rows),
            sum(first_nonpass(row) == 2 and row[STAGE_COLUMNS[2]] == "Fail" for row in s_rows),
            sum(first_nonpass(row) == 2 and row[STAGE_COLUMNS[2]] == "Unverified" for row in s_rows),
        )
        families[family] = dict(zip(FAMILY_FIELDS, values))
        for field, actual, required in zip(FAMILY_FIELDS, values, expected):
            check_equal(actual, required, family + " " + field, errors)
    return {
        "status": "fail" if errors else "pass",
        "scope": "Internal record consistency only; source evidence and panel optimality are not revalidated.",
        "totals": totals,
        "first_nonpass": {stage: dict(nonpass[stage]) for stage in STAGES},
        "families": families,
        "selected": {row["resource_id"]: row["resource_name"] for row in selected_rows},
        "errors": errors,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", metavar="PATH", type=Path, help="also save the JSON report to PATH")
    args = parser.parse_args(argv)
    directory = Path(__file__).resolve().parent
    screening_path = directory / "screening.csv"
    panel_path = directory / "panel_selection.csv"
    errors = []
    screening = read_csv(screening_path, SCREENING_COLUMNS, errors)
    panel = read_csv(panel_path, PANEL_COLUMNS, errors)
    report = validate(screening, panel, errors)
    if args.json is not None:
        destination = args.json.resolve()
        protected = {screening_path.resolve(), panel_path.resolve(), Path(__file__).resolve()}
        if destination in protected:
            errors.append("--json must not overwrite either input CSV or this script")
        else:
            try:
                destination.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            except (OSError, UnicodeError) as exc:
                errors.append("Cannot write JSON report: {}".format(exc))
    report["status"] = "fail" if errors else "pass"
    totals = report["totals"]
    print("{}: {} -> {} -> {} -> {} -> {}; {} alternatives.".format(
        report["status"].upper(), totals["initial"], totals["after_s1"],
        totals["after_s2"], totals["advance"], totals["selected"],
        totals["alternative"],
    ))
    print("First non-pass: " + json.dumps(report["first_nonpass"], sort_keys=True))
    print("Families (initial/advance/selected/alternative): " + "; ".join(
        "{} {}/{}/{}/{}".format(
            family, counts["initial"], counts["advance"],
            counts["selected"], counts["alternative"],
        ) for family, counts in report["families"].items()
    ))
    print(report["scope"])
    for error in errors:
        print("ERROR: " + error)
    if args.json is not None and not errors:
        print("JSON report: " + str(args.json))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
