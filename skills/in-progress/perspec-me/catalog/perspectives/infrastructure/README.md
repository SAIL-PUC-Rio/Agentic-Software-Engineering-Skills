# I — Infrastructure

The Infrastructure perspective connects an ML model to an operational software system. It addresses data transport, serving and updating the model, storing artifacts, observing behavior, and automating the workflow. Integration and financial cost complete the view of the infrastructure needed to operate and maintain the system.

8 tasks · 11 concerns · I1–I11.

## How to use this perspective

Work through the tasks with the recommended stakeholders, open each concern for context, and inspect its available definition, questions, and relationships before deciding applicability. The task groups organize specification discussions; they do not prescribe a separate implementation schedule.

## Transport data to the model

Move relevant data from its source to the model for analysis, training, or prediction.

Recommended stakeholders: Software/ML Engineer (SE).

- [I1 — Data streaming](../../concerns/i1-data-streaming/): Specify how data travels to the model, including real-time or batch delivery.

## Make the ML model available

Deploy and expose the trained model so it can be accessed for predictions.

Recommended stakeholders: Software/ML Engineer (SE); Data Scientist (DS).

- [I2 — Model serving](../../concerns/i2-model-serving/): Choose how the model will be executed and made available for consumption.

## Update the ML model

Plan improvements or modifications to an existing model.

Recommended stakeholders: Software/ML Engineer (SE); Data Scientist (DS).

- [I3 — Incremental learning](../../concerns/i3-incremental-learning/): Determine whether the system must keep learning from new data.

## Store ML artifacts

Organize the storage and management of artifacts generated during ML development.

Recommended stakeholders: Software/ML Engineer (SE).

- [I4 — Storage](../../concerns/i4-storage/): Specify where ML artifacts will be stored.

## Observe the ML model

Analyze the performance, behavior, and outcomes of the model and surrounding system.

Recommended stakeholders: Software/ML Engineer (SE).

- [I5 — Monitorability](../../concerns/i5-monitorability/): Determine how to monitor data and model outputs for drift or change.
- [I6 — Telemetry](../../concerns/i6-telemetry/): Identify the system usage data that needs to be collected.

## Automate End-to-End ML workflow

Plan an automated workflow from data preparation through deployment and monitoring.

Recommended stakeholders: Data Scientist (DS); Software/ML Engineer (SE).

- [I7 — Reproducibility](../../concerns/i7-reproducibility/): Determine the need to repeat ML processes and obtain the same or similar results.
- [I8 — Maintainability](../../concerns/i8-maintainability/): Determine how the system must support changes to performance or operating conditions.

## Integrate the ML model

Incorporate the trained model into the software system that will consume its predictions.

Recommended stakeholders: Software/ML Engineer (SE).

- [I9 — Integration](../../concerns/i9-integration/): Specify how the model integrates with the rest of the system's functionality.
- [I10 — Hybrid decision intelligence](../../concerns/i10-hybrid-decision-intelligence/): Describe how model outputs combine with rules or heuristics to support decisions.

## Evaluate the financial cost involved with infrastructure

Assess expenses for the resources, hardware, software, and services that support the project.

Recommended stakeholders: Business Owner (BO); Software/ML Engineer (SE).

- [I11 — Cost](../../concerns/i11-cost/): Assess the financial cost of inference and supporting infrastructure.

## Source notes

The introductory paragraph and task descriptions are editorial paraphrases of the article, section 3.4 and [Table 3, p. 7](../../1-s2.0-S0164121224000980-main.pdf#page=7). Concern names follow [Table 8, p. 9](../../1-s2.0-S0164121224000980-main.pdf#page=9); task–concern and task–stakeholder assignments come from [Figure 2, p. 11](../../1-s2.0-S0164121224000980-main.pdf#page=11).

The example text on p. 14 says seven infrastructure concerns have relationships; Figure 2 lists references under six (I1–I6). The task label “Transport data to the model” follows Table 3; the diagram adds “ML”.

Requirements Engineers facilitate the discussion but have no separate task assignments in Figure 2. Complete elicitation questions and relationship tables are unavailable in the local material; see [sources, differences, and coverage](../../SOURCES.md).

[All concerns](../../concerns/) · [PerSpecML overview](../../README.md).
