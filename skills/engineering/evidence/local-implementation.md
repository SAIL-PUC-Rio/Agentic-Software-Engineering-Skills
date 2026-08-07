# Publishing: Local `.scratch`

## Resolving the task reference

The task reference is the ticket's path: `.scratch/<feature-slug>/issues/<NN>-<slug>.md`. Find the file whose `Status:` line is `claimed` under the feature the current work belongs to, or use the map/spec file directly if that's what the task pointed at.

## Publishing

There is no separate "comment" mechanism to invent — the local tracker already defines one.

1. Append the rendered pack under that file's `## Comments` heading, per the local tracker's own convention — creating the heading if it isn't already there.
2. Check the file for an existing marker before appending, to decide fresh-vs-update-in-place per step 9.
3. To update in place, replace that prior block rather than appending a duplicate.
