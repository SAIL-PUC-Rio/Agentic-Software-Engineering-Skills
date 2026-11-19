# Ship the skill set as a native Claude Code plugin; defer a native Codex plugin

These skills are installable via [skills.sh](https://skills.sh) (`npx skills@latest add https://github.com/SAIL-PUC-Rio/Agentic-Software-Engineering-Skills/tree/beta`), which copies editable skill files into a user's project across Claude Code, Codex, and other Agent-Skills-standard harnesses. The other distribution people want is **plug-and-play**: subscribe to the set as a read-only, always-current bundle you don't edit. That is what native plugin systems provide.

We ship a native **Claude Code plugin** and, for now, **defer** a native **Codex plugin**. The split is forced by how each ecosystem's plugin manifest selects skills, against this repo's bucketed layout.

## The constraint: bucketed skills vs. single-path selection

Skills live in bucket folders under `skills/` — `engineering/` and `productivity/` are **promoted** (shipped); `in-progress/` and `deprecated/` are **not**. A plugin must expose only the promoted set, which spans two of those bucket folders.

- **Claude Code** — `.claude-plugin/plugin.json` accepts `skills` as an **array of explicit skill-directory paths**. We list the promoted skills one by one, exclude everything else with zero ambiguity, and add `.claude-plugin/marketplace.json` so the repo is its own single-plugin marketplace. `claude plugin validate . --strict` passes, and `marketplace add` → `install` resolves all promoted skills.

- **Codex** — `.codex-plugin/plugin.json` accepts `skills` only as a **single path string** (arrays are rejected with `missing or invalid plugin.json`), and Codex discovers `SKILL.md` files recursively under it. There is no way to name two bucket folders, or to curate a subset, from one path. Two escape hatches were tested and rejected:
  - Pointing at `./skills/` would also ship `deprecated/` and `in-progress/` — retired and draft skills we deliberately don't promote.
  - A curated flat directory of **symlinks** into the buckets does not survive install: Codex copies the plugin tree into its cache and **drops symlinks**, so the skills arrive empty.

The only robust ways to give Codex a single promoted-only path are (a) **restructure** so `skills/` contains only promoted skills, or (b) **commit duplicate copies** of promoted skills into a flat directory. Both are structural decisions, not something to bundle into shipping the Claude plugin.

## Decision

- Ship the **Claude Code plugin** (`.claude-plugin/plugin.json` + `.claude-plugin/marketplace.json`), curated to the promoted set. The documented route is the repo's own marketplace: `/plugin install sail-skills --marketplace https://github.com/SAIL-PUC-Rio/Agentic-Software-Engineering-Skills.git#beta` (or `marketplace add` then `install` on older Claude Code). The plugin is not listed in any third-party marketplace.
- Keep **skills.sh** as the universal installer — it serves Codex and other harnesses, so no Codex user is left without an install path.
- **Defer** the native Codex plugin until we decide between restructuring `skills/` to promoted-only vs. committing a generated flat copy. Revisit when Codex either supports a `skills` array / include-list or preserves symlinks on install.

## Invariants this creates

- Every promoted skill has an entry in `.claude-plugin/plugin.json`'s `skills` array (this already stood as an `AGENTS.md` rule; it now also gates the plugin's contents).
- `.claude-plugin/plugin.json`'s `version` tracks `package.json`'s version — bump both together on release. Claude uses the plugin `version` to decide when installed users see an update.

## History

This repository was forked from an upstream skills repo whose plugin was listed in Claude Code's official marketplace. The fork renamed the plugin to `sail-skills` (version 2.0.0, 2026-10-18), is not in that listing, and documents the self-marketplace route instead.
