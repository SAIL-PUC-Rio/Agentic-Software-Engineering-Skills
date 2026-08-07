Create a new Claude Code skill named `Evidence`.

This is an implementation task, not merely a design exercise. Inspect the repository, determine its conventions, create the skill and template, integrate it with the existing `Implement` skill, validate the result, and report the files changed.

# Objective

`Evidence` must be an engineering skill that runs as the closeout stage of the existing `Implement` skill.

After `Implement` finishes its work, `Evidence` must produce a factual, auditable evidence pack demonstrating what was changed, which requirements were addressed, which validations were actually executed, and what remains uncertain.

The evidence must then be published to the task’s canonical collaboration channel:

- As a comment on the relevant GitHub issue when the active task is GitHub-backed.
- Through the repository’s local `.scratch` workflow when the active task is local.
- It must not assume that the existence of a GitHub remote means that the current task is a GitHub issue.

The skill must follow the principle:

> Trust is earned through verifiable evidence, not through a confident narrative.

Do not claim that something works merely because the implementation looks plausible.

# Phase 1 — Repository investigation

Before changing files, inspect the repository and determine how skills and task modes actually work.

At minimum, inspect:

1. The root `CLAUDE.md` and any nested Claude instructions relevant to skills.
2. The directory structure and metadata used to group skills into sets.
3. The existing `Implement` skill in full.
4. The existing `Setup-Matt-Pocock` skill in full.
5. Any capitalization or naming variants of `Setup-Matt-Pocock`.
6. At least two other skills in the engineering set.
7. Existing skill templates, supporting Markdown templates, helper scripts, and skill registries or indexes.
8. All references to:
   - `.scratch`
   - GitHub issues
   - `gh issue`
   - issue comments
   - task mode
   - work item
   - task source
   - setup state
   - current issue
   - issue number
   - repository slug
9. Any commands or helpers already used to:
   - determine whether work is GitHub-backed or local;
   - find the active issue;
   - post a GitHub issue comment;
   - store comments, results, or completion records in `.scratch`.

Do not invent paths, metadata fields, helper commands, or invocation syntax. Reuse the repository’s existing conventions.

Pay particular attention to `Setup-Matt-Pocock`. Determine what canonical state or metadata it creates to distinguish:

- GitHub issue mode;
- local `.scratch` mode;
- a repository that has a GitHub remote but whose current task is local.

The mode-selection behavior of `Evidence` must agree with the setup workflow rather than creating a competing heuristic.

Any mode behaviour for `Evidence`, be it the github or the local .scratch, must be made into a separate skill to not overload the main skill. so evidence should call all "github" instructions from a separate skill or ".scratch" from a separate skill as to maintain the context window smaller.

Before implementation, summarize the discovered conventions briefly in the working session so the subsequent edits are grounded in the repository.

# Phase 2 — Create the Evidence skill

Create `Evidence` inside the repository’s existing engineering skill set.

Use the exact directory layout, front matter, naming, description style, invocation conventions, and registration mechanisms used by neighboring engineering skills.

The skill should remain usable in two ways:

1. Automatically as the final stage of `Implement`.
2. Manually when evidence needs to be regenerated or inspected.

The skill must explain that its responsibility is not to repeat the implementation summary. Its responsibility is to connect claims about the completed work to reproducible evidence.

## Core workflow

The skill must perform the following process.

### 1. Resolve the task context

Determine:

- task mode: GitHub issue or local `.scratch`;
- canonical task identifier;
- issue number and repository when applicable;
- local work-item location when applicable;
- repository root;
- current branch;
- base and current commit identifiers when available;
- conceptual plan, acceptance criteria, or issue requirements;
- implementation result received from `Implement`.

Use explicit task context and setup metadata before using secondary heuristics.

Use this precedence:

1. Explicit context passed by `Implement`.
2. Canonical state produced by `Setup-Matt-Pocock`.
3. Existing active-work-item metadata in the repository.
4. Conservative repository inspection.

Do not choose a GitHub issue based only on a branch name, remote URL, or guessed issue number.

When the target remains ambiguous, do not post externally. Generate the evidence locally in the safest canonical `.scratch` location and clearly mark publication as blocked because the destination could not be resolved.

### 2. Identify the claims that require evidence

Extract the claims from:

