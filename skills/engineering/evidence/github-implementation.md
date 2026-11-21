# Publishing: GitHub

## Resolving the task reference

Look for an issue or PR number in recent commit messages (`#123`, `Closes #45`), a path passed as an argument, or active `.scratch` state if the task started local before being filed on GitHub.

Never resolve the target from a branch name or remote URL alone, and never guess a number — confirm it actually exists (`gh issue view <n>` / `gh pr view <n>`) before treating it as the task reference.

A bare `#42` may be an issue or a PR — GitHub shares one number space. Resolve with `gh pr view 42`, falling back to `gh issue view 42`, per `docs/agents/issue-tracker.md`.

## Publishing

Render the pack to a file first — never pass it inline.

1. Write the rendered Markdown pack to a temp file.
2. Post it with `gh issue comment <n> --body-file <path>`. Never use inline `--body "..."` interpolation — the pack's own code fences, backticks, and `$(...)`-shaped text are exactly what corrupts a shell-quoted body.
3. Check for an existing marker with `gh issue view <n> --comments --json comments --jq '.comments[].body'`, grepped for it, to decide fresh-vs-update-in-place per step 9.
4. To update in place: `gh api` a `PATCH` against the existing comment's `id`, rather than posting a duplicate.
