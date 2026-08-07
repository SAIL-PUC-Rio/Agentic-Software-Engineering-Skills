# Evidence Pack

- **Pack ID:**
- **Template version:** 1.0
- **Generated at (UTC):**
- **Overall status:** <!-- see claim-labels.md -->
- **Task mode:** <!-- github | gitlab | scratch | other | ambiguous -->
- **Task reference:**
- **Repository:**
- **Branch:**
- **Base revision:**
- **Current revision:**
- **Working-tree state:** <!-- clean | dirty, and why if dirty -->
- **Producer:**

## 1. Executive result

What was implemented, in one or two sentences. Whether the requested properties were actually proven (not just attempted). The overall evidence status. The single most important limitation, if one exists.

## 2. Scope-to-proof map

| Claim ID | Requirement or property | Source | Verification | Evidence IDs | Status |
| -------- | ------------------------ | ------ | ------------- | ------------ | ------ |
| CLM-001  |                           |        |               |              |        |

## 3. Change inventory

- **Added:**
- **Modified:**
- **Deleted:**
- **Config/schema changes:**
- **Externally visible behaviour changes:**
- **Intentionally untouched:**

## 4. Verification bundle

- **Tests run:**
- **Newly added tests:**
- **Edge/failure cases covered:**
- **Integration/e2e checks:**
- **Skipped or unavailable checks:**

| Command | Exit code | Result | Evidence ID |
| ------- | --------- | ------ | ------------ |
|         |           |        |              |

## 5. Engineering hygiene

| Category | Status | Evidence ID |
| --- | --- | --- |
| Linting | | |
| Formatting | | |
| Static analysis | | |
| Type checking | | |
| Build | | |
| Repo-specific architectural rules / coding standards | | |

For now, don't investigate whether a category applies to this repo — mark any category `implement` didn't already run as `NOT_RUN` without further discovery. Never leave a row blank in a way that implies a pass.

## 6. Plan ledger and deviations

- **Conceptual plan:**
- **Executed approach:**
- **Deviations:** what changed, why, whether it stayed in scope, and any approval/discussion pointer.

## 7. Rationale and trade-offs

- **Approach taken:**
- **Alternatives considered:**
- **Why rejected:**
- **Known trade-offs:**

## 8. Exploration archive

Rejected paths and experiments worth a one-line summary, with a pointer to full artifacts where they exist. Not a transcript.

## 9. Risks, rollback, and limitations

- **Residual risk / blast radius:**
- **Rollback approach:**
- **Incomplete work:**
- **Assumptions:**
- **Environment limitations:**
- **Missing evidence:**
- **Follow-up work:**

## 10. Chain of custody

Per artifact: producer, generation time (UTC), command/tool (+ version if known), repo/branch/revision, file/output pointer, and a SHA-256 checksum — only when actually computed over a real file.

## 11. Machine-readable manifest

<!-- evidence-manifest:start -->

```yaml
# claims[].status and artifacts[].status: see claim-labels.md for the valid values
manifest_version: "1.0"
pack_id: ""
task:
  mode: "github|gitlab|scratch|other|ambiguous"
  reference: ""
repository:
  branch: ""
  base_revision: ""
  current_revision: ""
generated:
  at_utc: ""
  producer: ""
claims:
  - id: "CLM-001"
    status: ""
    evidence_ids:
      - "EVD-001"
artifacts:
  - id: "EVD-001"
    category: "test|lint|build|diff|log|decision|exploration|risk|other"
    status: ""
    claim_ids:
      - "CLM-001"
    command: ""
    working_directory: ""
    exit_code: 0
    pointer: ""
    sha256: ""
    generated_at_utc: ""
    producer: ""
    tool: ""
    tool_version: ""
```

<!-- evidence-manifest:end -->

<!-- evidence-pack:<task-reference>:<revision> -->
