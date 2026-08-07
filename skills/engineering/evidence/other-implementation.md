# Publishing: Other (freeform) trackers

`docs/agents/issue-tracker.md` carries a freeform description of how this repo's tracker works, written by the user during `/setup-matt-pocock-skills`. There is no fixed CLI shape to follow — read that description and use whatever posting mechanism it names (an API call, a different CLI, a manual step).

## Resolving the task reference

Follow however that description identifies the current task (an ID, a URL, a name). If it doesn't describe a way to identify one, treat the task as ambiguous rather than guessing.

## Publishing

Regardless of mechanism:

1. Render the pack to a file first.
2. Check whether the described workflow gives you a way to detect an existing marker before publishing, to decide fresh-vs-update-in-place per step 9. If it gives no way to check, publish fresh but note in the pack's chain of custody that idempotency couldn't be verified.

If the described workflow doesn't support programmatic publishing at all, fall back to the ambiguous-mode path in `SKILL.md` — write the pack locally and report publication as blocked, naming the gap.
