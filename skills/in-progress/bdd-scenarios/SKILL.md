---
name: bdd-scenarios
description: Construct Gherkin Feature files from an already-agreed requirement or story and revise them through a scenario quality gate. Use when the user wants BDD scenarios, Gherkin, Given/When/Then, or executable acceptance criteria written from decided behavior.
---

# BDD Scenarios

The executable-specification counterpart of `tdd`: `tdd` turns behavior into tests, this turns an agreed requirement into Gherkin that names the behavior before any test exists. Scenarios are specifications of **known** behavior, for one of two audiences (below). They are never a way to decide behavior nobody decided.

## When it applies

- A requirement, story, or spec already states observable behavior and the user wants it as `Feature`/`Scenario`.
- Not for a pure refactor with **no** behavior change: nothing to specify. Say so and stop.
- Not a requirements interview. If the source is silent, report it (step 6), do not ask-and-invent.

Read `CONTEXT.md` (if it exists) so actors and entities use the project's glossary, and respect ADRs in the area.

## Audience

- **Customer-facing**: the behavior is visible to an end user or business person. Business-domain vocabulary from `CONTEXT.md`, actors are people or external systems.
- **Developer-facing**: the behavior of an internal component (module, function, pipeline stage, model, agent) observable at **its own interface**. Written for developers, in the component's vocabulary (inputs, outputs, states, collaborators), still declarative. No fake end-user actor. The source must still state the behavior; never specify private structure.

Infer the audience from the source (Data / Model / Agent stories are usually developer-facing). When developer-facing, load [references/developer-facing.md](references/developer-facing.md). The gate below is identical for both.

## Modes

Inferred from the task, not a flag. Given source behavior and no Gherkin, **construct**. Given existing Gherkin (a `.feature` file or block) to check, improve, or critique, **review**. If both, construct then review.

## Construct workflow

1. **Identify the observable behavior.** What an actor can see or verify from outside, per the source. Quote or cite the source line for each behavior.
2. **Identify actors and domain entities**, using the glossary terms verbatim. Do not coin synonyms.
3. **Draft** `Feature` / `Scenario` / `Given` / `When` / `Then`. One behavioral intention per scenario; title states the action and outcome; steps say what, not how. Load [references/gherkin-guidelines.md](references/gherkin-guidelines.md) before drafting.
4. **Run the quality gate.** Load [references/quality-model.md](references/quality-model.md) and check the feature, every scenario, and every step against all 12 questions. Each attribute ends as `PASS`, `REVISE`, or `NOT_APPLICABLE`. No numeric scores.
5. **Revise** every `REVISE` finding, then re-run the gate on what changed. Do not change meaning unless the source supports it.
6. **Report unresolved behavior.** Where the source never decided an outcome, condition, or actor, do not write a guessed `Then`. List it under `### Unresolved behavior`, stating what is missing and which scenario it blocks. Leave that scenario out or stub it as a comment.
7. **Return** the Gherkin, then the `Unresolved behavior` list (omit if empty), then a one-line gate result per attribute.

## Review workflow

Load [references/review-mode.md](references/review-mode.md). It parses the Gherkin into feature/scenario/step units, applies the same 12-question gate, and returns findings grouped by attribute (`PASS`/`REVISE`/`NOT_APPLICABLE`, citing question numbers) plus a **revised Gherkin block**. Always propose the revision, never only a list of violations. The revision keeps the original semantics; change behavior only where a cited source supports it, otherwise list it under `### Unresolved behavior`.

## Examples

[examples/good.feature](examples/good.feature) passes the gate. [examples/bad.feature](examples/bad.feature) violates several named attributes, each annotated. [examples/bad.review.md](examples/bad.review.md) and [examples/good.review.md](examples/good.review.md) record the review-mode output for each. The developer-facing pair is `examples/developer-good.feature`, `examples/developer-bad.feature` and their `.review.md` records. Read them to calibrate; do not copy their domain.