- issue acceptance criteria;
- Definition of Done;
- requested behavior;
- implementation plan;
- invariants or constraints;
- final implementation summary;
- any approved deviations.

Give each claim a stable identifier such as:

- `CLM-001`
- `CLM-002`
- `CLM-003`

Do not treat “implementation completed” as sufficient evidence.

### 3. Build a scope-to-proof map

For every relevant claim, record:

- the claim;
- its source;
- the implementation surface associated with it;
- the verification method;
- the corresponding evidence identifiers;
- the final status.

Use a controlled status vocabulary:

- `PASS`
- `FAIL`
- `PARTIAL`
- `NOT_RUN`
- `NOT_APPLICABLE`
- `UNKNOWN`

Never silently convert `NOT_RUN` or `UNKNOWN` into `PASS`.

They should be stored inside the skill folder as templates for status of evidence. much like skills/engineering/setup-matt-pocock-skills/triage-labels.md inside the setup skills

### 4. Collect factual evidence

Use evidence that can be independently inspected, such as:

- exact tests that were executed;
- test exit codes;
- relevant test output;
- newly added or modified tests;
- lint output;
- formatter checks;
- type-checking output;
- static-analysis output;
- build output;
- executable examples;
- runtime checks;
- focused reproduction commands;
- git diff and changed-file information;
- configuration validation;
- schema or migration validation;
- generated artifacts;
- relevant logs;
- repository status;
- commit identifiers;
- explicit decision and deviation records.

For every executed command, preserve:

- the exact command;
- working directory;
- UTC execution time;
- exit code;
- concise result;
- a pointer to the complete output when the repository has an appropriate place for it.

Do not rerun expensive, destructive, production-facing, credential-sensitive, or externally mutating operations merely to manufacture evidence.

Use existing validation results passed by `Implement` when they are trustworthy and sufficiently detailed. Run additional checks only when they are safe, relevant, and necessary to close an evidence gap.

### 5. Record negative evidence honestly

Evidence must include failures and omissions.

Explicitly record:

- tests that failed;
- tests that were not executed;
- validations unavailable in the current environment;
- missing credentials or services;
- unresolved assumptions;
- incomplete acceptance criteria;
- behavioral areas not covered;
- commands that produced inconclusive results;
- evidence publication failures.

A failure to prove a claim must remain visible.

Do not fabricate logs, commands, timestamps, exit codes, checksums, issue references, or test results.

### 6. Compare the plan with the execution

Create a compact plan ledger containing:

- the original conceptual plan;
- the executed approach;
- meaningful deviations;
- why each deviation occurred;
- whether the deviation remained inside the allowed scope;
- any approval or issue discussion associated with it.

Do not expose private chain-of-thought. Record concise engineering rationales and observable decisions only.

### 7. Capture provenance and chain of custody

For each evidence artifact, record as applicable:

- stable evidence identifier;
- producer;
- generation time in UTC;
- command or tool used;
- tool version when available;
- repository and branch;
- commit or working-tree state;
- file or output pointer;
- SHA-256 checksum for persisted evidence files;
- access classification when the repository has such a convention.

Only provide a checksum when it was actually computed over an existing artifact.

### 8. Organize evidence through progressive disclosure

The evidence pack must be readable at different depths:

1. A short result summary.
2. Claim and acceptance-criteria status.
3. Verification and engineering-hygiene summaries.
4. Detailed commands, outputs, logs, manifests, and artifact pointers.

Do not bury the result under raw terminal output.

Use collapsible Markdown details where appropriate for GitHub comments, while keeping the primary status visible without expanding anything.

# Phase 3 — Create the Markdown template

Create a Markdown evidence template in the same folder as the `Evidence` skill.

Name it according to repository conventions. Prefer `EVIDENCE_TEMPLATE.md` unless neighboring skills establish another naming pattern.

The `Evidence` skill must explicitly load and use this file rather than duplicating the entire template inside `SKILL.md`.

The template must contain at least the following sections.

## Required template structure

### Evidence Pack

Basic metadata:

- Pack ID
- Template version
- Generated at, in UTC
- Overall status
- Task mode
- Task reference
- Repository
- Branch
- Base revision
- Current revision
- Working-tree state
- Producer

### 1. Executive result

A concise statement of:

- what was implemented;
- whether the requested properties were proven;
- the overall evidence status;
- the most important limitation, when one exists.

