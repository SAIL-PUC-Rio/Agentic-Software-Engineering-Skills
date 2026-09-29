# Review mode

Input: an existing `.feature` file or Gherkin block, optionally with a requirement source. Output: findings grouped by attribute **and** a revised Gherkin block. Never return findings alone.

## Audience

Infer the audience before judging and state it in the output. Signals for **developer-facing**: the vocabulary is the component's own (inputs, outputs, states, collaborators, error kinds), no end-user actor appears, and a parent scenario or story ID (`BS-###`, `DS-###`, `MS-###`, `AS-###`) is referenced. Otherwise **customer-facing** (business vocabulary, people or external systems as actors). If mixed or unclear, choose the better fit and say why in the audience line.

The gate is identical for both. For developer-facing input, load [developer-facing.md](developer-facing.md) and read Q1-Q12 through its table: the component's interface vocabulary and the component as actor are legitimate. Q9-Q12 still fire on implementation mechanics: private classes and methods, internal data structures, call order, storage, and transport or UI details. Never "fix" a developer-facing scenario by rewriting it into business or end-user language or by inventing an end-user actor; fixes stay in the component's vocabulary.

## Procedure

1. **Parse** into feature, scenario, and step units (Background steps and Outline rows belong to their scenarios). Note the Scenario titles.
2. **Feature level.** Ask Q1 and Q2 ([quality-model.md](quality-model.md)) once. Q2 is judged against the source only. A missing scenario whose outcome the source did not decide goes to `### Unresolved behavior`, not into the revision.
3. **Across scenarios.** Compare every pair for duplication (Q5): same Given/When with the same or a subset Then is a duplicate. Then note missing coverage for Q2.
4. **Scenario level.** Ask Q3-Q8 for each scenario.
5. **Step level.** Ask Q9-Q12 for each step.
6. **Group findings by attribute** (all 8, in the order of the quality model). Each is `PASS`, `REVISE`, or `NOT_APPLICABLE`. Every `REVISE` names the scenario or step, cites the question number(s), and states the fix. A `PASS` needs no finding.
7. **Revise.** Write the full revised Gherkin block resolving every `REVISE`. Then re-run steps 2-5 on it and confirm no `REVISE` remains (except items that can only be settled by the source).
8. **Preserve semantics.** The revision keeps every behavior the original states. Change behavior (add an outcome, add a scenario, alter a condition) only when a cited source line supports it; put the citation in a comment or the finding. Otherwise list the gap under `### Unresolved behavior` and leave it out of the revision. A vague step whose meaning cannot be recovered from the file or source is also Unresolved, not a guess.

Fixes (in the audience's own vocabulary; for developer-facing, never toward end-user language): remove removable steps, replace UI/transport mechanics with the behavior they express, split independent `When`s into separate scenarios, reorder to Given/When/Then, rename to the canonical term, merge or drop duplicates (say which), retitle to action + outcome.

If nothing is `REVISE`, say so and return the input unchanged as the revised block.

## Output shape

```markdown
## BDD Review

**Audience judged:** customer-facing | developer-facing (one clause of evidence)

### Findings

- **Singular - REVISE (Q6, Q7):** `Scenario: Update profile` has two independent `When` actions; split.
- **Ubiquitous - REVISE (Q9):** `user` and `customer` name the same actor; use the canonical term.
- **Essential - PASS**

### Revised scenario

```gherkin
...
```

### Unresolved behavior
(omit if empty)
```
