# The canonical install block

One install story, one wording. `README.md` and the bucket `README.md`s say **this** and nothing else. Change it here first, then propagate.

There are two routes. They are exclusive: the plugin is a managed, read-only bundle you subscribe to; skills.sh writes files you own and edit. Installing both leaves the user with every skill twice, so always say "pick one".

## Claude Code, the plugin

`.claude-plugin/marketplace.json` makes this repo its own single-plugin marketplace. One line installs from it on Claude Code 2.1.275 or later; older versions run `/plugin marketplace add SAIL-PUC-Rio/Agentic-Software-Engineering-Skills` first, then `/plugin install sail-skills@sail`.

<canonical-block name="claude-code">

```
/plugin install sail-skills --marketplace SAIL-PUC-Rio/Agentic-Software-Engineering-Skills
```

</canonical-block>

The plugin ships exactly the promoted set (`skills/engineering/` and `skills/productivity/`). Updates arrive when the marketplace is refreshed.

## Codex, and other agents: skills.sh

The plugin is Claude Code only. Everywhere else, [skills.sh](https://skills.sh) copies editable skill files into the project. Use the whole-set form on `README.md`:

<canonical-block name="skills-sh-whole-set">

```bash
npx skills@latest add SAIL-PUC-Rio/Agentic-Software-Engineering-Skills
```

Pick the skills you want, and which coding agents to install them on. **Make sure `setup-sail-skills` is one of them.**

</canonical-block>

…and the single-skill form wherever one skill is named on its own:

<canonical-block name="skills-sh-one-skill">

```bash
npx skills@latest add SAIL-PUC-Rio/Agentic-Software-Engineering-Skills --skill=<name>
```

```bash
npx skills@latest update <name>
```

</canonical-block>

`skills@latest` is the pinned spelling in all three.

## Contributors

`scripts/link-skills.sh` symlinks every skill in this checkout into `~/.claude/skills` and `~/.agents/skills`, so a `git pull` keeps them current. It is the route for working on the skills themselves, not an install route to document to users.
