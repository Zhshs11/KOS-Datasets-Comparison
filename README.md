# Seven KOS Datasets and Structural Examples

This repository organizes the downloaded Excel data for DDC, UDC, LCC, LCSH, SUMO, Wikidata and DBpedia. The dataset collection covers the retained material across topics. A separate computing example illustrates selected organizational structures; it is not the scope of the dataset analysis.

## Contents

- [Dataset_Guide.xlsx](Dataset_Guide.xlsx): workbook inventory, native fields, partition reconciliation, row counts, tested joins and concrete limitations.
- [datasets/](datasets/): 48 dataset workbooks, organized by KOS. This includes 47 unchanged source copies and one reviewed SUMO replacement.
- [Computing example](examples/computing/README.md): a small, traceable illustration using one computing/programming theme.
- [Sample Excel](examples/computing/KOS_Computing_Samples.xlsx): 42 selected native records and their source-row evidence.
- [Structure diagrams](examples/computing/KOS_Computing_Structures.pdf): a three-page comparison of the selected structures.

There are 50 Excel workbooks in total: 48 dataset workbooks, one dataset guide and one sample workbook. The guide indexes all 63 input workbooks, including archive-only inputs that are not included here. Use its retention decision and output-path fields to identify the retained files. The original downloads and redundant ZIP packages are not part of this repository.

## Dataset overview

| System | Workbooks | Principal retained data |
|---|---:|---|
| [DDC](datasets/DDC/) | 8 | 942 observed labels; 271,060 documents and 271,060 assignments |
| [UDC](datasets/UDC/) | 2 | 2,452 Summary concepts; 1,001 companion documents and 649 notation links |
| [LCC](datasets/LCC/) | 1 | 9,967 source entries; 9,377 derived layout relationships |
| [LCSH](datasets/LCSH/) | 16 | 81,923 units; 213,958 statements; 11,463 ordered component rows |
| [SUMO](datasets/SUMO/) | 2 | 8,914 symbols; 11,024 reviewed binary symbol rows; 27,600 full native expressions |
| [Wikidata](datasets/Wikidata/) | 14 | 31,253 units; 150,305 statements; 123,233 qualifiers; 66,730 reference snaks |
| [DBpedia](datasets/DBpedia/) | 5 | 13,606 units; 49,728 statements |

These counts represent different kinds of records. Boundary identifiers, schema units, embedded nodes, source entries and observed corpus labels must not all be treated as comparable concepts.

## Reading and joining

1. Read `Overview` and `Issues` in the guide before interpreting the counts.
2. Use `Workbooks` to locate files and `Partitions` to assemble each logical table exactly once, in part order. Some initial segments are in the main Prepared workbook.
3. Use `Fields` for original column names, interpretation, actual types and missing counts. Use `Joins` for tested references and scope gaps.
4. Preserve identifiers, classification punctuation, original text, role/status, predicate, language, datatype and source locators. Optional blanks are not filled with invented values.

## Specific corrections and limits

- **SUMO:** `SUMO_Structural_Data.xlsx` replaces the original main workbook. It preserves Units, Texts and Sources. Statements retains only verified top-level ground expressions with two symbol arguments. The exclusion ledger lists 7,726 lossy projections and 114 numeric-argument rows outside that restricted view. The companion Native_Logic workbook preserves all complete expressions and dependencies.
- **DDC:** the existing duplicate flag describes normalized title/description families, excluding the label. There are 305 repeated families, but zero identical raw DDC/title/description triples. All records are retained. This corpus does not provide an official DDC schedule hierarchy.
- **UDC:** component matches are not complete compound-classmark interpretations. Native boundary URIs and unmatched documents remain available.
- **LCC:** layoutContains is derived from indentation and is not a verified subclass predicate.
- **Wikidata:** prepared statement IDs are unique; some native IDs repeat. Property metadata and qualifier/reference targets are not fully fetched. Use the exact counts in Joins.
- Some original acquisition/revision metadata cells are numeric Excel date serials; originals are preserved. Source version metadata remains in the native Sources sheets.

Source URLs, versions and rights notices remain source-specific; the collection does not assert a blanket redistribution licence. Refer to the guide and retained Sources sheets. Existing Sample_Manifest sheets describe earlier preparation only. 

## How the example relates to the analysis

The workbook inventory, field checks and record statistics describe the retained collection across topics. The computing example is an additional structural illustration. Python is reused in DDC, LCC and DBpedia; UDC, LCSH and SUMO use language categories, while the selected Wikidata chain is at a broader discipline level. These records do not assert cross-system equivalence.

Read the [example notes](examples/computing/README.md) for the selection rationale. The sample workbook's Evidence sheet points to paths relative to this repository root, preserving the source sheet, physical Excel row and record ID.
