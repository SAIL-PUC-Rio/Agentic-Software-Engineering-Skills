# D — Data

The Data perspective examines whether the data can support the intended ML problem. It covers collection, selection, description, and quality, including ethical considerations and protection of individual identities. It also addresses the operations needed for the model's representation, dataset splitting, and a reference dataset approved by a domain expert.

6 tasks · 16 concerns · D1–D16.

## How to use this perspective

Work through the tasks with the recommended stakeholders, open each concern for context, and inspect its available definition, questions, and relationships before deciding applicability. The task groups organize specification discussions; they do not prescribe a separate implementation schedule.

## Collect data

Obtain the data needed for model development and evaluation in time for its use.

Recommended stakeholders: Data Scientist (DS); Software/ML Engineer (SE).

- [D1 — Source](../../concerns/d1-source/): Identify where the data will be obtained.
- [D2 — Timeliness](../../concerns/d2-timeliness/): Specify the delay between expected and actual data availability.

## Select and describe data

Choose relevant data and describe its features.

Recommended stakeholders: Data Scientist (DS); Domain Expert (DE).

- [D3 — Data selection](../../concerns/d3-data-selection/): Determine which data types and samples should be collected.
- [D4 — Data dictionary](../../concerns/d4-data-dictionary/): Describe data elements through their names, definitions, and attributes.
- [D5 — Quantity](../../concerns/d5-quantity/): Specify the expected amount of data for the problem and algorithm.

## Evaluate high-quality data

Assess whether the data meets the quality criteria needed for reliable results.

Recommended stakeholders: Data Scientist (DS); Domain Expert (DE).

- [D6 — Accuracy](../../concerns/d6-accuracy/): Determine the need for correct data.
- [D7 — Completeness](../../concerns/d7-completeness/): Determine whether data covers the situations in which the model will operate.
- [D8 — Credibility](../../concerns/d8-credibility/): Determine the need for true data that users find believable and understandable.
- [D9 — Real usage](../../concerns/d9-real-usage/): Determine whether data represents the real problem the model will face.
- [D10 — Bias](../../concerns/d10-bias/): Determine the need for fair samples and representative data distributions.
- [D11 — Consistency](../../concerns/d11-consistency/): Determine whether data is consistent within its specific context.
- [D12 — Ethics](../../concerns/d12-ethics/): Identify potential adverse societal effects associated with the data.
- [D13 — Anonymization](../../concerns/d13-anonymization/): Determine how to protect individual identities while keeping data useful for ML.

## Convert data in the representation of the ML model

Transform raw data into a representation the algorithm can process.

Recommended stakeholders: Data Scientist (DS); Domain Expert (DE).

- [D14 — Data operations & Modeling](../../concerns/d14-data-operations-modeling/): Specify the operations that convert data into the model's required representation.

## Split dataset

Divide the available data into training, validation, and test subsets.

Recommended stakeholders: Data Scientist (DS).

- [D15 — Data distribution](../../concerns/d15-data-distribution/): Specify data distributions and the split into training, validation, and test sets.

## Define a golden dataset

Define a high-quality reference dataset representing the problem domain.

Recommended stakeholders: Data Scientist (DS); Domain Expert (DE).

- [D16 — Golden dataset](../../concerns/d16-golden-dataset/): Determine the need for a domain-approved reference dataset representing the problem.

## Source notes

The introductory paragraph and task descriptions are editorial paraphrases of the article, section 3.4 and [Table 5, p. 7](../../1-s2.0-S0164121224000980-main.pdf#page=7). Concern names follow [Table 10, p. 10](../../1-s2.0-S0164121224000980-main.pdf#page=10); task–concern and task–stakeholder assignments come from [Figure 2, p. 11](../../1-s2.0-S0164121224000980-main.pdf#page=11).

Table 10 and Figure 2 disagree on the names assigned to D9–D11. This page uses Table 10; the corresponding concern pages preserve the conflicting diagram labels. The Golden dataset task and concern also describe different uses.

Requirements Engineers facilitate the discussion but have no separate task assignments in Figure 2. Complete elicitation questions and relationship tables are unavailable in the local material; see [sources, differences, and coverage](../../SOURCES.md).

[All concerns](../../concerns/) · [PerSpecML overview](../../README.md).