### 2. Scope-to-proof map

A table with columns equivalent to:

| Claim ID | Requirement or property | Source | Verification | Evidence IDs | Status |

### 3. Change inventory

Include:

- files added;
- files modified;
- files deleted;
- configuration or schema changes;
- externally visible behavior changes;
- intentionally untouched areas.

### 4. Verification bundle

Include:

- tests run;
- newly added tests;
- edge and failure cases;
- integration or end-to-end checks;
- command, exit code, result, and evidence ID;
- skipped or unavailable checks.

### 5. Engineering hygiene

Include applicable evidence for:

- linting;
- formatting;
- static analysis;
- type checking;
- build validation;
- complexity or maintainability;
- repository-specific architectural rules;
- coding standards.

Mark unavailable categories as `NOT_RUN` or `NOT_APPLICABLE`. Do not omit them in a way that implies they passed.

### 6. Plan ledger and deviations

Include:

- conceptual plan;
- executed plan;
- deviations;
- rationale;
- scope or autonomy impact;
- associated evidence or approval pointer.

### 7. Rationale and trade-offs

Capture concise, reviewable engineering decisions:

- selected approach;
- important alternatives considered;
- why alternatives were rejected;
- known trade-offs.

Do not include hidden reasoning or verbose conversational history.

### 8. Exploration archive

Summarize relevant experiments and rejected paths.

Provide pointers to complete exploration artifacts where they exist rather than placing all raw material in the main report.

### 9. Risks, rollback, and limitations

Include:

- residual risks;
- blast radius;
- rollback or recovery approach;
- incomplete work;
- assumptions;
- environment limitations;
- missing evidence;
- follow-up work.

### 10. Chain of custody

Include the provenance necessary to reconstruct how the evidence was produced.

### 11. Machine-readable manifest

Include a delimited YAML block inside the Markdown file using explicit markers such as:

`<!-- evidence-manifest:start -->`

and:

`<!-- evidence-manifest:end -->`

The manifest should follow a structure equivalent to:

manifest_version: "1.0"
pack_id: "..."
task:
  mode: "github|scratch"
  reference: "..."
repository:
  branch: "..."
  base_revision: "..."
  current_revision: "..."
generated:
  at_utc: "..."
  producer: "..."
claims:
  - id: "CLM-001"
    status: "PASS|FAIL|PARTIAL|NOT_RUN|NOT_APPLICABLE|UNKNOWN"
    evidence_ids:
      - "EVD-001"
artifacts:
  - id: "EVD-001"
    category: "test|lint|build|diff|log|decision|exploration|risk|other"
    status: "PASS|FAIL|PARTIAL|NOT_RUN|NOT_APPLICABLE|UNKNOWN"
    claim_ids:
      - "CLM-001"
    command: "..."
    working_directory: "..."
    exit_code: 0
    pointer: "..."
    sha256: "..."
    generated_at_utc: "..."
    producer: "..."
    tool: "..."
    tool_version: "..."

Adapt field names to existing repository conventions where needed.

The generated manifest must be syntactically valid and enumerable. Do not place explanatory prose inside fields intended for machine parsing.

# Phase 4 — Publishing behavior

Implement publication using the repository’s existing mechanisms.

## GitHub issue mode

When the setup state unambiguously says the current task is GitHub-backed:

- Publish the rendered evidence as a comment on the correct issue.
- Prefer an existing repository helper over directly constructing a new command.
- When direct CLI use is the established convention, use a body file rather than unsafe shell interpolation.
- Make the comment readable using progressive disclosure.
- Include the executive result and scope-to-proof table near the top.
- Preserve the machine-readable manifest in the posted body unless existing repository conventions provide a durable linked artifact.
- Do not expose secrets, tokens, credentials, sensitive environment values, or unnecessarily large logs.

Add an invisible stable marker to support idempotency, for example:

`<!-- evidence-pack:<task-reference>:<revision> -->`

On regeneration, update or replace the matching evidence publication when the repository’s tooling allows it. Do not create repeated duplicate comments for the same task and revision.

If GitHub mode is confirmed but authentication or publication fails:

- preserve the generated evidence locally using the canonical recovery location;
- report that evidence generation succeeded but GitHub publication failed;
- do not silently reclassify the task as local.

## Local `.scratch` mode

When the setup state says the task is local:

