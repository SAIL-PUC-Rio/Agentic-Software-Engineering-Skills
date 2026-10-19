# Productivity

General workflow tools, not code-specific. Shipped in the plugin.

## User-invoked

Reachable only when you type them (Claude Code: `disable-model-invocation: true`; Codex: `policy.allow_implicit_invocation: false` in `agents/openai.yaml`).

- **[grill-me](./grill-me/SKILL.md)** — The same relentless interview as `grill-with-docs`, stateless. For plans and designs with no repo under them.
- **[handoff](./handoff/SKILL.md)** — Compact the current conversation into a handoff document for another agent to pick up.

## Model-invoked

Model- or user-reachable (rich trigger phrasing so the model can reach for them).

- **[grilling](./grilling/SKILL.md)** — The interview primitive behind `grill-me`, `grill-with-docs`, `triage` and `wayfinder`.
- **[writing-for-agents](./writing-for-agents/SKILL.md)** — Writing documents agents consume: skills, `AGENTS.md`, `CLAUDE.md`, and anything reached by a pointer.
