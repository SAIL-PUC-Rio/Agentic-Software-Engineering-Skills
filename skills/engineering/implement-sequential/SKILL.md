---
name: implement-sequential
description: "Implement every subissue of a spec issue one at a time — a fresh subagent per subissue, evidence closed out before the next starts."
disable-model-invocation: true
---

Work a spec issue's subissues to completion, one at a time, so each subissue gets a clean subagent and a closed-out evidence pack before the next one starts.

## Resolve the subissues

Take the spec issue from the user, or ask for it. Read its subissues and their blocking edges the way `docs/agents/issue-tracker.md` describes for the configured tracker — child issues plus native blocking links on GitHub, `Blocked by` lines in `.scratch/<feature>/issues/*.md` locally. Order them blockers-first: the same frontier `to-tickets`' graph and `wayfinder`'s frontier query both use — a subissue is next only once every subissue that blocks it is closed.

## Work the frontier, one at a time

For each subissue, in that order:

1. **Spawn a subagent** scoped to just this one subissue. Do not have it call the Skill tool with "implement" — `implement` is user-invoked, and per `.agents/invocation.md` that command is reachable only by a human literally typing `/implement`; a call from any other agent, including a subagent this skill spawns on the user's explicit instruction, is refused, full stop. Brief the subagent with `implement`'s own steps inline instead: drive `/tdd` at pre-agreed seams, follow `CODING_STANDARDS.md` and respect the ADRs in the area it's touching, typecheck and run single test files as it goes, run the full suite once at the end, and commit to the current branch when done. Give it only this subissue's context — not the whole spec.
2. **Wait for it to finish** — its commit lands before you move on.
3. **Close it out yourself.** Call the Skill tool with "evidence" — it's model-invoked, so you can call it directly, without going through the subagent — to produce and publish the evidence pack for the commit the subagent just made.
4. **Discard the subagent.** The moment its commit and evidence pack exist, its job is done; don't resume it, don't fold its context into yours.
5. Move to the next subissue in the frontier order.

## Finish

Once every subissue is done, report which ones were completed, link each evidence pack, and name anything that stayed blocked — an unresolved blocker, a subagent that couldn't finish — rather than silently skipping it.
