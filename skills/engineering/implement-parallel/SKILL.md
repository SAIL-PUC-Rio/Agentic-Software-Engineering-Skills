---
name: implement-parallel
description: "Spawn a subagent per independent subissue of a spec issue to implement them concurrently, then merge the wave and verify the suite before opening the next one."
disable-model-invocation: true
---

Work a spec issue's subissues in waves: every subissue with no open blocker runs at once, each isolated in its own worktree, then the wave is merged and proven green before the next wave opens up.

## Resolve the subissues and the frontier

Read the spec issue's subissues and blocking edges the same way `implement-sequential` does, per `docs/agents/issue-tracker.md`. The **frontier** is every open subissue with no open blocker — the same query `wayfinder` runs.

## Work one wave

While the frontier is non-empty:

1. **Spawn one subagent per frontier subissue, in parallel** — a single message, one Agent-tool call per subissue, each with `isolation: "worktree"`. This isn't optional: parallel `implement`-style sessions sharing one checkout corrupt each other's index, HEAD, and even stash, and a worktree per subagent is what actually fixes it (stash itself still isn't isolated across worktrees, so brief each subagent to commit its own work rather than stash it). Brief each subagent the way `implement-sequential` does — `implement`'s own steps inlined (TDD at pre-agreed seams, with each cited `BS-###` scenario driven red-green at the seam the spec's Testing Decisions assigns it — pass the scenario Gherkin and those Testing Decisions lines in the brief; a subissue with no BS IDs is driven from its acceptance criteria; `CODING_STANDARDS.md`/ADRs, typecheck and test as it goes, commit), never a Skill-tool call to "implement" itself, which stays refused for any non-literal-human invocation per `.agents/invocation.md`. Scope each subagent to exactly one subissue.
2. **Wait for the whole wave to finish committing.**
3. **Merge each subissue back through the subagent that wrote it, one at a time — not batched onto yourself at the end.** Resume that subagent (don't discard it yet) and have it merge its own worktree branch into the branch this wave started from. If the merge conflicts, that subagent drives `resolving-merge-conflicts` itself — it still holds the intent behind its own changes, and this repo's own experience with parallel worktrees is that the session which wrote a change merges it back better than one agent trying to reconstruct everyone's intent from scratch at the end.
4. **Close out each subissue.** Once its branch is merged clean, call the Skill tool with "evidence" for it, then discard that subagent — its work is on the shared branch now, nothing more carries forward.
5. **Prove the wave green.** Once every subissue in the wave is merged, run the full test suite once — not per-branch, since a wave's branches can conflict in ways no single branch's tests would catch. A red suite blocks the next wave: fix it before opening one.
6. **Recompute the frontier** — subissues that were blocked only by this wave are now open — and repeat from step 1.

## Finish

Once no subissue remains, report which ones ran in which wave, link each evidence pack, and name anything left blocked or any subagent that failed to finish.
