# Quality model

Source: Oliveira, Marczak & Moralles (2019), "How to Evaluate BDD Scenarios' Quality?" (SBES 2019). The 12-question checklist below is the source of truth, copied from `docs/bdd/oliveira_guidelines.md`. The attribute mapping after it is an operational aid.

## The eight attributes

| Attribute | Means |
|---|---|
| Essential | Only what is needed to understand the behavior; nothing removable. |
| Focused | Says what the system does (declarative), not how it is done. |
| Singular | One behavioral intention per scenario; the title names it. |
| Clear | One reasonable interpretation; not vague or misleading. |
| Complete | Nothing needed is missing, in a scenario or across the feature. |
| Unique | Each scenario and the feature itself is distinct in purpose and value. |
| Ubiquitous | Uses the project's business terms and correct actors. |
| Integrous | Respects Gherkin keyword meaning and natural order. |

## The 12-question checklist

| ID | Question | Scope | Attribute |
|---:|---|---|---|
| 1 | Can the feature file business value or outcome be identified by its description? | Feature | Unique |
| 2 | Does the feature file has any missing scenarios? | Feature | Complete |
| 3 | Does the scenario carry all the information needed to understand it? | Scenario | Complete |
| 4 | Does the scenario has steps that can be removed without affecting its understanding? | Scenario | Essential |
| 5 | How different each scenario is from the others? | Scenario | Unique |
| 6 | Can the scenario single action be identified on its title and match what the scenario is doing? | Scenario | Singular |
| 7 | Can the scenario outcome or verifications be identified on its title and match what the scenario is doing? | Scenario | Singular |
| 8 | Does the scenario respect Gherkin keywords meaning and its natural order? | Scenario | Integrous |
| 9 | Does the step correctly employs business terms, including a proper actor? | Step | Ubiquitous |
| 10 | Does the step has details that can be removed without affecting its meaning? | Step | Essential |
| 11 | Does the step express "what" it is doing by being written in a declarative way? | Step | Focused |
| 12 | Does the step allow different interpretations by being vague or misleading? | Step | Clear |

Apply Feature questions (1-2) once, Scenario questions (3-8) to every scenario, Step questions (9-12) to every step. Question 12 is inverted: a step that allows different interpretations is a failure. Question 2 can only be judged against the source; a "missing" scenario the source never decided is Unresolved behavior, not a gap to fill.

## Attribute to question mapping

| Attribute | Questions | Extra check |
|---|---|---|
| Essential | 4, 10 | |
| Focused | 11 | |
| Singular | 6, 7 | Intention check: can the scenario be summarized as one action and one outcome? Two independent `When`s fail. |
| Clear | 12 | |
| Complete | 2, 3 | |
| Unique | 1, 5 | |
| Ubiquitous | 9 | Terms match `CONTEXT.md`; one term per concept. For developer-facing specs, "domain entity" may be a module type and the actor a component. |
| Integrous | 8 | |

The questions apply unchanged to developer-facing specs; how each reads is in [developer-facing.md](developer-facing.md).

## Statuses

Each attribute gets one status, with a finding when it is `REVISE`. No numeric scoring.

- `PASS` - every applicable question passes.
- `REVISE` - at least one question fails; name the scenario/step and the fix.
- `NOT_APPLICABLE` - the attribute cannot apply (e.g. Unique with a single scenario, question 5); say why.

```markdown
| Attribute | Questions | Result | Finding |
|---|---|---|---|
| Singular | 6, 7 | REVISE | "Update profile" has two independent When actions; split. |
```
