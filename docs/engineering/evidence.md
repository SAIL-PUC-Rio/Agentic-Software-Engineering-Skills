Quickstart:

```bash
npx skills add mattpocock/skills --skill=evidence
```

```bash
npx skills update evidence
```

[Source](https://github.com/mattpocock/skills/tree/main/skills/engineering/evidence)

## What it does

`evidence` turns a finished piece of work into a factual, auditable pack — a scope-to-proof map tying each claim about what got built to the command, exit code, or diff that actually proves it — then publishes that pack to the task's issue tracker. It never treats "implementation completed" as evidence on its own, and it never rounds a skipped or inconclusive check up to a pass.

## When to reach for it

Type `/evidence`, or the agent reaches for it automatically when a task fits — most often because [implement](https://aihero.dev/skills-implement) just committed and runs it as a mandatory closeout. Reach for it directly when you want to regenerate or inspect the evidence for a commit that's already landed, without redoing the implementation.

## Prerequisites

The issue tracker `evidence` publishes to comes from [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) — without `docs/agents/issue-tracker.md`, it can't tell a GitHub repo from a local `.scratch/` convention, and falls back to writing the pack locally with publication marked blocked rather than guessing.

## Claims, not confidence

The unit `evidence` works in is the **claim** — a single assertion (an acceptance criterion, an invariant) given a stable ID (`CLM-001`) and a status from a fixed vocabulary: `PASS`, `FAIL`, `PARTIAL`, `NOT_RUN`, `NOT_APPLICABLE`, `UNKNOWN`. A claim only reaches `PASS` because a specific, cited command or diff proved it — never because the surrounding narrative sounds finished. Negative evidence — a failing test, a check that didn't run, a credential that wasn't available — stays in the pack exactly as visibly as a pass.

## Behavioral Specifications

When the originating spec has `## Behavioral Specifications`, each in-scope scenario becomes its own claim, whatever its audience, citing its `BS-###` and story IDs, backed by the run of the test at the agreed seam. The pack also records the `bdd-scenarios` review of those scenarios as an evidence artifact, so it shows whether the specification met its quality gate as well as whether the code met the specification. A scenario with no verifying test shows as `NOT_RUN` or `NOT_APPLICABLE`, never `PASS`. `bdd-scenarios` is a beta skill; where it isn't installed, the review artifact is recorded as `NOT_RUN`. A spec without Behavioral Specifications gets the same pack as before.

## It's working if

- Every row in the scope-to-proof map cites a real evidence ID, not just a claim.
- A `NOT_RUN` or `UNKNOWN` claim is still visible in the executive result, not smoothed over.
- It reuses `implement`'s own command output where it can, rather than rerunning the whole suite a second time to manufacture evidence.
- For a spec with Behavioral Specifications, every in-scope `BS-###` has its own claim row, and an untested one reads `NOT_RUN` or `NOT_APPLICABLE`.
- Regenerating the pack for the same commit updates the existing published copy instead of posting a duplicate.

## Where it fits

`evidence` is `implement`'s internal closeout step, not a chain link you invoke yourself in the normal flow:

```txt
grill-with-docs → to-spec → to-tickets → implement (→ evidence) → code-review
```

Its closest neighbour is [implement](https://aihero.dev/skills-implement), which drives it automatically right after committing; [code-review](https://aihero.dev/skills-code-review) is the sibling closeout concern that stayed manual — one publishes what was verified, the other judges whether the diff was built and specced right. When you're unsure which skill or flow fits, [ask-matt](https://aihero.dev/skills-ask-matt) routes you.
