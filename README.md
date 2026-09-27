# KOS Datasets and Structural Examples

Private research collection for DDC, UDC, LCC, LCSH, SUMO, Wikidata, DBpedia, FAST and YAGO 4.6. Project files are shared through this private repository with invited collaborators.

## Files

| Location | Contents |
|---|---|
| [cleaned_10000/](cleaned_10000/) | Nine cleaned Excel workbooks, with 10,000 data rows per KOS. |
| [datasets/](datasets/) | Earlier 48-workbook collection: 47 unchanged downloaded copies and one reviewed SUMO workbook. |
| [Dataset_Guide.xlsx](Dataset_Guide.xlsx) | Inventory, fields, partitions and checks for the earlier collection. |
| [examples/computing/](examples/computing/) | Computing examples, an Excel sample, and the revised structure comparison in [PDF](examples/computing/KOS_Computing_Structures.pdf) and editable [LaTeX](examples/computing/KOS_Computing_Structures.tex). |

The cleaned workbooks contain 90,000 data rows in total, excluding headers, notes and source lists. Rows can represent concepts, documents, relationships, expressions or references; they are not all concepts. Each workbook explains its selection, fields and source locations.

- [FAST](cleaned_10000/FAST_10000.xlsx): 10,000 semantic statements selected across topics and facets through OCLC's official SRU interface. This is a query-based sample, not a full-database probability sample.
- [YAGO 4.6](cleaned_10000/YAGO_4_6_10000.xlsx): 10,000 native subclass relationships from the official taxonomy and schema files, with available labels and source locations. This covers class structure rather than entity facts.

The comparison reuses computing/Python where the retained data supports it. Tables precede diagrams, with neighboring entries and relationship types identified. Some context comes from the full retained collection rather than the 10,000-row subsets. DDC has observed document labels, not an official schedule; LCC layout links are derived from indentation. The seven samples are not equivalent in scope or granularity.

The illustrated comparison covers the original seven KOS. FAST and YAGO 4.6 now have cleaned workbooks; their small structural examples are pending. BabelNet has no prepared sample, and WordNet remains deferred.

Source details and rights notices remain in the workbooks. This collection has no blanket redistribution licence.
