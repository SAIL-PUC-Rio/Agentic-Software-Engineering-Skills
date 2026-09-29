## What it does

`implement-parallel` builds every subissue under a spec issue in waves: every subissue with no open blocker runs at once, each isolated in its own git worktree, then the wave is merged and proven green with a full test run before the next wave opens up. It exists for the same reason [implement-sequential](implement-sequential.md) does — `implement` can't be invoked by another agent — but scales it across a whole unblocked batch instead of one subissue at a time.

The defining constraint is the worktree: parallel `implement`-style sessions sharing one checkout corrupt each other's git index, HEAD, and stash, so every subagent in a wave gets its own isolated worktree, and merge-conflict resolution is handed back to the subagent that wrote the change rather than batched onto one agent at the end.

## When to reach for it

You invoke this by typing `/implement-parallel` — the agent won't reach for it on its own, and no other skill can call it either.

Reach for it when a spec issue's subissues have no dependency on each other and you want them built at the same time. Where subissues genuinely depend on each other, use [implement-sequential](implement-sequential.md) instead — running dependent work concurrently just means one subagent starts before its input exists.

## Prerequisites

Needs a spec issue whose subissues declare blocking edges — the output of [to-tickets](to-tickets.md), or a `wayfinder` map — so the skill can compute a frontier. It also needs `git worktree` to work in the repo you're running it in.

## Waves, not a single fan-out

A **wave** is every subissue on the frontier at once — the set with no open blocker. The skill doesn't just fan every subissue out in one shot: subissues gated by ones still in flight have to wait for the next wave, computed fresh once the current one merges and its tests go green.

Inside a wave: subagents run in parallel, each in its own worktree. Merging back isn't batched onto the orchestrating agent — each subagent merges its own branch, and if that merge conflicts, that same subagent runs [resolving-merge-conflicts](resolving-merge-conflicts.md) itself, since it's the one that still holds the intent behind its own diff. Only once a wave is fully merged does the full test suite run — once, not per branch, because a wave's branches can conflict in ways no single branch's tests would catch.

Each subagent's brief carries its subissue's cited story and BS IDs, the scenario Gherkin with any audience line, and the matching Testing Decisions seams, so a `BS-###` scenario is driven red-green at its seam (a developer-facing one at its unit or module seam). A regression scenario is a constraint that must pass before and after, with no pre-existing test edited. If `bdd-scenarios` is installed, the brief also points each subagent at its during-implementation reference: derive the component scenario from the parent BS, cite it, add no behavior, and ask about any case the BS never settles. A subissue with no BS IDs is driven from its acceptance criteria.

## Common questions

**Why does each subagent merge its own branch instead of the orchestrator doing it once at the end?**

Because this repo has already seen the failure mode: batching every sibling's conflicts onto one agent at the end throws away the context each session had about its own change, and a session merging back its own ticket does it better than one trying to reconstruct everyone's intent afterward. The orchestrating agent still drives the overall sequence and runs the final test suite — it just doesn't resolve conflicts blind.

**Why worktrees and not just running several implementers in the same checkout?**

Because that's documented elsewhere in this repo as actively unsafe, not just unsupported: sessions sharing one checkout have corrupted each other's commits, dropped stashes, and landed commits on the wrong branch. Worktrees fix the index/HEAD collision; stash still isn't isolated across worktrees, which is why subagents are briefed to commit rather than stash.

**What if a wave leaves the suite red?**

The next wave doesn't open. Fixing the suite blocks progress on purpose — a wave's merges are exactly the place a change that looked fine on its own branch can break another.

## It's working if

- Every subagent in a wave runs in its own worktree, visible as a separate branch.
- A subissue's own subagent is the one that merges its branch back, not the orchestrator.
- The full suite runs once per wave, after every branch in that wave is merged — not once per branch.
- A later wave never starts while an earlier one's suite is red.
- An evidence pack exists for every merged subissue.

## Where it fits

A **chain step**, sibling to [implement-sequential](implement-sequential.md), sitting downstream of [to-tickets](to-tickets.md) or a `wayfinder` map. It leans on [resolving-merge-conflicts](resolving-merge-conflicts.md) for the merges and drives [evidence](evidence.md) itself per subissue. [ask-matt](ask-matt.md) is the router over the whole set.
