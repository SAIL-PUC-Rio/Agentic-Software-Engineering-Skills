## What it does

`implement` builds work that has already been decided. You point it at a [ticket](https://www.aihero.dev/ai-coding-dictionary/ticket), a [spec](https://www.aihero.dev/ai-coding-dictionary/spec), or the plan you just agreed in the conversation, and it writes the code, drives [tdd](https://aihero.dev/skills-tdd) at the seams, typechecks as it goes, commits to the current branch, and closes out with [evidence](https://aihero.dev/skills-evidence), which publishes a factual proof pack for the work to the issue tracker.

It never reopens the plan. There is no interview, no clarifying round, no proposal of a different approach. Whatever was settled upstream is the input, and the skill's whole job is to turn that into a commit. That is what separates it from typing "build this" at a fresh [agent](https://www.aihero.dev/ai-coding-dictionary/agent), which will happily redesign the work while it builds it. It also doesn't review its own work — that's a separate, deliberate step you reach for once implementation is done; publishing proof that the work is done is a different concern, and that one *is* automatic.

## When to reach for it

You invoke this by typing `/implement` — the agent won't reach for it on its own. It ships with `disable-model-invocation: true`, so no other skill can call it either. Wherever [ask-matt](https://aihero.dev/skills-ask-matt) or [to-tickets](https://aihero.dev/skills-to-tickets) says "then `/implement` per ticket", that is an instruction to you, not something the agent will do unprompted.

Where the work currently lives decides whether this is the right skill:

| The work is… | Reach for |
| --- | --- |
| A ticket on the tracker | `/implement #42`, one ticket per [session](https://www.aihero.dev/ai-coding-dictionary/session), [clearing](https://www.aihero.dev/ai-coding-dictionary/clearing) context between tickets |
| A spec, not yet split up, and the build spans sessions | [to-tickets](https://aihero.dev/skills-to-tickets) first, then `/implement` per ticket |
| A spec, and the build is small | `/implement` directly against the spec |
| Only in the conversation you just had, and it's still small | `/implement` right there, in the same window |
| Not written down anywhere yet | [grill-with-docs](https://aihero.dev/skills-grill-with-docs), or [grill-me](https://aihero.dev/skills-grill-me) if there's no codebase |
| One concrete behaviour you want test-first, with no spec | [tdd](https://aihero.dev/skills-tdd) directly |
| Already built, and you want it checked | [code-review](https://aihero.dev/skills-code-review) directly |

The same-session case is worth naming because the skill's own first line doesn't cover it. `SKILL.md` says "the spec or tickets", which nudges the [model](https://www.aihero.dev/ai-coding-dictionary/model) to go hunting for a file that doesn't exist. If the plan lives only in the thread, say so when you invoke it.

## Prerequisites

`implement` commits to the branch you are on. It does not create one, and it does not ask. Check you are on the branch you want the work on before you start.

If the tickets came from [to-tickets](https://aihero.dev/skills-to-tickets), the tracker they live on was configured by [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills). `evidence` reads the same configuration to know where to publish the proof pack at close-out.

## What one run does

A run is five beats, in order:

1. Read the ticket or spec and work out the seams.
2. Drive [tdd](https://aihero.dev/skills-tdd) at the pre-agreed seams, one red-green slice at a time.
3. Typecheck often, run single test files as it goes.
4. Run the full test suite once, at the end.
5. Commit to the current branch, then run [evidence](https://aihero.dev/skills-evidence) to close out.

One run covers one ticket. The tickets [to-tickets](https://aihero.dev/skills-to-tickets) produces are tracer-bullet vertical slices sized to fit a single fresh [context window](https://www.aihero.dev/ai-coding-dictionary/context-window), so the intended rhythm is: clear context, implement one ticket, commit, clear again. Each ticket is self-contained, which is what makes the previous ticket's context disposable.

## Behavior scenarios

If the ticket or spec names `BS-###` scenarios, each one becomes a behavior to drive red-green through [tdd](https://aihero.dev/skills-tdd) at the seam the spec's Testing Decisions assigns to that ID; a developer-facing scenario is driven at its unit or module seam, not through the UI. The scenario says what to observe; the test at the seam is still yours to write. A `**Kind:** regression` scenario is a constraint rather than a feature: it passes before and after your change, and no pre-existing test is edited to make it pass. Unresolved behavior in the spec is not built from a guess. If `bdd-scenarios` (a beta skill outside the plugin) is installed, `implement` reads its during-implementation reference to derive a component scenario from the parent BS: it cites the `BS-###`, adds no behavior, and a case the BS never settles is raised as a question rather than written. Refactoring an existing component starts from its regression mode. It is never invoked by default, and nothing changes without it. Tickets and specs without BS IDs, including legacy `## User Stories` specs, run as before from the acceptance criteria. The same brief is passed to the subagents in [implement-sequential](https://aihero.dev/skills-implement-sequential) and [implement-parallel](https://aihero.dev/skills-implement-parallel).

## Pre-agreed seams

The idea the skill runs on is the **seam**: the public boundary you observe behaviour at, without reaching inside. Tests live at seams. Working at a seam agreed before any code is written is what keeps the tests durable, because the implementation underneath can be rewritten without the tests moving.

Around that core it keeps the loop tight — typecheck often, run single test files as it goes, run the whole suite once at the end — then commits to the current branch and hands off to [evidence](https://aihero.dev/skills-evidence), which publishes what actually got verified to the task's issue tracker.

The word "pre-agreed" is doing real work, and it is also the skill's weakest joint. Nothing inside `implement` agrees the seams. `tdd` is the skill that asks, and it refuses to write a test at an unconfirmed seam. So in practice the agreement happens either upstream in the spec, or in the first exchange of the run. If it happens nowhere, the precondition never fires and the run quietly becomes "just write the code". Naming the seams in the spec is what stops that.

## Common questions

**It finished, but my ticket is still open and the acceptance criteria are still unchecked.**

Correct, and expected. `implement` has no completion step. It ends at the commit and the [evidence](https://aihero.dev/skills-evidence) pack, and never touches the work item itself, confirmed on GitHub Issues and on the local markdown tracker, so it is not a tracker integration problem. It does not tick the `- [ ]` boxes on the originating issue. Close the ticket and reconcile the criteria yourself. This bites hardest on a dependency chain, because `to-tickets` defines the frontier as tickets whose blockers are all closed. If nothing gets closed, nothing ever becomes visibly unblocked.

**Can I point it at all my tickets at once, or run several in parallel?**

Not `implement` itself — one invocation, one ticket, and that hasn't changed. What changed is that batch dispatch across a ticket queue no longer means assembling it yourself: [implement-sequential](https://aihero.dev/skills-implement-sequential) runs a whole spec issue's subissues one after another, a fresh subagent per subissue; [implement-parallel](https://aihero.dev/skills-implement-parallel) runs every unblocked subissue of a wave concurrently. Neither gets there by calling `/implement` from another agent — that call is still refused, same as ever — they brief each subagent with `implement`'s own steps directly instead.

The reason `implement` itself stays single-ticket is the failure mode that made parallel dispatch dangerous in the first place: one field report describes a `git commit --amend` in one session landing on another session's commit, a stash vanishing from `refs/stash`, and commits landing on the wrong branch, all in a single afternoon across three issues, from sessions sharing one working directory, one index, and one HEAD. `implement-parallel` isolates every subagent in its own git worktree specifically because of this — worktrees fix the index/HEAD collision, though `refs/stash` still isn't isolated across them, which is why its subagents are briefed to commit rather than stash.

**Can it open a pull request instead of committing?**

Not built in. It commits straight to the current branch, which several people find too eager: the code lands before they have had a chance to verify it works. There is no configuration flag and no PR mode. People override it in the invocation ("commit to a branch and open a PR") or by editing their local copy of the skill.

**I want `code-review` to run as part of the same pass. Why doesn't it?**

By design, on this fork. `implement` commits, then hands off to `evidence` to publish a proof pack — it does not review its own diff first. Reviewing the code you just wrote is biased toward your own solution, so run [code-review](https://aihero.dev/skills-code-review) yourself, in a fresh session, against the commit `implement` just made. Because `implement` commits before handing off, `code-review`'s `<fixed-point>...HEAD` diff has something to see immediately — no interim commit needed first.

**One ticket burned 150k tokens. Am I using it wrong?**

Probably the ticket is too big rather than the skill being misused. A run does codebase exploration, a red-green loop per seam, a full suite, and an evidence pack, so a non-trivial ticket exceeding 100k [tokens](https://www.aihero.dev/ai-coding-dictionary/token) is normal rather than a sign something broke. The lever is upstream: right-size the tickets in [to-tickets](https://aihero.dev/skills-to-tickets) so each fits one fresh window. If a single ticket keeps blowing out, split it rather than raising the [effort](https://www.aihero.dev/ai-coding-dictionary/effort) level.

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

Its neighbours are [to-tickets](https://aihero.dev/skills-to-tickets), which produces the tickets it consumes and declares the blocking edges that decide their order; [tdd](https://aihero.dev/skills-tdd), which it drives internally at each seam; and [evidence](https://aihero.dev/skills-evidence), which it drives internally once more after committing, to publish an auditable proof pack. It commits its own work but doesn't review it; run [code-review](https://aihero.dev/skills-code-review) yourself once implementation is done. It sits downstream of the planning skills and trusts them. It does not re-validate the shape of what it was handed, so a badly-structured map or a horizontally-layered ticket gets built as written.

That trust is why [wayfinder](https://aihero.dev/skills-wayfinder) merges onto the chain at [to-spec](https://aihero.dev/skills-to-spec) rather than looping its map straight into `implement`. Go straight to `implement` from a map only when the effort turned out genuinely small.

[ask-matt](https://aihero.dev/skills-ask-matt) is the router over the whole set when you are not sure which flow you are in.
