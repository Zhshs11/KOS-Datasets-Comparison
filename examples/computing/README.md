# Computing across KOS

One computing/programming theme is reused across the seven available KOS, with Python included where the local records support it. This is a small structural comparison, not an equivalence mapping or coverage benchmark.

## Files

- [KOS_Computing_Samples.xlsx](KOS_Computing_Samples.xlsx): the original 42-record selection, with native fields and source-row evidence. It does not include every neighbor added to the revised diagrams.
- [KOS_Computing_Structures.pdf](KOS_Computing_Structures.pdf): four pages, with each evidence table above its corresponding diagram.
- [KOS_Computing_Structures.tex](KOS_Computing_Structures.tex): self-contained editable LaTeX source for the PDF; no external images or data files are needed to compile it.

| KOS | What the example shows |
|---|---|
| DDC | Observed labels 004, 005 and 006, document titles and description excerpts; no official captions or sibling hierarchy are inferred. |
| UDC | Computer languages, computer programming and system software share Software as their broader concept. |
| LCC | Python, Pseudocode and RPG share printed language-list context; dashed layoutContains links are derived from indentation. |
| LCSH | Programming languages and Computer programming share a broader heading; Computer languages is a variant, not a sibling class. |
| SUMO | ComputerLanguage and ConstructedLanguage share ArtificialLanguage as a superclass; an existing logic rule is retained. |
| Wikidata | Applied and theoretical computer science share computer science as a superclass; this is a broader discipline-level example. |
| DBpedia | Python and Assembly language resources share a class type; Gramps has a programmingLanguage link to Python. |

Source workbook names, sheets and physical Excel row numbers appear in the PDF and LaTeX source. The seven illustrated examples use the retained [datasets](../../datasets/) collection; some neighboring rows are outside the [10,000-row subsets](../../cleaned_10000/).

Separate 10,000-row workbooks are now available for [FAST](../../cleaned_10000/FAST_10000.xlsx) and [YAGO 4.6](../../cleaned_10000/YAGO_4_6_10000.xlsx). Their small structural examples have not yet been added to this comparison. The PDF's status table distinguishes available datasets from pending diagrams. BabelNet still has no prepared sample, and WordNet remains deferred.

See the [dataset guide](../../Dataset_Guide.xlsx) for collection details and the [repository overview](../../README.md) for file locations.
