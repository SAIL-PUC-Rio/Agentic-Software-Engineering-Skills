# Concerns

Each entry introduces one concern in a sentence; open its folder for a paragraph of context and links to the available detail. Names and IDs follow Tables 6–10 of the final article.

## O — System Objectives

- [O1 — Context](o1-context/): Describe the circumstances in which the ML-enabled system will operate.
- [O2 — Need](o2-need/): Identify the requirement, desire, or gap the system must address.
- [O3 — ML functionality](o3-ml-functionality/): Define the learning problem and the outcome expected from the ML model.
- [O4 — Profit hypothesis](o4-profit-hypothesis/): Explain how the system's outcomes are expected to produce organizational gains.
- [O5 — Organizational goals](o5-organizational-goals/): Set measurable benefits that ML should bring to the organization.
- [O6 — System goals](o6-system-goals/): Define the behavior and quality the overall system should achieve with ML support.
- [O7 — User goals](o7-user-goals/): State what users want to achieve by using ML.
- [O8 — Model goals](o8-model-goals/): Set the metrics and acceptable values the model should achieve.
- [O9 — Leading indicators](o9-leading-indicators/): Identify measures that correlate with future business success.
- [O10 — ML trade-off](o10-ml-trade-off/): Make the balance between competing ML expectations explicit.

[Tasks and stakeholders for this perspective](../perspectives/system-objectives/).

## U — User Experience

- [U1 — Value](u1-value/): Identify the value users perceive in the model's predictions.
- [U2 — Forcefulness](u2-forcefulness/): Decide how strongly predictions direct users' actions.
- [U3 — Frequency](u3-frequency/): Specify how often the system interacts with users.
- [U4 — Visualization](u4-visualization/): Define how interfaces present model outputs so users can understand and use them.
- [U5 — Learning feedback](u5-learning-feedback/): Specify user interactions that provide new data for learning.
- [U6 — Acceptance](u6-acceptance/): Examine how well the model makes decisions and how it reaches them.
- [U7 — Accountability](u7-accountability/): Identify who is responsible for unexpected model results.
- [U8 — Cost](u8-cost/): Describe the impact on users of an incorrect prediction.
- [U9 — User education & Training](u9-user-education-training/): Identify the education users need to understand system limitations and interpret outputs.

[Tasks and stakeholders for this perspective](../perspectives/user-experience/).

## I — Infrastructure

- [I1 — Data streaming](i1-data-streaming/): Specify how data travels to the model, including real-time or batch delivery.
- [I2 — Model serving](i2-model-serving/): Choose how the model will be executed and made available for consumption.
- [I3 — Incremental learning](i3-incremental-learning/): Determine whether the system must keep learning from new data.
- [I4 — Storage](i4-storage/): Specify where ML artifacts will be stored.
- [I5 — Monitorability](i5-monitorability/): Determine how to monitor data and model outputs for drift or change.
- [I6 — Telemetry](i6-telemetry/): Identify the system usage data that needs to be collected.
- [I7 — Reproducibility](i7-reproducibility/): Determine the need to repeat ML processes and obtain the same or similar results.
- [I8 — Maintainability](i8-maintainability/): Determine how the system must support changes to performance or operating conditions.
- [I9 — Integration](i9-integration/): Specify how the model integrates with the rest of the system's functionality.
- [I10 — Hybrid decision intelligence](i10-hybrid-decision-intelligence/): Describe how model outputs combine with rules or heuristics to support decisions.
- [I11 — Cost](i11-cost/): Assess the financial cost of inference and supporting infrastructure.

[Tasks and stakeholders for this perspective](../perspectives/infrastructure/).

## M — Model

- [M1 — Algorithm & model selection](m1-algorithm-model-selection/): Identify candidate algorithms and models that fit the problem and its constraints.
- [M2 — Algorithm tuning](m2-algorithm-tuning/): Determine the need to choose suitable hyperparameters for the learning algorithm.
- [M3 — Input & Output](m3-input-output/): Describe the model's expected input features and output.
- [M4 — Learning time](m4-learning-time/): Set an acceptable time for training the model.
- [M5 — Performance metrics](m5-performance-metrics/): Choose metrics and measurable expectations for evaluating the model.
- [M6 — Baseline model](m6-baseline-model/): Decide whether a simple reference model is needed to contextualize results.
- [M7 — Inference time](m7-inference-time/): Set an acceptable time for model execution and prediction delivery.
- [M8 — Model size](m8-model-size/): Specify model storage size and complexity constraints.
- [M9 — Performance degradation](m9-performance-degradation/): Account for predictive performance decreasing over time.
- [M10 — Versioning](m10-versioning/): Specify library versions and address dependency compatibility.
- [M11 — Interpretability & Explainability](m11-interpretability-explainability/): Determine the need to understand and explain the reasons for model inferences.
- [M12 — Scalability](m12-scalability/): Determine how the model should perform as data volume and problem complexity grow.
- [M13 — Bias & Fairness](m13-bias-fairness/): Examine the model's treatment of different groups of people or entities.
- [M14 — Security & Privacy](m14-security-privacy/): Determine how the model should protect sensitive data and prevent unauthorized access.

[Tasks and stakeholders for this perspective](../perspectives/model/).

## D — Data

- [D1 — Source](d1-source/): Identify where the data will be obtained.
- [D2 — Timeliness](d2-timeliness/): Specify the delay between expected and actual data availability.
- [D3 — Data selection](d3-data-selection/): Determine which data types and samples should be collected.
- [D4 — Data dictionary](d4-data-dictionary/): Describe data elements through their names, definitions, and attributes.
- [D5 — Quantity](d5-quantity/): Specify the expected amount of data for the problem and algorithm.
- [D6 — Accuracy](d6-accuracy/): Determine the need for correct data.
- [D7 — Completeness](d7-completeness/): Determine whether data covers the situations in which the model will operate.
- [D8 — Credibility](d8-credibility/): Determine the need for true data that users find believable and understandable.
- [D9 — Real usage](d9-real-usage/): Determine whether data represents the real problem the model will face.
- [D10 — Bias](d10-bias/): Determine the need for fair samples and representative data distributions.
- [D11 — Consistency](d11-consistency/): Determine whether data is consistent within its specific context.
- [D12 — Ethics](d12-ethics/): Identify potential adverse societal effects associated with the data.
- [D13 — Anonymization](d13-anonymization/): Determine how to protect individual identities while keeping data useful for ML.
- [D14 — Data operations & Modeling](d14-data-operations-modeling/): Specify the operations that convert data into the model's required representation.
- [D15 — Data distribution](d15-data-distribution/): Specify data distributions and the split into training, validation, and test sets.
- [D16 — Golden dataset](d16-golden-dataset/): Determine the need for a domain-approved reference dataset representing the problem.

[Tasks and stakeholders for this perspective](../perspectives/data/).

The [source register](../SOURCES.md) records the D9–D11 naming conflict, other differences, and missing template and relationship-table coverage. The one-sentence descriptions are editorial summaries, not additional official definitions.

[PerSpecML overview](../README.md).
