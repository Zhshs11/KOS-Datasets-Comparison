# Computing across seven KOS

This small comparison uses one shared computing/programming theme and reuses Python wherever the supplied records support it. All samples come from the previously organized Excel collection. No external records or invented instances were added.

- [KOS_Computing_Samples.xlsx](KOS_Computing_Samples.xlsx) contains an overview, one worksheet per KOS and exact source-row evidence. Each block retains selected native columns; `evidence_ref` is an added pointer to the Evidence sheet.
- [KOS_Computing_Structures.pdf](KOS_Computing_Structures.pdf) draws the selected relationships. Solid arrows follow the retained relation direction. LCC layout relations are explicitly marked as derived.

| KOS | Selected anchor | Interpretation |
|---|---|---|
| DDC | Python pocket reference -> 005 | Existing third-party document label; no official DDC schedule path is reconstructed. |
| UDC | Computer languages (004.43) | Subject category under Software (004.4) and Computing (004). |
| LCC | Python (QA76.73.P98) | Printed entry under programming-language context; layoutContains is derived from indentation. |
| LCSH | Programming languages (Electronic computers) | Broader authority plus the variant label Computer languages. |
| SUMO | ComputerLanguage | Ontology class, subclass facts and an existing membership-inheritance rule. |
| Wikidata | computer science (Q21198) | A broader discipline-level subclass chain, with native statement IDs and rank. |
| DBpedia | Python (programming language) | A resource with a class type and an incoming programmingLanguage relation from Gramps. |

The common theme is not an equivalence mapping. In particular, the book, schedule entry, authority, ontology class and resource are different kinds of objects. The selected Wikidata records are broader than programming languages. Missing Python-level records in this bounded sample do not imply that the complete KOS lacks them.

## Traceability

Open the matching KOS worksheet for its native rows. Use `evidence_ref` to find the source filename, sheet, physical Excel row and original record ID. `source_workbook` paths are relative to the repository root, which contains the `datasets` directory. Original source text, identifiers and blank values remain unchanged in the selected columns.

This is a deliberate teaching sample, not a statistical benchmark or an assessment of overall KOS coverage. Each diagram shows one useful structure without adding unrelated examples. The [dataset guide](../../Dataset_Guide.xlsx) retains full scope and source-rights information. Return to the [repository overview](../../README.md) for the complete retained collection.
