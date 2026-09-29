# Developer-facing scenarios

For internal components whose behavior is observable at their own interface: a module, function, pipeline stage, model, or agent. Basis: `docs/bdd/bdd_principles_unit_tests.md` (2.3.7). Same discipline, same gate; only the vocabulary source and the meaning of "observable" change.

## Choose the boundary

- The boundary is the component's **interface**: what a caller supplies (inputs, configuration, collaborator responses) and what it returns, emits, or leaves in a collaborator.
- Observable means visible there. Internal calls, private helpers, data structures, and ordering of internal steps are not.
- The source must still state the behavior. A pure refactor with no behavior change has no agreed behavior to specify; pin the existing behavior with [regression-mode.md](regression-mode.md) instead.
- Guardrail: describe **behavior**, not how the component is built. "How it is built" is the Focused / Essential failure (Q10, Q11).

## Vocabulary

- Actor is the component or its caller/collaborator (`the deduplication stage`, `the evaluator`), never an invented end user.
- Terms come from `CONTEXT.md` first, then the module's own public terms (input/output types, states, error kinds). One term per concept.
- Do not name private classes, methods, tables, or files unless they are the interface.

## Link to the parent acceptance scenario

Keep the outside-in trace: put the parent in a comment above the Feature, e.g. `# Parent: BS-004 (customer sees only distinct results)`, and cite the source line or story ID (`DS-###`, `MS-###`, `AS-###`) per behavior. Each developer-facing scenario should contribute to a parent outcome; one that contributes to none is a candidate for Q4/Q5.

## The 12 questions for a developer audience

| Q | Reads as |
|---|---|
| 1 | Does the description state the component's capability and why the feature or parent scenario needs it? |
| 2 | Missing scenarios are judged against the source's decided input classes/outcomes only; undecided ones go to Unresolved behavior. |
| 3 | The scenario states the inputs, state, and collaborator responses a developer needs; no hidden fixture. |
| 4 | No step removable without losing the input-to-output meaning. |
| 5 | Scenarios differ in input class or condition, not just in data (use Outline for data). |
| 6 | Title names the one stimulus (input, event, call). |
| 7 | Title names the one outcome at the interface (output, emitted event, rejection). |
| 8 | Given (component state or collaborator), When (the stimulus), Then (observable result). |
| 9 | Component vocabulary and the proper actor: the component or its caller, one term per concept. |
| 10 | No detail that does not change the behavior (thresholds not in the source, internal IDs). |
| 11 | Declarative: what the component does with inputs, not the algorithm, calls, or storage used. |
| 12 | Concrete expected values or classes from the source; no "valid", "correctly", "processed". |

Statuses and the attribute mapping are unchanged.
