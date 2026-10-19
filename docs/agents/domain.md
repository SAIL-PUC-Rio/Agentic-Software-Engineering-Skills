# Domain Docs

How the engineering skills should consume this repo's domain documentation when exploring the codebase.

## Before exploring, read these

- **`CONTEXT-MAP.md`** at the repo root — it points at one `CONTEXT.md` per context. Read each one relevant to the topic.
- **`.agents/adr/`** — system-wide decisions. In this multi-context repo, also check `skills/<bucket>/<skill-name>/docs/adr/` for context-scoped decisions.

If a context's docs don't exist yet, **proceed silently**. Don't flag their absence; don't suggest creating them upfront. The `/domain-modeling` skill (reached via `/grill-with-docs`) creates them lazily when terms or decisions actually get resolved.

## File structure (multi-context)

```
/
├── CONTEXT-MAP.md
├── CONTEXT.md                                          ← the skills repo itself
├── .agents/adr/                                         ← system-wide decisions
└── skills/
    └── <bucket>/
        └── <skill-name>/
            ├── CONTEXT.md                                ← context-specific glossary
            └── docs/adr/                                 ← context-specific decisions
```

Current contexts (per `CONTEXT-MAP.md`): the skills repo itself, and `skills/in-progress/mutation-guided-testing/`.

## Use the glossary's vocabulary

When your output names a domain concept (in an issue title, a refactor proposal, a hypothesis, a test name), use the term as defined in the relevant `CONTEXT.md`. Don't drift to synonyms the glossary explicitly avoids.

If the concept you need isn't in the glossary yet, that's a signal — either you're inventing language the project doesn't use (reconsider) or there's a real gap (note it for `/domain-modeling`).

## Flag ADR conflicts

If your output contradicts an existing ADR, surface it explicitly rather than silently overriding:

> _Contradicts ADR-0007 (event-sourced orders) — but worth reopening because…_
