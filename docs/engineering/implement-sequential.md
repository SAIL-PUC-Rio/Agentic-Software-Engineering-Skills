## What it does

`implement-sequential` builds every subissue under a spec issue, one at a time: a fresh subagent per subissue, an [evidence](https://aihero.dev/skills-evidence) pack closed out before the next one starts. It exists because `implement` itself is user-invoked and can't be called by another agent — not even by a subagent this skill spawns on your explicit instruction — so it never tries to. Instead it briefs each subagent with `implement`'s own steps directly, and drives `evidence` itself once the subagent's commit lands.

## When to reach for it

You invoke this by typing `/implement-sequential` — the agent won't reach for it on its own, and no other skill can call it either.

Reach for it when you have a spec issue with several subissues and want them built one after another without babysitting each `/implement` call and `/clear` by hand. For a single ticket, or work that isn't split up yet, use [implement](https://aihero.dev/skills-implement) directly instead. For subissues with no dependency on each other, where you want them built at the same time rather than in order, use [implement-parallel](https://aihero.dev/skills-implement-parallel).

## Prerequisites

Needs a spec issue whose subissues declare blocking edges — the output of [to-tickets](https://aihero.dev/skills-to-tickets), or a `wayfinder` map. Without blocking edges to order by, there's no frontier to work.

## The frontier, one subissue at a time

The core idea is the same **frontier** [to-tickets](https://aihero.dev/skills-to-tickets) and `wayfinder` both use: a subissue is workable once every subissue blocking it is closed. This skill just walks that frontier itself instead of handing it to you to work by hand — spawn a subagent for the next open subissue, wait for its commit, publish its evidence pack, discard the subagent, repeat.

Each subagent only ever sees one subissue. That's deliberate: the previous subissue's context is disposable the moment its commit and evidence pack exist, which is the same discipline `implement`'s own docs describe for a human clearing context between tickets — this skill just automates the clearing.

Each subagent's brief carries the subissue's cited story and BS IDs, the scenario Gherkin with any audience line, and the matching Testing Decisions seams, so a `BS-###` scenario is driven red-green at its seam (a developer-facing one at its unit or module seam). A subissue with no BS IDs is driven from its acceptance criteria.

## Common questions

**Why not just have the subagent call `/implement` itself?**

Because it's refused. `implement` carries `disable-model-invocation: true`, which — per this repo's own invocation rules — means no agent can reach it, regardless of who told that agent to try. That includes a subagent spawned by a human-typed `/implement-sequential`. The workaround is to hand the subagent `implement`'s steps directly rather than the skill itself.

**Why not run this in parallel instead?**

Nothing here stops you from wanting that, but sequential and parallel are different tools for different situations. Subissues with real dependencies between them still need to happen in order regardless of how they're dispatched. Where a whole batch of subissues has no dependency on each other, [implement-parallel](https://aihero.dev/skills-implement-parallel) runs them concurrently in isolated worktrees instead of one at a time.

## It's working if

- Each subissue gets its own subagent, briefed on nothing but that subissue.
- An evidence pack exists for every completed subissue before the next one's subagent spawns.
- Subissues land in blocker-respecting order, not issue-number order.
- Nothing about a finished subagent's context shows up influencing the next one.

## Where it fits

A **chain step** that sits downstream of [to-tickets](https://aihero.dev/skills-to-tickets) or a `wayfinder` map, and stands in for hand-driving [implement](https://aihero.dev/skills-implement) per ticket. Its sibling is [implement-parallel](https://aihero.dev/skills-implement-parallel), for the case where subissues don't depend on each other; its downstream neighbour is [evidence](https://aihero.dev/skills-evidence), which it drives itself after every subissue. [ask-matt](https://aihero.dev/skills-ask-matt) is the router over the whole set.
