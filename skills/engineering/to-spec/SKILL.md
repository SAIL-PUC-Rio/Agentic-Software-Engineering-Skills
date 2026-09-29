---
name: to-spec
description: Turn the current conversation into a spec and publish it to the project issue tracker — no interview, just synthesis of what you've already discussed.
disable-model-invocation: true
---

This skill takes the current conversation context and codebase understanding and produces a spec. Do NOT interview the user — just synthesize what you already know.

The issue tracker and triage label vocabulary should have been provided to you. If not, tell the user to run `/setup-matt-pocock-skills`.

## Process

1. Explore the repo to understand the current state of the codebase, if you haven't already. Use the project's domain glossary vocabulary throughout the spec, and respect any ADRs in the area you're touching.

2. Sketch out the seams at which you're going to test the feature. Existing seams should be preferred to new ones. Use the highest seam possible. If new seams are needed, propose them at the highest point you can. The fewer seams across the codebase, the better - the ideal number is one.

Check with the user that these seams match their expectations.

3. Write the spec using the template below, then publish it to the project issue tracker. Apply the `ready-for-agent` triage label - no need for additional triage.

<spec-template>

## Problem Statement

The problem that the user is facing, from the user's perspective.

## Solution

The solution to the problem, from the user's perspective.

## Stories

Typed, ID'd entries, one per story. Before drafting, classify the already-agreed work using [STORY-TYPES.md](./STORY-TYPES.md): it holds the selection rules (including Model vs Agent and the branch that keeps non-behavioral work as an Implementation Decision), each kind's required core fields, and the entry format.

There are four built-in kinds: User Story (`US-###`), Data Story (`DS-###`), Model Story (`MS-###`), and Agent Story (`AS-###`). If `.agents/spec/story-types.yaml` exists, it can add kinds, take precedence over the built-ins, and narrow the built-in set; [STORY-TYPES.md](./STORY-TYPES.md) has the rules and [STORY-TYPE-TEMPLATE.yaml](./STORY-TYPE-TEMPLATE.yaml) is the template to copy. Never create a kind that is not in that file or the built-in set. Emit only the kinds the work actually uses, and never an empty section for a kind that isn't relevant. A feature can mix kinds. Architectural or refactoring specs may have few or no stories; leave this section out rather than forcing decisions into story shape.

Record a required field the conversation never settled as `Unresolved: <what is missing>`. Never invent metrics, thresholds, quantities, or actors.

<story-example>
### US-001 — See the balance

**Type:** User Story

As a mobile bank customer, I want to see balance on my accounts, so that I can make better informed decisions about my spending.
</story-example>

A spec that still has `## User Stories` reads as all `kind: user`; never rewrite historical specs.

## Behavioral Specifications

Gherkin for behavior the conversation already agreed, traced to the stories it specifies. `bdd-scenarios` is a beta skill: call the Skill tool with "bdd-scenarios" to construct the Gherkin and run its quality gate. Do not restate its rules here. If the skill is not available, leave this section out and add a line to Further Notes saying agreed behavior was not written as scenarios.

Each entry is `BS-###` (counting up per spec, never renumbered after publishing) with a **Stories:** line listing the story IDs it specifies, an optional **Audience:** line, then one fenced `gherkin` block:

- **Audience** is `customer-facing` or `developer-facing`. Omitted means customer-facing, so specs written before this line existed read unchanged. Write `**Audience:** developer-facing` when the agreed behavior is observed at an internal component's interface (a pipeline stage, model, or agent), which is typical of Data, Model and Agent stories; `bdd-scenarios` builds it in its developer-facing mode, with no invented end-user actor. A kind defined in `.agents/spec/story-types.yaml` may declare a default audience ([STORY-TYPES.md](./STORY-TYPES.md)). One entry has one audience: split when the same story has both.
- One story can have many BS entries.
- One BS entry can span several stories, of different kinds.
- A story can have no BS entry when no behavior was agreed for it.
- Emit a scenario only if it passed the gate. Where a branch or outcome was never decided, list it under `### Unresolved behavior` inside that BS entry, say what is missing, and write no `Then` for it. Never guess to complete a scenario.
- Leave the whole section out when no behavior of either audience was agreed, as with a refactor that changes no behavior, or data work whose behavior nobody agreed. Never write scenarios to fill it.

This section decides nothing. It restates agreed behavior; it does not choose where the behavior is verified (that is Testing Decisions), and it does not interview the user.

<bs-example>
### BS-001 — Detect a smartphone

**Stories:** US-001, MS-001

```gherkin
Feature: Smartphone detection

  Scenario: Flag an image containing a smartphone
    Given an image eligible for smartphone detection
    When the image contains a smartphone
    Then the system reports a smartphone detection
```

### Unresolved behavior

- The result for an image that is not eligible for detection was not decided.

### BS-002 — Skip images ineligible for detection

**Stories:** MS-001, DS-001

**Audience:** developer-facing

```gherkin
# Parent: BS-001 (the system reports smartphone detections)
Feature: Detection input filtering

  Scenario: Exclude an image below the minimum resolution
    Given an image below the minimum resolution
    When the detector receives the image
    Then the detector returns no detection result for it
```
</bs-example>

## Implementation Decisions

A list of implementation decisions that were made. This can include:

- The modules that will be built/modified
- The interfaces of those modules that will be modified
- Technical clarifications from the developer
- Architectural decisions
- Schema changes
- API contracts
- Specific interactions

Do NOT include specific file paths or code snippets. They may end up being outdated very quickly.

Exception: if a prototype produced a snippet that encodes a decision more precisely than prose can (state machine, reducer, schema, type shape), inline it within the relevant decision and note briefly that it came from a prototype. Trim to the decision-rich parts — not a working demo, just the important bits.

## Testing Decisions

A list of testing decisions that were made. Include:

- A description of what makes a good test (only test external behavior, not implementation details)
- Which modules will be tested
- For each BS entry, the agreed seam that verifies it, by ID (e.g. "Verify BS-004 through the public dataset-import boundary"). Behavioral Specifications never replace seam selection, and a BS entry is not a test
- Prior art for the tests (i.e. similar types of tests in the codebase)

## Out of Scope

A description of the things that are out of scope for this spec.

## Further Notes

Any further notes about the feature.

</spec-template>
