# Computing across KOS

One computing/programming theme is reused across the nine available KOS, with Python included where the local records support it. This is a small structural comparison, not an equivalence mapping or coverage benchmark.

## Files

- [KOS_Computing_Samples.xlsx](KOS_Computing_Samples.xlsx): the original 42-record selection for seven KOS, with native fields and source-row evidence. It excludes FAST, YAGO 4.6, the added official DDC summary context and some neighbors in the revised diagrams.
- [KOS_Computing_Structures.pdf](KOS_Computing_Structures.pdf): five pages, with each evidence table above its corresponding diagram.
- [KOS_Computing_Structures.tex](KOS_Computing_Structures.tex): self-contained editable LaTeX source for the PDF; no external images or data files are needed to compile it.

| KOS | What the example shows |
|---|---|
| DDC | Local document assignments to 004, 005 and 006, with their shared division 000 (000-009) and main class 000 (000-099) added from OCLC's official summaries. |
| UDC | Computer languages, computer programming and system software share Software as their broader concept. |
| LCC | Python, Pseudocode and RPG share printed language-list context; dashed layoutContains links are derived from indentation. |
| LCSH | Programming languages and Computer programming share a broader heading; Computer languages is a variant, not a sibling class. |
| SUMO | ComputerLanguage and ConstructedLanguage share ArtificialLanguage as a superclass; an existing logic rule is retained. |
| Wikidata | Applied and theoretical computer science share computer science as a superclass; this is a broader discipline-level example. |
| DBpedia | Python and Assembly language resources share a class type; Gramps has a programmingLanguage link to Python. |
| FAST | Kotlin and Wolfram language share a broader heading; Wolfram language has another broader heading and a mapping to LCSH. |
| YAGO 4.6 | Source code and Control flow are subclasses of Computer code, which is a subclass of Text (literary theory). |

Source workbook names, sheets and physical Excel row numbers appear in the PDF and LaTeX source. The original seven illustrated examples use the retained [datasets](../../datasets/) collection; some neighboring rows are outside the [10,000-row subsets](../../cleaned_10000/). The DDC diagram also adds hierarchy from the [OCLC DDC Summaries](https://www.oclc.org/content/dam/oclc/dewey/ddc23-summaries.pdf), distinguished from document assignments recorded in Excel.

Page 5 uses relationships directly from the [FAST](../../cleaned_10000/FAST_10000.xlsx) and [YAGO 4.6](../../cleaned_10000/YAGO_4_6_10000.xlsx) 10,000-row workbooks. These show language headings and code classes at different levels of the shared theme. BabelNet has no prepared sample, and WordNet remains deferred.

See the [dataset guide](../../Dataset_Guide.xlsx) for collection details and the [repository overview](../../README.md) for file locations.
