# Sources, attribution, and coverage

This is an English Markdown adaptation of the final PerSpecML catalog, organized as sentence summaries, paragraph introductions, and dedicated detail pages. It is based on the two local PDFs listed below. The catalog structure is verified; the complete elicitation template and relationship tables are not available locally.

## Canonical sources and local copies

| Priority | Source | Local evidence |
|---|---|---|
| 1 | Hugo Villamizar, Marcos Kalinowski, Hélio Lopes, and Daniel Mendez, “Identifying concerns when specifying machine learning-enabled systems: A perspective-based approach”, The Journal of Systems and Software 213 (2024), 112053; [DOI](https://doi.org/10.1016/j.jss.2024.112053) | [Published article, 31 pages](1-s2.0-S0164121224000980-main.pdf) |
| 2 | [Zenodo record 10143970](https://zenodo.org/records/10143970), designated as the final artifact source in the conversion request | [Overview_online_material.pdf, 2 pages](Overview_online_material.pdf), an index of the package |
| 3 | [Miro board](https://miro.com/app/board/uXjVPiQXg7E=/), referenced by the package overview for Product Classification and Market | No local export; Figure 4 of the article reproduces only part of a specification template |

The package index lists `FINAL Artifacts_PerSpecML.pdf`, but that file is absent. The index is not a substitute for its contents. Neither the full template nor the narrative relationship tables could be inspected. No external pages or downloads were used for this adaptation, and the current version of the live Zenodo record and Miro board was not checked.

The article's repository reference, footnote 1 on p. 10, is [10.5281/zenodo.7705002](https://doi.org/10.5281/zenodo.7705002). Its relationship to the requested record 10143970 cannot be established from these PDFs. Both identifiers are retained without asserting that they are equivalent.

The article also points to the [Miroverse template](https://miro.com/miroverse/perspecml-machine-learning/) on p. 23 and cites the 2023 template by Hugo Villamizar, Marcos Kalinowski, and Hélio Lopes on p. 31. The template and the case-study board are distinct references; this adaptation does not assume their current contents match.

### Local source fingerprints

SHA-256 values identify the exact local copies inspected on 2026-09-15:

- `1-s2.0-S0164121224000980-main.pdf`: `b75fd17715510565bd9b84c879ab8070292f6e49f118c17d659bfebda0f5b842`
- `Overview_online_material.pdf`: `b57d1c23d3902de1feff586e45872ae6428f87757bb2ce464aed40c208a38d07`

All page numbers refer to the numbered PDF pages. The article's printed page numbers and PDF page positions coincide.

## Attribution and license

Credit the PerSpecML research to Hugo Villamizar, Marcos Kalinowski, Hélio Lopes, and Daniel Mendez, with the article citation above. The article separately credits the online template to Villamizar, Kalinowski, and Lopes.

The conversion request identifies the Zenodo material as licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). Preserve that attribution, the Zenodo source link, the license link, and an indication of changes when reusing that material. The local overview does not reproduce the license metadata or establish the full artifact's creator list; those details remain to be checked against the actual artifact or record.

The article's first page states © 2024 Elsevier Inc., all rights reserved. Its quoted definitions are attributed to the article, and the Zenodo license is not asserted to cover the article PDF or every quotation in this adaptation. The surrounding skills repository's license is likewise not substituted for the source materials' notices.

Changes made in this adaptation: English editorial summaries and introductions; folder-based navigation; separation of definitions, elicitation, and relationships; explicit source annotations; expansion of diagram ID ranges; and a visible record of conflicting names and missing evidence. No endorsement by the original authors is implied.

## Reading structure

- The root README introduces each perspective in one sentence.
- Each perspective folder starts with a paragraph explaining its nature, then presents tasks, stakeholders, and a sentence linking to each concern folder.
- The global concern index repeats those same one-sentence summaries.
- Each concern folder starts with a paragraph of context and links to the available detail.
- Definition, elicitation, and relationship files carry their own exact references. An aspect file is omitted when no substantive content is available; the concern README records the coverage gap.

Tasks remain sections of perspective READMEs. Stakeholders remain with their tasks. Relationships remain within concern folders. There are no standalone task, actor, or relationship entities outside that structure.

Introductions, summary sentences, task descriptions, and relationship explanations are editorial paraphrases. Block quotations in definition and elicitation files preserve source wording, with layout, line breaks, and typographic emphasis normalized for Markdown.

## Source-to-content map

| Content | Exact source |
|---|---|
| Stakeholder descriptions | Article section 3.1, pp. 4–5 |
| System Objectives tasks and definitions | Table 1, p. 6; Table 6, p. 8 |
| User Experience tasks and definitions | Table 2, p. 6; Table 7, p. 8 |
| Infrastructure tasks and definitions | Table 3, p. 7; Table 8, p. 9 |
| Model tasks and definitions | Table 4, p. 7; Table 9, p. 9 |
| Data tasks and definitions | Table 5, p. 7; Table 10, p. 10 |
| Perspective nature and purpose | Section 3.4, pp. 6–8 |
| Task–concern and task–stakeholder assignments | Figure 2, p. 11 |
| Diagram relationship references | Figure 2, p. 11, including bracketed ID lists |
| Examples of relationship explanations | Section 3.5, p. 10; section 3.9, p. 14 |
| Template structure and experimentation marker | Section 3.7, pp. 11–12; Figures 3–4 |
| Five recoverable template questions | Figure 4, p. 12 |
| Application workflow and applicability | Section 3.8, p. 12; Figure 5, p. 13 |
| Sentiment-analysis specification example | Section 3.9, pp. 13–15; Tables 12–13 |
| Limits of applicability, including supervised-learning focus | Section 10.2, p. 29 |
| Package file descriptions | Overview_online_material.pdf, pp. 1–2 |

### Stakeholders

Figure 2 assigns five role labels to tasks: BO — Business Owner; DE — Domain Expert; DG — Designer; DS — Data Scientist; SE — Software/ML Engineer. SE is one combined label, not two counted roles.

Requirements Engineers are a sixth stakeholder category discussed in section 3.1, with a facilitation role also described in section 3.8. Figure 2 does not assign a separate Requirements Engineer label to individual tasks, so no such assignments have been invented.

### Structural inventory

Counts were recalculated from the table rows and Figure 2, rather than copied from the article's abstract.

| Perspective | Tasks | Concerns | IDs | Task–role associations | Task–concern associations | Diagram references |
|---|---:|---:|---|---:|---:|---:|
| O — System Objectives | 4 | 10 | O1–O10 | 10 | 10 | 13 |
| U — User Experience | 5 | 9 | U1–U9 | 9 | 9 | 5 |
| I — Infrastructure | 8 | 11 | I1–I11 | 12 | 11 | 30 |
| M — Model | 5 | 14 | M1–M14 | 7 | 14 | 44 |
| D — Data | 6 | 16 | D1–D16 | 11 | 16 | 4 |
| Total | 28 | 60 | 60 unique IDs | 49 | 60 | 96 |

The diagram has references printed under 30 concerns. Expanding those references produces 96 ordered source-location pairs and 94 distinct unordered pairs: I1–M7 and I1–M12 occur in both directions. These references touch 50 concerns. Ten concerns have neither an outgoing nor incoming explicit diagram reference: O2, O6, O7, O8, U1, U4, U8, I9, D2, and D4.

Two additional connections are identified from the article's prose and kept separate from that diagram count: Context–Ethics (O1–D12), section 3.9, p. 14; and algorithm selection–explainability (M1–M11), section 3.5, p. 10. Their ID mappings are editorial: the text names the concepts rather than printing these ID pairs.

### Relationship evidence

Relationship pages distinguish where a reference is printed from what it means:

- “Listed under this concern” transcribes Figure 2's outgoing bracketed references.
- “Listed under other concerns” provides incoming navigation without adding a new source relationship.
- “Additional discussion in the article” identifies prose connections absent from the diagram, with explicit source and mapping notes.
- Explanations are included only where the inspected article explains the pair; otherwise the page says no explanation was found in the inspected material.

The three occurrences of `D6:D12` under I3, I5, and M13 expand to seven IDs each. This preserves the diagram's IDs; it does not silently permute D9, D10, and D11 to match their differing names. Lowercase `i10` under M3 is linked to I10, and the normalization is explicitly recorded.

The labels `diagram-only` and `relationship-table-only` are reserved for a completed comparison with the narrative relationship tables. They cannot truthfully be assigned while those tables are absent. Current relationship pages say the table comparison is unavailable. Absence from the inspected article is not evidence of absence from the missing artifact.

No direction of influence is inferred merely from which concern contains a bracketed reference. Nor does lack of a reciprocal reference automatically establish a mistake: for example, U5 lists I3, while I3 lists U6. Those references are retained as printed.

### Elicitation and refinement coverage

Five question prompts can be read in Figure 4:

| Concern folder used here | Topic in the reproduced template | Mapping status |
|---|---|---|
| M3 | Model input and output | Explicit concept match; Figure 4 prints no concern ID |
| M1 | Set of candidate algorithms | Explicit concept match; Figure 4 prints no concern ID |
| D1 | Data source/origin | Explicit concept match; Figure 4 prints no concern ID |
| D5 | Amount of selected data | Editorial mapping to Quantity |
| D4 | Meaning of collected data and data dictionary | Explicit concept match; Figure 4 prints no concern ID |

These mappings make the excerpt navigable; they do not certify that the full final template has the same wording or grouping. The other 55 concern READMEs record the absence of a recoverable concern-specific template question. Generic prose questions and historical questionnaires are not substituted for missing final prompts.

Section 3.7 describes one refinement marker, E, for tasks involving experimentation. Figure 4 shows it twice, on the model input/output block and candidate-algorithm block. These are the two observed occurrences, not a count for the unavailable full template.

Figure 5 has two outcomes for the applicability decision: True and False. Section 3.8 describes four application steps. No operational relevance scale is enumerated in the inspected final presentation; the prioritization suggestion on p. 27 and historical evaluation scales are not treated as final concern relevance levels.

## Differences and unresolved coverage

| Area | Conflicting or incomplete evidence | Treatment |
|---|---|---|
| D9 | Table 10: Real usage; Figure 2: Consistency | Folder name and definition follow Table 10; both labels are retained in source notes |
| D10 | Table 10: Bias; Figure 2: Real usage | Same treatment |
| D11 | Table 10: Consistency; Figure 2: Bias | Same treatment |
| M2 | Table 9: Algorithm tuning; Figure 2: Hyperparameter tuning | Table name retained; diagram variant recorded |
| M3 | Table 9: Input & Output; Figure 2: Inputs & outputs | Table name retained |
| M8 | Table 9: Model size; Figure 2: Model size & complexity | Table name retained without dropping complexity from the definition |
| M11 | Table 9: Interpretability & Explainability; Figure 2: Explainability & Interpretability | Table name retained |
| U9 and D14 | Tables capitalize Training and Modeling; Figure 2 uses lowercase | Table capitalization retained |
| M1 and M3 task headings | Figure 4 uses candidate-algorithm and input/output headings different from the final task groupings | Questions retain their original headings; final task assignments still come from Figure 2 |
| Infrastructure task heading | Table 3: Transport data to the model; Figure 2: Transport data to the ML model | Table task name retained |
| Infrastructure relationship count | Text on p. 14 says seven concerns; Figure 2 has references under six, I1–I6 | Structural inventory uses the actual diagram count |
| M3 reference | Figure 2 prints lowercase i10 | Link targets I10; normalization recorded |
| M13 definition | Table 9 does not say how the model should treat different groups | Quotation preserved without completing it; overview also cites section 3.4 |
| D16 scope | Table 10 describes monitoring later data; Table 5 describes training/evaluation ground truth | Both stated uses are recorded |
| Context–Ethics | Section 3.9 discusses the connection; Figure 2 lists only M13 and M14 under O1 | Included as separately attributed article prose |
| Algorithm selection–explainability | Section 3.5 discusses the connection; Figure 2 omits the M1–M11 pair | Included as separately attributed article prose |
| Model metrics versus explainability | Section 3.5 describes a trade-off with accuracy without providing an ID pair | Retained as prose in the M11 relationship page, without adding a diagram edge |
| Stakeholder count | Five task labels in Figure 2; six categories discussed in section 3.1 | Separate counts and facilitator role documented |
| Zenodo locator | Article cites 7705002; request identifies 10143970 | Both retained; version relationship unverified |
| Full artifact, relationship tables, and Miro | No local final artifact or board export | No claim of complete cross-source agreement |

The removal of relationship representations from the specification template is intentional, according to p. 23. Their absence from that template alone is not a discrepancy.

The historical 45-, 52-, and 59-concern versions are outside this final catalog. Historical validation examples and diagrams are identified as such and are not used to fill gaps in the 60-concern version.

## Artifact and example inventory

The overview enumerates 12 files and one Miro board:

- Academic validation: `ACAD_Specification_Assignment.pdf`, `ACAD_Catologue_of_Concerns.png`, and `ACAD_FollowUp-Questionnaire.pdf`.
- Static validation: `STATIC_Candidate_Solution.png`, `STATIC_Characterization_Questionnaire.pdf`, `STATIC_Specification_Project_A.png`, `STATIC_Specification_Project_B.png`, `STATIC_FollowUp_Questionnaire.pdf`, and `STATIC_Transcription.pdf`.
- Dynamic validation: `DYNAMIC_FollowUp_Questionnaire.pdf` and `DYNAMIC_Transcription.pdf`, plus the board for Product Classification and Market.
- Final package: `FINAL Artifacts_PerSpecML.pdf`, described as containing the catalog, application guide, diagram, template, and concern relationships.

Those enumerated files are not present locally. The published article contains the final catalog and diagram, and a template excerpt. PerSpecML's two principal operational artifacts are the Perspective-Based ML Task and Concern Diagram and the Perspective-Based ML Specification Template.

| Example | Exact source | Coverage |
|---|---|---|
| Sentiment analysis of customer reviews | Article section 3.9, pp. 13–15; Tables 12–13 | Final-presentation example: 10 System Objectives and 11 Infrastructure specifications, plus a user story and 10 additional requirements |
| Bank loan | Section 5.1, p. 17 | Historical academic exercise |
| Project A: refinery odor alerts | Table 16 and section 6.1, p. 20 | Historical static validation, PerSpecML v1 |
| Project B: refinery flame monitoring | Table 16 and section 6.1, p. 20 | Historical static validation, PerSpecML v1 |
| Product Classification | Table 19, p. 24; overview p. 2 | Dynamic validation, PerSpecML v2; full specification referenced on Miro |
| Market | Table 19, p. 24; overview p. 2 | Dynamic validation, PerSpecML v2; full specification referenced on Miro |

The article mentions another complete example in the online template. Its identity and possible overlap with these six named scenarios cannot be checked locally.

## Local verification

The Markdown adaptation was checked on 2026-09-15 using the available PDF tools and Python's standard library, without installing dependencies or adding a documentation generator.

- 183 Markdown files: 67 READMEs, this source register, 60 definition pages, 5 elicitation pages, and 50 relationship pages.
- Exactly 5 perspective folders and 60 concern folders, each with its own README.
- Unique, gap-free concern IDs in O1–O10, U1–U9, I1–I11, M1–M14, and D1–D16.
- Task distribution 4, 5, 8, 5, 6; concern distribution 10, 9, 11, 14, 16.
- Each concern linked from exactly one perspective task; 49 task–role associations.
- All 60 canonical names and quoted definitions compared against the extracted PDF table rows.
- 96 outgoing diagram references and matching incoming navigation; 94 distinct unordered diagram pairs.
- 1,740 relative links checked, including folder README resolution and Markdown heading anchors.
- The PDF fingerprints remained unchanged; only Markdown documentation was added.

These checks establish structural consistency and fidelity to the available sources. They do not certify the absent final template, relationship tables, or live Miro content.

## Remaining source work

The Markdown structure can be used to navigate the verified final catalog now. Completing source coverage requires the actual final artifact or an equivalent local export to recover the remaining elicitation prompts, compare narrative relationship tables, confirm relevance levels if any, and check current artifact attribution and license metadata. No absent definition, question, explanation, or applicability state has been invented.

[PerSpecML overview](README.md) · [All concerns](concerns/).
