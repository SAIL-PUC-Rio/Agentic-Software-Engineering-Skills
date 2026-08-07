# Publishing: GitLab

## Resolving the task reference

Look for an issue or MR reference in recent commit messages (`#123`, GitLab's `!67` for merge requests), a path passed as an argument, or active `.scratch` state if the task started local before being filed on GitLab.

Never resolve the target from a branch name or remote URL alone, and never guess a number — confirm it actually exists (`glab issue view <n>` / `glab mr view <n>`) before treating it as the task reference.

## Publishing

Same shape as GitHub, with `glab` in place of `gh` and "note" in place of "comment":

1. Write the rendered Markdown pack to a temp file.
2. Post it with `glab issue note <n> -F <path>` (or `glab mr note <n> -F <path>` when the task reference is a merge request) — read the body from the file rather than inlining it, for the same shell-quoting reasons as the GitHub path.
3. Check for an existing marker via `glab issue view <n> --comments` (or `glab mr view <n> --comments`) to decide fresh-vs-update-in-place per step 9.
4. To update in place, use the GitLab API directly if `glab` doesn't expose an edit command.
