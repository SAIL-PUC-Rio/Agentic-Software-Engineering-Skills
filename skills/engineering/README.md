# Engineering

Skills for daily code work. Shipped in the plugin.

## User-invoked

Reachable only when you type them (Claude Code: `disable-model-invocation: true`; Codex: `policy.allow_implicit_invocation: false` in `agents/openai.yaml`).

- **[ask-sail](./ask-sail/SKILL.md)** — Ask which skill or flow fits your situation. A router over the skills in this repo.
- **[setup-sail-skills](./setup-sail-skills/SKILL.md)** — Configure a repo for the engineering skills: issue tracker, triage labels, domain doc layout. Run once per repo.
- **[grill-with-docs](./grill-with-docs/SKILL.md)** — A relentless interview to sharpen a plan or design, which also builds the project's domain model: `CONTEXT.md` and ADRs, updated inline.
- **[to-spec](./to-spec/SKILL.md)** — Turn the current conversation into a spec with typed stories and Behavioral Specifications, and publish it to the issue tracker. No interview, just synthesis.
- **[to-tickets](./to-tickets/SKILL.md)** — Break a spec or conversation into tracer-bullet tickets with blocking edges and a rendered dependency graph.
- **[implement](./implement/SKILL.md)** — Build the work described by a spec or ticket, driving `tdd` at agreed seams with the scenarios as reference, then commit and close out with `evidence`.
- **[implement-sequential](./implement-sequential/SKILL.md)** — Build every subissue of a spec issue one at a time: a fresh subagent per subissue, evidence closed out before the next starts.
- **[implement-parallel](./implement-parallel/SKILL.md)** — Build every independent subissue of a spec issue in waves, one subagent per subissue in its own worktree.
- **[triage](./triage/SKILL.md)** — Move incoming issues and external PRs through a state machine of triage roles and write agent-ready briefs.
- **[wayfinder](./wayfinder/SKILL.md)** — Plan a huge chunk of work as a shared map of decision tickets on the issue tracker, resolved one at a time.

## Model-invoked

Model- or user-reachable (rich trigger phrasing so the model can reach for them).

- **[tdd](./tdd/SKILL.md)** — Test-driven development with a red-green-refactor loop, one vertical slice at a time.
- **[evidence](./evidence/SKILL.md)** — Publish a factual scope-to-proof map for completed work: claims, verification, negative evidence. `implement`'s mandatory closeout.
- **[code-review](./code-review/SKILL.md)** — Two-axis review of the diff since a fixed point: Standards and Spec, as parallel subagents.
- **[domain-modeling](./domain-modeling/SKILL.md)** — Build and sharpen the project's domain model: challenge terms, stress-test with edge cases, update `CONTEXT.md` and ADRs inline.
- **[codebase-design](./codebase-design/SKILL.md)** — The deep-module vocabulary for designing a module's shape.
- **[prototype](./prototype/SKILL.md)** — A throwaway prototype that answers one design question.
- **[research](./research/SKILL.md)** — Investigate a question against primary sources in a background agent and leave a cited Markdown file in the repo.
- **[resolving-merge-conflicts](./resolving-merge-conflicts/SKILL.md)** — Work an in-progress merge or rebase conflict hunk by hunk, resolving by intent, never `--abort`.
