---
name: evidence
description: Produce a factual, auditable evidence pack for completed work and publish it to the task's issue tracker — the scope-to-proof map, verification results, and negative evidence. Use when the user wants proof a change works, an evidence pack, an audit trail for a commit, or after implement finishes a piece of work.
---

Trust is earned through verifiable evidence, not a confident narrative. `evidence` connects claims about completed work to reproducible proof — it does not repeat the implementation summary.

The issue tracker should have been provided to you — run `/setup-matt-pocock-skills` if `docs/agents/issue-tracker.md` is missing. Without it, `evidence` cannot know where to publish and falls back to the ambiguous-mode path below.

## Process

### 1. Resolve the task context

Determine task mode, task reference, repository root, current branch, and base/current commit, in this order of precedence:

1. Explicit context passed by `implement` in the current conversation (spec, tickets, issue reference already discussed).
2. Canonical state in `docs/agents/issue-tracker.md` — this is the **Issue tracker** `setup-matt-pocock-skills` configured. Read it; don't guess which tracker is in play.
3. Existing active-work-item metadata in the repo, resolved the way the configured tracker resolves it — see [github-implementation.md](./github-implementation.md), [gitlab-implementation.md](./gitlab-implementation.md), [local-implementation.md](./local-implementation.md), or [other-implementation.md](./other-implementation.md).
4. Conservative repository inspection, as a last resort.

**If the mode is still ambiguous** once you've exhausted the above: do not publish externally. Write the pack to `.scratch/_evidence/<UTC-timestamp>-<slug>.md` instead, and mark publication as blocked in the pack's executive result, naming exactly what metadata was missing (usually: `/setup-matt-pocock-skills` was never run).

### 2. Identify the claims

Pull claims from acceptance criteria, Definition of Done, the implementation plan, invariants, and the final implementation summary. Give each a stable ID (`CLM-001`, `CLM-002`, …). "Implementation completed" is never itself a claim's evidence.

**When the originating spec has `## Behavioral Specifications`**, every in-scope `BS-###` also becomes a claim, one per scenario. Its Source records the BS ID and the story IDs on its **Stories:** line (e.g. `BS-002 (STORY-001, STORY-003)`), and its requirement is the scenario title. In scope means the ticket or spec slice names it. A spec with no such section, including a legacy `## User Stories` one, adds nothing here.

### 3. Build the scope-to-proof map

For each claim, record its source, the implementation surface it maps to, how it's verified, the evidence IDs backing it, and a status. The full status vocabulary and its rules live in [claim-labels.md](./claim-labels.md) — use it as-is, never a status outside that table.

A BS-derived claim's Verification is the test at the seam the spec's Testing Decisions assigns to that BS ID. Its status comes from that test's actual run: `PASS` or `FAIL` from the run, `NOT_RUN` if a verifying test exists but wasn't executed, `NOT_APPLICABLE` if no test verifies the scenario. A scenario with no verifying test is never `PASS`, and the claim carries no test EVD.

### 4. Collect evidence — reuse before rerunning

Prefer the commands, exit codes, and output `implement` already produced in this same conversation — reusing them is what keeps this step's token cost down. Run an additional command only to close a specific gap, and never rerun anything expensive, destructive, production-facing, or credential-sensitive merely to manufacture evidence.

For a BS-derived claim, the EVD is the run of the test at the agreed seam that verifies it, and that EVD lists the BS claim in its `claim_ids`. Test runs `implement` already produced count; find the test by the BS ID in its name or comment, or by the ticket's seam mapping.

Also record the `bdd-scenarios` review-mode result for the in-scope scenarios as one EVD artifact (category `decision`), citing the per-attribute `PASS`/`REVISE`/`NOT_APPLICABLE` findings and any `### Unresolved behavior`. Reuse a review already run in this conversation. Otherwise, if `bdd-scenarios` is installed, call the Skill tool with "bdd-scenarios" and run its review mode over the in-scope Gherkin; that skill is a beta, so if it is not installed, record the artifact as `NOT_RUN` and say why. The review artifact's status reports the review only, and never raises a claim's status.

For every command (reused or newly run), keep the exact command, working directory, UTC time, exit code, and a concise result.

### 5. Record negative evidence honestly

Failed tests, skipped validations, missing credentials, unresolved assumptions, inconclusive commands, publication failures — all stay visible. Never fabricate a log, command, timestamp, checksum, or test result to fill a gap.

### 6. Compare plan to execution

A compact ledger: the conceptual plan, what was actually executed, meaningful deviations and why, and whether each stayed in scope. Concise engineering rationale only — no chain-of-thought.

### 7. Capture provenance

Per evidence artifact: an ID, producer, UTC generation time, command/tool used, repo/branch/commit, a pointer to the artifact, and a SHA-256 checksum — only when one was actually computed over a real file.

### 8. Assemble the pack

Use [EVIDENCE_TEMPLATE.md](./EVIDENCE_TEMPLATE.md) verbatim — don't duplicate its structure here. Fill it depth-first: executive result, then claim/criteria status, then verification and hygiene summaries, then full detail. Never bury the result under raw terminal output.

### 9. Publish through the configured tracker

Every pack carries the idempotency marker `<!-- evidence-pack:<task-reference>:<revision> -->`. Before publishing, check whether one already exists for this task: no match, or a match for a *different* revision, means publish fresh; a match for the *same* revision means this is a regeneration — update that publication in place rather than creating a duplicate.

`docs/agents/issue-tracker.md` names which tracker is configured. *How* to check for the marker and *how* to update in place differ by tracker, so only those mechanics are externalized, one file per tracker:

- **GitHub** → [github-implementation.md](./github-implementation.md)
- **GitLab** → [gitlab-implementation.md](./gitlab-implementation.md)
- **Local `.scratch`** → [local-implementation.md](./local-implementation.md)
- **Other** (freeform) → [other-implementation.md](./other-implementation.md)

If the mode is confirmed but publication fails (auth, network, tracker outage), keep the generated pack in the local recovery location from step 1, report that evidence generation succeeded but publication failed, and do not reclassify the task as local-mode just because the post didn't land.

### 10. Report back

Report per the rules in [claim-labels.md](./claim-labels.md): implementation status and evidence status as two separate lines, neither one silently overwriting the other.
