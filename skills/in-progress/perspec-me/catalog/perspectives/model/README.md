# M — Model

The Model perspective examines the choices and constraints involved in creating a usable ML model. It covers algorithm selection, tuning, inputs and outputs, training, validation, and deployment. Its quality concerns also address explainability, scalability, fairness, security, and privacy, so model assessment extends beyond a predictive score.

5 tasks · 14 concerns · M1–M14.

## How to use this perspective

Work through the tasks with the recommended stakeholders, open each concern for context, and inspect its available definition, questions, and relationships before deciding applicability. The task groups organize specification discussions; they do not prescribe a separate implementation schedule.

## Select and configure the ML model

Shortlist suitable algorithms and investigate hyperparameter configurations.

Recommended stakeholders: Data Scientist (DS).

- [M1 — Algorithm & model selection](../../concerns/m1-algorithm-model-selection/): Identify candidate algorithms and models that fit the problem and its constraints.
- [M2 — Algorithm tuning](../../concerns/m2-algorithm-tuning/): Determine the need to choose suitable hyperparameters for the learning algorithm.

## Train the ML model

Create a model that captures patterns in data and predicts unseen examples.

Recommended stakeholders: Data Scientist (DS).

- [M3 — Input & Output](../../concerns/m3-input-output/): Describe the model's expected input features and output.
- [M4 — Learning time](../../concerns/m4-learning-time/): Set an acceptable time for training the model.

## Validate the ML model

Check that the trained model meets the desired criteria.

Recommended stakeholders: Data Scientist (DS); Domain Expert (DE).

- [M5 — Performance metrics](../../concerns/m5-performance-metrics/): Choose metrics and measurable expectations for evaluating the model.
- [M6 — Baseline model](../../concerns/m6-baseline-model/): Decide whether a simple reference model is needed to contextualize results.

## Deploy the ML model

Make the trained model operational in a production environment.

Recommended stakeholders: Data Scientist (DS).

- [M7 — Inference time](../../concerns/m7-inference-time/): Set an acceptable time for model execution and prediction delivery.
- [M8 — Model size](../../concerns/m8-model-size/): Specify model storage size and complexity constraints.
- [M9 — Performance degradation](../../concerns/m9-performance-degradation/): Account for predictive performance decreasing over time.
- [M10 — Versioning](../../concerns/m10-versioning/): Specify library versions and address dependency compatibility.

## Evaluate other quality characteristics

Assess quality characteristics that affect real-world suitability beyond predictive accuracy.

Recommended stakeholders: Data Scientist (DS); Software/ML Engineer (SE).

- [M11 — Interpretability & Explainability](../../concerns/m11-interpretability-explainability/): Determine the need to understand and explain the reasons for model inferences.
- [M12 — Scalability](../../concerns/m12-scalability/): Determine how the model should perform as data volume and problem complexity grow.
- [M13 — Bias & Fairness](../../concerns/m13-bias-fairness/): Examine the model's treatment of different groups of people or entities.
- [M14 — Security & Privacy](../../concerns/m14-security-privacy/): Determine how the model should protect sensitive data and prevent unauthorized access.

## Source notes

The introductory paragraph and task descriptions are editorial paraphrases of the article, section 3.4 and [Table 4, p. 7](../../1-s2.0-S0164121224000980-main.pdf#page=7). Concern names follow [Table 9, p. 9](../../1-s2.0-S0164121224000980-main.pdf#page=9); task–concern and task–stakeholder assignments come from [Figure 2, p. 11](../../1-s2.0-S0164121224000980-main.pdf#page=11).

The diagram and definition table use different names for M2, M3, M8, and M11. The reproduced template also uses different task headings for the M1 and M3 questions. Each affected concern records these differences.

Requirements Engineers facilitate the discussion but have no separate task assignments in Figure 2. Complete elicitation questions and relationship tables are unavailable in the local material; see [sources, differences, and coverage](../../SOURCES.md).

[All concerns](../../concerns/) · [PerSpecML overview](../../README.md).
