# Story types

How `/to-spec` classifies already-agreed work into typed Stories. This file only sorts and shapes what the conversation already decided. It never adds requirements, metrics, or thresholds.

## Selection rules

Classify each requirement or intent on its own, in this order. Take the first branch that fits.

1. **Agent Story** — the work centres on an agentic system around a foundation model (FM): goal-directed behavior, tool use, skills, memory/context, planning, workflows, guardrails, human approval, orchestration, end-to-end agent evaluation.
2. **Model Story** — the work centres on a learned model as the development object: feature processing, training, validation, model selection, fine-tuning, model performance, deployment/versioning of the model.
3. **Data Story** — the work is primarily acquiring, preparing, cleaning, transforming, storing, or managing data or context: datasets, retrieval corpora, knowledge sources, curated evaluation sets.
4. **User Story** — the work is actor-visible: an actor interacting with the system, a user-visible capability, a business workflow, externally observable software behavior.
5. **None of the above** — architecture, refactoring, module boundaries, tooling, migration. Do not force it into a story. Record it under Implementation Decisions.

A single feature can produce several kinds, and one requirement can yield linked stories of different kinds (a User Story for the visible behavior, a Data Story for the data it needs). Emit only the kinds the work actually uses. Never emit an empty Data, Model, or Agent Story to fill out the template.

### Model vs Agent

Do not treat every AI requirement as a Model Story.

| The engineering work is about | Kind |
| --- | --- |
| Training, tuning, validating, or selecting a model; its accuracy or performance | Model Story |
| What an FM-based agent pursues, which tools/context it has, where humans approve, how the agent is evaluated | Agent Story |
| An FM that is consumed as-is (not trained or adapted) | Agent Story only. Do not add a Model Story because an FM is involved |
| An FM that is fine-tuned or adapted and the model itself is what is being built | Model Story (plus an Agent Story if an agent is also built around it) |

Data Stories stay relevant to agents. Their focus shifts from training sets to knowledge sources, retrieval corpora, contextual information, skills or reference artifacts, representative examples, and curated evaluation datasets.

### Tie-breakers

- A requirement with an actor but whose substance is model or agent behavior is not a User Story. Do not invent a human actor to satisfy the User Story grammar.
- If two kinds both fit, split into two linked stories rather than blending fields.
- If the conversation never settled which kind, or never settled the work at all, keep it as an Implementation Decision or an unresolved note. Do not guess.

## Story entry format

Every entry has a stable ID, an explicit **Type**, and a title. IDs count up per prefix within the spec: `US-001`, `US-002`, `DS-001`, and so on. They are stable, so never renumber after publishing.

| Kind | Prefix |
| --- | --- |
| User Story | `US-###` |
| Data Story | `DS-###` |
| Model Story | `MS-###` |
| Agent Story | `AS-###` |

## Core fields

Core fields come from the source papers. All are required. If the conversation did not settle one, write `Unresolved: <what is missing>` in its place. Never fabricate a value, a metric, a threshold, or a quantity.

### User Story

Actor, capability, value.

```markdown
### US-001 — <title>

**Type:** User Story

As a <actor>, I want <capability>, so that <value>.
```

The list of User Stories should be extensive and cover the user-facing behavior discussed.

### Data Story (Agile4MLS)

Goal, source, data type, approximate quantity.

```markdown
### DS-001 — <title>

**Type:** Data Story

- Goal:
- Source:
- Data type:
- Approximate quantity:
```

### Model Story (Agile4MLS)

Learning goal, learning type, data source, expected performance.

```markdown
### MS-001 — <title>

**Type:** Model Story

- Learning goal:
- Learning type:
- Data source:
- Expected performance:
```

### Agent Story (Romao et al.)

Agent goal, possible tasks, available artifacts, autonomy and human interference, expected performance.

```markdown
### AS-001 — <title>

**Type:** Agent Story

- **Agent goal:** <outcome the agent pursues>
- **Possible tasks:**
  - <task>
- **Available artifacts:**
  - **Tools:** <if applicable>
  - **Skills:** <if applicable>
  - **Context / knowledge:** <if applicable>
  - **Memory:** <if applicable>
- **Autonomy:** <what it may do alone, where a human must approve or intervene>
- **Expected performance:** <agreed threshold on the evaluation suite>
```

## Optional extension fields

These are this skill's extension, not part of the papers' definitions. Add one only when the conversation already stated it, and never mark the story unresolved for lacking one.

| Kind | Optional fields |
| --- | --- |
| Data Story | quality constraints, labeling, sampling, privacy, freshness |
| Model Story | metric, baseline, constraints, robustness, latency, deployment target |

## Backward compatibility

An existing spec with a `## User Stories` section reads as a `## Stories` section where every entry is `kind: user`. Do not rewrite historical specs.
