---
"mattpocock-skills": minor
---

Add **`evidence`**, a model-invoked skill that runs automatically as `implement`'s mandatory closeout — publishing a factual scope-to-proof map, verification results, and negative evidence to the task's configured issue tracker (GitHub, GitLab, local `.scratch`, or a described "other" tracker) instead of a confident narrative. It never treats "implementation completed" as evidence on its own, and never upgrades a `NOT_RUN`/`UNKNOWN` claim to `PASS`.

`implement` now commits, then drives `/evidence` internally; both the implementation result and the evidence-generation/publication result get reported, and a publication failure never erases the implementation result. This deliberately reverses the direction taken when `/code-review`'s auto-closeout was removed from `implement` for token/latency reasons — see `.agents/adr/0003-evidence-runs-as-implements-mandatory-automatic-closeout.md` for why, and the anticipated escape hatch if token cost proves too high in practice.

`CONTEXT.md` gains **Evidence pack** and **Claim** as domain terms. Docs pages for `implement` and the new `evidence` skill are synced; both READMEs, `ask-matt`, and `.claude-plugin/plugin.json` reference the new skill.
