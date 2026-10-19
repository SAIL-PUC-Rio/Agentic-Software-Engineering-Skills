Skills are organized into bucket folders under `skills/`:

- `engineering/` — daily code work
- `productivity/` — daily non-code workflow tools
- `in-progress/` — beta: public on purpose, feedback wanted, not shipped in the plugin
- `deprecated/` — no longer used (empty; a retired skill is deleted and the removing commit names its replacement)

`references/` holds reading material that is not a skill (the cloud patterns catalog). It is never linked into harness skill directories and never listed in the plugin.

Every skill in `engineering/` or `productivity/` (the **promoted** buckets) must have a reference in the top-level `README.md` and an entry in `.claude-plugin/plugin.json`'s `skills` array (the Claude Code plugin ships exactly the promoted set). Skills in `in-progress/` and `deprecated/` must not appear in the plugin; `in-progress/` skills are listed in the README under their own heading.

Install commands are copied verbatim from [.agents/install-block.md](./.agents/install-block.md). `.claude-plugin/marketplace.json` makes the repo its own single-plugin marketplace, and that is the documented Claude Code route. Run `claude plugin validate .` after touching either manifest; the only accepted warning is the one about `CLAUDE.md` at the plugin root, which the Claude Code validator always emits for this layout. Why a Claude plugin but not (yet) a Codex one lives in [.agents/adr/0002-ship-as-a-claude-code-plugin.md](./.agents/adr/0002-ship-as-a-claude-code-plugin.md).

Each skill entry in the top-level `README.md` must link the skill name to its `SKILL.md`.

Each bucket folder has a `README.md` that lists every skill in the bucket with a one-line description, with the skill name linked to its `SKILL.md`. The promoted buckets' `README.md`s and the top-level `README.md` group entries into **User-invoked** and **Model-invoked**; `in-progress/README.md` uses a flat list.

Skills authored or substantially reworked in this repo and living in a promoted bucket have a human-facing docs page at `docs/<bucket>/<skill-name>.md` (today: `code-review`, `evidence`, `implement`, `implement-parallel`, `implement-sequential`, `to-spec`, `to-tickets`). Skills kept from upstream unchanged are documented by their `SKILL.md` alone. When you add a skill to a promoted bucket, or rename or change the behaviour of one that has a page, create or re-sync its page following [.agents/writing-docs.md](./.agents/writing-docs.md). A finished page carries four sections — **What it does**, **When to reach for it**, **Common questions**, **It's working if** — and `writing-docs.md` holds the template and the section order. Skills in `in-progress/` and `deprecated/` get **no** docs page.

Every `SKILL.md` is either user-invoked (`disable-model-invocation: true` plus `policy.allow_implicit_invocation: false` in `agents/openai.yaml`, reachable only by the human) or model-invoked (model- or user-reachable). See [.agents/invocation.md](./.agents/invocation.md).

[`ask-sail`](./skills/engineering/ask-sail/SKILL.md) is the router that maps every user-reachable skill and how they relate. Whenever you add, rename, remove, or change how a user-reachable skill fits the flows, re-read `ask-sail`'s `SKILL.md` and update it so the map stays accurate — a new skill it never mentions, or a stale one it still routes to, is a router that lies.

Vendored third-party skills (today: `show-me`) stay byte-for-byte identical to their source; repo conventions go in sibling files, never in the vendored `SKILL.md`.

To (re)link every skill into the local harness skill directories (`~/.claude/skills`, `~/.agents/skills`), run `scripts/link-skills.sh`. Each entry is a symlink into this repo, so a `git pull` keeps installed skills current; the script also prunes links to skills that no longer exist. Re-run it after adding, removing, or renaming a skill.

`.claude-plugin/plugin.json`'s `version` tracks `package.json`'s; `npm run check-plugin-version` verifies it, `npm run sync-plugin-version` fixes it. Bump both together on release.

## Agent skills

### Issue tracker

Issues live in this repo's GitHub Issues (`Esduard/skills`, via the `gh` CLI). See `docs/agents/issue-tracker.md`.

### Triage labels

Default vocabulary: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. See `docs/agents/triage-labels.md`.

### Domain docs

Multi-context: a root `CONTEXT-MAP.md` pointing to per-context `CONTEXT.md` files. See `docs/agents/domain.md`.
