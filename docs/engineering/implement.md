## What it does

`implement` builds work that has already been decided. You point it at a ticket, a spec, or the plan you just agreed in the conversation, and it writes the code, drives [tdd](../../skills/engineering/tdd/SKILL.md) at the seams, typechecks as it goes, commits to the current branch, and closes out with [evidence](evidence.md), which publishes a factual proof pack for the work to the issue tracker.

It never reopens the plan. There is no interview, no clarifying round, no proposal of a different approach. Whatever was settled upstream is the input, and the skill's whole job is to turn that into a commit. That is what separates it from typing "build this" at a fresh agent, which will happily redesign the work while it builds it. It also doesn't review its own work — that's a separate, deliberate step you reach for once implementation is done; publishing proof that the work is done is a different concern, and that one *is* automatic.

## When to reach for it

You invoke this by typing `/implement` — the agent won't reach for it on its own. It ships with `disable-model-invocation: true`, so no other skill can call it either. Wherever [ask-sail](../../skills/engineering/ask-sail/SKILL.md) or [to-tickets](to-tickets.md) says "then `/implement` per ticket", that is an instruction to you, not something the agent will do unprompted.

Where the work currently lives decides whether this is the right skill:

| The work is… | Reach for |
| --- | --- |
| A ticket on the tracker | `/implement #42`, one ticket per session, clearing context between tickets |
| A spec, not yet split up, and the build spans sessions | [to-tickets](to-tickets.md) first, then `/implement` per ticket |
| A spec, and the build is small | `/implement` directly against the spec |
| Only in the conversation you just had, and it's still small | `/implement` right there, in the same window |
| Not written down anywhere yet | [grill-with-docs](../../skills/engineering/grill-with-docs/SKILL.md), or [grill-me](../../skills/productivity/grill-me/SKILL.md) if there's no codebase |
| One concrete behaviour you want test-first, with no spec | [tdd](../../skills/engineering/tdd/SKILL.md) directly |
| Already built, and you want it checked | [code-review](code-review.md) directly |

The same-session case is worth naming because the skill's own first line doesn't cover it. `SKILL.md` says "the spec or tickets", which nudges the model to go hunting for a file that doesn't exist. If the plan lives only in the thread, say so when you invoke it.

## Prerequisites

`implement` commits to the branch you are on. It does not create one, and it does not ask. Check you are on the branch you want the work on before you start.

If the tickets came from [to-tickets](to-tickets.md), the tracker they live on was configured by [setup-sail-skills](../../skills/engineering/setup-sail-skills/SKILL.md). `evidence` reads the same configuration to know where to publish the proof pack at close-out.

## What one run does

A run is five beats, in order:

1. Read the ticket or spec and work out the seams.
2. Drive [tdd](../../skills/engineering/tdd/SKILL.md) at the pre-agreed seams, one red-green slice at a time.
3. Typecheck often, run single test files as it goes.
4. Run the full test suite once, at the end.
5. Commit to the current branch, then run [evidence](evidence.md) to close out.

One run covers one ticket. The tickets [to-tickets](to-tickets.md) produces are tracer-bullet vertical slices sized to fit a single fresh context window, so the intended rhythm is: clear context, implement one ticket, commit, clear again. Each ticket is self-contained, which is what makes the previous ticket's context disposable.

## Behavior scenarios

If the ticket or spec names `BS-###` scenarios, each one becomes a behavior to drive red-green through [tdd](../../skills/engineering/tdd/SKILL.md) at the seam the spec's Testing Decisions assigns to that ID; a developer-facing scenario is driven at its unit or module seam, not through the UI. The scenario says what to observe; the test at the seam is still yours to write. A `**Kind:** regression` scenario is a constraint rather than a feature: it passes before and after your change, and no pre-existing test is edited to make it pass. Unresolved behavior in the spec is not built from a guess. If `bdd-scenarios` (a beta skill outside the plugin) is installed, `implement` reads its during-implementation reference to derive a component scenario from the parent BS: it cites the `BS-###`, adds no behavior, and a case the BS never settles is raised as a question rather than written. Refactoring an existing component starts from its regression mode. It is never invoked by default, and nothing changes without it. Tickets and specs without BS IDs, including legacy `## User Stories` specs, run as before from the acceptance criteria. The same brief is passed to the subagents in [implement-sequential](implement-sequential.md) and [implement-parallel](implement-parallel.md).

## Pre-agreed seams

The idea the skill runs on is the **seam**: the public boundary you observe behaviour at, without reaching inside. Tests live at seams. Working at a seam agreed before any code is written is what keeps the tests durable, because the implementation underneath can be rewritten without the tests moving.

Around that core it keeps the loop tight — typecheck often, run single test files as it goes, run the whole suite once at the end — then commits to the current branch and hands off to [evidence](evidence.md), which publishes what actually got verified to the task's issue tracker.