- use the established `.scratch` task structure;
- publish the evidence through the local equivalent of an issue comment or closeout record;
- preserve the full Markdown evidence pack;
- use the task’s canonical identifier and location;
- make regeneration idempotent or revision-aware;
- do not create an unrelated new `.scratch` convention.

## Ambiguous mode

When no canonical destination can be proven:

- do not guess;
- do not post to GitHub;
- write the evidence to the safest canonical local recovery location;
- mark destination resolution as blocked;
- tell the caller exactly what metadata is missing.

# Phase 5 — Integrate Evidence with Implement

Modify the existing `Implement` skill so that `Evidence` becomes its required closeout stage.

Mirror the way skills in this repository compose or invoke other skills. Do not invent a new composition mechanism when one already exists.

`Implement` should provide `Evidence` with as much structured context as the current framework supports, including:

- task mode and task reference;
- original issue or work-item requirements;
- acceptance criteria;
- conceptual implementation plan;
- completed changes;
- commands already executed;
- command outputs and exit codes;
- tests added;
- tests not run;
- deviations;
- unresolved risks;
- current repository state.

Required behavior:

1. Implementation occurs.
2. Implementation validation occurs.
3. `Evidence` performs closeout and publication.
4. `Implement` reports both:
   - implementation status;
   - evidence-generation and publication status.

Do not let a publication failure erase or misreport the implementation result.

Conversely, do not mark the overall task as fully proven when evidence generation reveals failed or missing acceptance criteria.

Run `Evidence` at closeout even when implementation is partial or failed, because failed commands, blocked requirements, and unresolved gaps are themselves relevant evidence.

Avoid duplicating the complete evidence template inside `Implement`. `Implement` should delegate evidence responsibilities to `Evidence`.

# Phase 6 — Validation

Validate the new workflow using the repository’s existing testing or validation conventions.

At minimum, verify:

- the new skill is inside and discoverable from the engineering set;
- its metadata and front matter are valid;
- it references the Markdown template correctly;
- the template exists in the same skill folder;
- the YAML manifest example is syntactically valid;
- `Implement` invokes or delegates to `Evidence`;
- GitHub mode does not activate solely because a remote exists;
- local mode uses the canonical `.scratch` structure;
- ambiguous mode does not post externally;
- statuses distinguish pass, fail, partial, not-run, not-applicable, and unknown;
- missing validations are visible;
- the publication method avoids shell-quoting corruption;
- rerunning evidence does not spam duplicate comments or records.

Do not post test comments to real GitHub issues.

Use mocks, dry-run support, temporary fixtures, or existing repository test helpers for publication tests.

Do not perform destructive operations or modify unrelated task records while testing.

# Constraints

- Inspect first; edit second.
- Preserve existing repository architecture.
- Prefer existing helpers and abstractions.
- Do not introduce a large framework merely to create this skill.
- Do not duplicate mode-detection logic already owned by `Setup-Matt-Pocock`.
- Do not fabricate proof.
- Do not confuse a narrative summary with evidence.
- Do not expose chain-of-thought.
- Do not hide failed or missing validation.
- Do not post to an issue unless the issue destination is unambiguous.
- Do not create test comments on live issues.
- Do not modify unrelated skills.
- Update a skill registry, index, or documentation only when the repository requires it for discoverability.

# Completion criteria

The task is complete only when:

1. `Evidence` exists as a valid engineering skill.
2. A Markdown evidence template exists in the same folder.
3. The skill generates a structured, progressively disclosed evidence pack.
4. The pack contains a machine-readable manifest with stable claim and evidence identifiers.
5. Evidence contains provenance and truthful execution results.
6. GitHub-backed work is published to the correct issue comment.
7. Local work is published through the existing `.scratch` workflow.
8. Mode selection agrees with `Setup-Matt-Pocock`.
9. `Implement` delegates its final closeout to `Evidence`.
10. The behavior has been validated without posting test data to a real issue.

# Final response

After making the changes, report:

- the repository conventions discovered;
- how GitHub mode and local mode are distinguished;
- every file created or modified;
- how `Implement` now delegates to `Evidence`;
- the evidence template structure;
- validation commands and their actual outcomes;
- any assumptions, limitations, or unverified behavior.

Do not merely state that the skill was created. Provide factual evidence for this implementation as well.