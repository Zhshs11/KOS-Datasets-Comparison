# KOS Datasets and Structural Examples

Private research collection for DDC, UDC, LCC, LCSH, SUMO, Wikidata and DBpedia. Access is managed through this private repository.

## Files

- [cleaned_10000/](cleaned_10000/): seven cleaned Excel workbooks, each containing 10,000 data rows selected from the existing collection.
- [datasets/](datasets/): the earlier 48-workbook collection, including 47 unchanged downloaded copies and one reviewed SUMO workbook.
- [Dataset_Guide.xlsx](Dataset_Guide.xlsx): inventory, fields, partitions and checks for the earlier collection.
- [examples/computing/](examples/computing/): the existing 42-record sample workbook, structure PDF and example notes.

## Cleaned datasets

The total is 70,000 data rows. Headers, notes and source lists are excluded. A data row may be a concept, document, relationship, expression or reference value; 10,000 rows does not mean 10,000 concepts.

| Workbook | Data rows by sheet or record type |
|---|---|
| [DDC](cleaned_10000/DDC_10000.xlsx) | 942 observed labels + 4,529 documents + 4,529 assignments |
| [UDC](cleaned_10000/UDC_10000.xlsx) | 2,452 concepts + 2,724 relationships + 2,290 texts + 884 examples + 1,001 documents + 649 assignments |
| [LCC](cleaned_10000/LCC_10000.xlsx) | 5,295 source entries + 4,705 layout relationships |
| [LCSH](cleaned_10000/LCSH_10000.xlsx) | 10,000 statements, with available labels, classification details and ordered components attached |
| [SUMO](cleaned_10000/SUMO_10000.xlsx) | 5,652 complete expressions + 4,348 symbols |
| [Wikidata](cleaned_10000/Wikidata_10000.xlsx) | 5,152 statements + 1,849 qualifiers + 2,999 reference property values |
| [DBpedia](cleaned_10000/DBpedia_10000.xlsx) | 7,000 resource statements + 3,000 ontology statements |

Selection covers the topics available in the existing downloads. Redundant records and unnecessary management metadata are reduced while native text, identifiers, relationship meaning and source locations are preserved. Workbook notes explain the selection and remaining gaps.

DDC contains observed document labels rather than an official schedule. UDC uses the public Summary. LCC covers the retained H, N, Q and T material; its layout links are derived from indentation. Graph boundary records remain explicit. SUMO preserves complete selected expressions, and Wikidata keeps all qualifiers and reference rows attached to selected statements. These are finite research samples, not complete or semantically equivalent KOS datasets.

Source URLs, versions and rights notices remain in the workbooks. There is no blanket redistribution licence for the collection.
