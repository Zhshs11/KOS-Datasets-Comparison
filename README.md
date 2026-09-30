# KOS Datasets and Structural Examples

Research collection for DDC, UDC, LCC, LCSH, SUMO, Wikidata, DBpedia, FAST, YAGO 4.6 and BabelNet.

## Files

| Location | Contents |
|---|---|
| [cleaned_10000/](cleaned_10000/) | Ten cleaned Excel workbooks, with 10,000 data rows per KOS. |
| [datasets/](datasets/) | Earlier 48-workbook collection: 47 unchanged downloaded copies and one reviewed SUMO workbook. |
| [Dataset_Guide.xlsx](Dataset_Guide.xlsx) | Inventory, fields, partitions and checks for the earlier collection. |
| [examples/computing/](examples/computing/) | Computing examples, an Excel sample, and the revised structure comparison in [PDF](examples/computing/KOS_Computing_Structures.pdf) and editable [LaTeX](examples/computing/KOS_Computing_Structures.tex). |

The cleaned workbooks contain 100,000 data rows in total, excluding headers, notes and source lists. Rows can represent concepts, documents, relationships, expressions or references; they are not all concepts. Each workbook explains its selection, fields and source locations.

- [DDC](cleaned_10000/DDC_10000.xlsx): the original 10,000 rows are preserved. Seven added columns in `Units` provide DDC 23 summary parent/main-class groups and sources for 873 observed labels. The 58 unassigned and 11 optional numbers are flagged without new hierarchy links; 20 matched rows have an uncertain parent caption marked in the workbook. This adds summary context, not full WebDewey hierarchy or validation of the original document assignments.
- [FAST](cleaned_10000/FAST_10000.xlsx): 10,000 semantic statements selected across topics and facets through OCLC's official SRU interface. This is a query-based sample, not a full-database probability sample.
- [YAGO 4.6](cleaned_10000/YAGO_4_6_10000.xlsx): 10,000 native subclass relationships from the official taxonomy and schema files, with available labels and source locations. This covers class structure rather than entity facts.
- [BabelNet](cleaned_10000/BabelNet_10000.xlsx): 10,000 distinct child-parent pairs from the THUNLP BabelNet-Sememe-Prediction research subset, with labels and definitions matched from MSGI, original relation types and source-row references. This is a research subset, not a complete BabelNet export. See the [source notes](cleaned_10000/BabelNet_SOURCE_NOTES.md).

The comparison reuses computing/Python where the retained data supports it. Tables precede diagrams, with neighboring entries and relationship types identified. Some context comes from the full retained collection rather than the 10,000-row subsets. DDC document assignments come from the local corpus, with broader groups added from OCLC's official summaries; LCC layout links are derived from indentation. The nine samples are not equivalent in scope or granularity.

The published five-page PDF and its LaTeX source cover nine KOS, including FAST subject headings and mappings and YAGO 4.6 code classes. BabelNet is now available in the cleaned workbooks; its PDF addition has not been published. WordNet remains deferred.

Source details and rights notices remain in the workbooks. This collection has no blanket redistribution licence.