The word "pre-agreed" is doing real work, and it is also the skill's weakest joint. Nothing inside `implement` agrees the seams. `tdd` is the skill that asks, and it refuses to write a test at an unconfirmed seam. So in practice the agreement happens either upstream in the spec, or in the first exchange of the run. If it happens nowhere, the precondition never fires and the run quietly becomes "just write the code". Naming the seams in the spec is what stops that.

## Common questions

**It finished, but my ticket is still open and the acceptance criteria are still unchecked.**

Correct, and expected. `implement` has no completion step. It ends at the commit and the [evidence](evidence.md) pack, and never touches the work item itself, confirmed on GitHub Issues and on the local markdown tracker, so it is not a tracker integration problem. It does not tick the `- [ ]` boxes on the originating issue. Close the ticket and reconcile the criteria yourself. This bites hardest on a dependency chain, because `to-tickets` defines the frontier as tickets whose blockers are all closed. If nothing gets closed, nothing ever becomes visibly unblocked.

**Can I point it at all my tickets at once, or run several in parallel?**

Not `implement` itself — one invocation, one ticket, and that hasn't changed. What changed is that batch dispatch across a ticket queue no longer means assembling it yourself: [implement-sequential](implement-sequential.md) runs a whole spec issue's subissues one after another, a fresh subagent per subissue; [implement-parallel](implement-parallel.md) runs every unblocked subissue of a wave concurrently. Neither gets there by calling `/implement` from another agent — that call is still refused, same as ever — they brief each subagent with `implement`'s own steps directly instead.

The reason `implement` itself stays single-ticket is the failure mode that made parallel dispatch dangerous in the first place: one field report describes a `git commit --amend` in one session landing on another session's commit, a stash vanishing from `refs/stash`, and commits landing on the wrong branch, all in a single afternoon across three issues, from sessions sharing one working directory, one index, and one HEAD. `implement-parallel` isolates every subagent in its own git worktree specifically because of this — worktrees fix the index/HEAD collision, though `refs/stash` still isn't isolated across them, which is why its subagents are briefed to commit rather than stash.

**Can it open a pull request instead of committing?**

Not built in. It commits straight to the current branch, which several people find too eager: the code lands before they have had a chance to verify it works. There is no configuration flag and no PR mode. People override it in the invocation ("commit to a branch and open a PR") or by editing their local copy of the skill.

**I want `code-review` to run as part of the same pass. Why doesn't it?**

By design, on this fork. `implement` commits, then hands off to `evidence` to publish a proof pack — it does not review its own diff first. Reviewing the code you just wrote is biased toward your own solution, so run [code-review](code-review.md) yourself, in a fresh session, against the commit `implement` just made. Because `implement` commits before handing off, `code-review`'s `<fixed-point>...HEAD` diff has something to see immediately — no interim commit needed first.

**One ticket burned 150k tokens. Am I using it wrong?**

Probably the ticket is too big rather than the skill being misused. A run does codebase exploration, a red-green loop per seam, a full suite, and an evidence pack, so a non-trivial ticket exceeding 100k tokens is normal rather than a sign something broke. The lever is upstream: right-size the tickets in [to-tickets](to-tickets.md) so each fits one fresh window. If a single ticket keeps blowing out, split it rather than raising the effort level.

**`/implement #2` in a fresh session worked on something completely unrelated.**

`#2` is resolved against whatever numbered list the agent can see, which in a fresh session may be a todo file, a checklist, or another work list rather than the configured tracker. The resolution is confident rather than fail-closed, so the mistake is not obvious until it has started. Pass the full reference, the issue URL or `owner/repo#2`, and ask it to confirm the title back before it begins.

## It's working if

- The session opens by reading the ticket or spec and restating what it will build, rather than asking you what to build.
- You can see an actual `/tdd` invocation in the trace, not just tests appearing in the diff.
- Typechecks and single test files run repeatedly during the run, and the full suite runs once near the end.
- The run reaches a commit on your current branch, followed by an evidence pack, without you prompting it to carry on.
- The diff is one ticket's worth of change: a vertical slice through every layer, not several tickets swept together.

## Where it fits

`implement` is the build step of the main chain, second from the end:

```txt
grill-with-docs → to-spec → to-tickets → implement → evidence
```

Its neighbours are [to-tickets](to-tickets.md), which produces the tickets it consumes and declares the blocking edges that decide their order; [tdd](../../skills/engineering/tdd/SKILL.md), which it drives internally at each seam; and [evidence](evidence.md), which it drives internally once more after committing, to publish an auditable proof pack. It commits its own work but doesn't review it; run [code-review](code-review.md) yourself once implementation is done. It sits downstream of the planning skills and trusts them. It does not re-validate the shape of what it was handed, so a badly-structured map or a horizontally-layered ticket gets built as written.

That trust is why [wayfinder](../../skills/engineering/wayfinder/SKILL.md) merges onto the chain at [to-spec](to-spec.md) rather than looping its map straight into `implement`. Go straight to `implement` from a map only when the effort turned out genuinely small.

[ask-sail](../../skills/engineering/ask-sail/SKILL.md) is the router over the whole set when you are not sure which flow you are in.
