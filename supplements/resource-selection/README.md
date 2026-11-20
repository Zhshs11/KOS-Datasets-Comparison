# Knowledge Resource Selection from 224 Resources to 20 Candidates

Version 1.0. This supplement records eligibility screening of 224 knowledge resources and the selection of a 20-resource comparison panel across five KOS families.

The recorded sequence is **224 → 99 → 88 → 77 → 20**. The first three checks concern broad scope, usable English semantic content, and an accepted free public access route. The final step is a qualitative panel design: the other 57 eligible resources remain documented alternatives, rather than failed resources. The 20 candidates are intended for subsequent within-family assessment; they are not five family winners.

## Files

| File | Contents |
|---|---|
| [Selection record](Knowledge_Resource_Selection_Process_224_to_20.docx) | Explanatory text, stage counts, all 224 screening records and all 77 panel decisions. Resource links and internal table links support navigation. |
| [screening.csv](screening.csv) | Resource IDs, family labels, source pointers, three recorded checks, outcomes and decision bases. |
| [panel_selection.csv](panel_selection.csv) | Organizational contrasts, source relationships, selection rationales and panel membership for the 77 advancing resources. |
| [selection_summary.json](selection_summary.json) | Stage counts, per-family counts and the 20 selected IDs. |
| [validate_selection.py](validate_selection.py) | Checks IDs, sequential screening, counts, source URL form and panel membership using the Python standard library. |
| [build_document.py](build_document.py) | Rebuilds the Word document from the CSV tables and summary. Requires [requirements.txt](requirements.txt). |

`Pass`, `Fail` and `Unverified` preserve the recorded decisions. `Not assessed` means a later check was not reached after an earlier non-pass; the document displays this as a dash. Non-advancing entries are assigned to their first non-pass, preventing double counting.

## Reproduce the reported record

Download this folder from a single Git commit and run the following commands inside it with Python 3.10 or later:

```sh
python validate_selection.py
```

The expected totals are 224 initial resources, 99 after scope screening, 88 after English-content screening, 77 after public-access screening, 20 selected resources and 57 alternatives. Validation also checks:

```text
224 = 125 scope non-passes + 11 English non-passes
    + 11 access non-passes + 57 alternatives + 20 selected
```

To regenerate the document, first make a working copy of this folder: the builder overwrites the DOCX beside the script.

```sh
python -m pip install -r requirements.txt
python build_document.py
```

The scripts use local files and make no network requests. The published document was visually checked in Microsoft Word with Times New Roman installed. Pagination may differ across renderers; document metadata can also differ after rebuilding, so byte-identical output is not expected.

## Scope and provenance

The supplied selection record cites `KOS_Candidate_Catalog_en.xlsx` (Candidate catalog) and `KOS_Candidate_Catalog_after_en.xlsx` (Screening decisions and Candidate catalog) as its underlying records. The CSV files expose the decisions reported in the supplement; those original workbooks and discovery search logs are not included in this folder.

This package supports reconstruction and checking of the reported decisions and counts. It does not rerun the original discovery search, independently verify current source eligibility, or algorithmically derive a unique 20-resource panel. Source URLs reproduce the recorded pointers and were not revalidated for this release. Accepted access can refer to a bounded public subset, historical release or registered academic route; it does not imply unrestricted access to a complete resource. Resource providers' terms continue to apply.

## Citation

Cite **Knowledge Resource Selection from 224 Resources to 20 Candidates**, version 1.0, in the *KOS-Datasets-Comparison* repository, and include the permalink for the Git commit consulted. On GitHub, open the relevant commit and copy the link to this folder or the document. Use that fixed link rather than a moving `main` link so readers can retrieve the same version. This supplement has no assigned DOI.
