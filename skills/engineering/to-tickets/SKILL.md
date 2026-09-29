---
name: to-tickets
description: Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring its blocking edges, published to the configured tracker — edges as text in one file per ticket locally, or native blocking links on a real tracker.
disable-model-invocation: true
---

# To Tickets

Break a plan, spec, or conversation into a set of **tickets** — tracer-bullet vertical slices, each declaring the tickets that **block** it.

The issue tracker and triage label vocabulary should have been provided to you. If not, tell the user to run `/setup-matt-pocock-skills`.

## Process

### 1. Gather context

Work from whatever is already in the conversation context. If the user passes a reference (a spec path, an issue number or URL) as an argument, fetch it and read its full body and comments.

### 2. Explore the codebase (optional)

If you have not already explored the codebase, do so to understand the current state of the code. Ticket titles and descriptions should use the project's domain glossary vocabulary, and respect ADRs in the area you're touching.

Look for opportunities to prefactor the code to make the implementation easier. "Make the change easy, then make the easy change."

If the source spec has `## Stories` and/or `## Behavioral Specifications`, note each story ID (`US-###`, `DS-###`, `MS-###`, `AS-###`, or a project-defined prefix) and each `BS-###` entry, with the **Stories:** line linking them. These IDs are the trace the tickets carry forward. Treat a story as an ID, a title, and its fields; never parse or depend on its wording, whatever its kind — a story may be prose in any shape. A legacy spec with `## User Stories` has no IDs: number its items yourself as `US-001`... in listed order only for your working notes and cite them in tickets by their quoted title. A spec with neither section has nothing to cite; skip the trace lines below rather than inventing IDs.

### 3. Draft vertical slices

Break the work into **tracer bullet** tickets, then check the boundaries between them for **orthogonality**. The two are complementary, not redundant: tracer bullets buy completeness *within* a ticket — each slice is a whole vertical path through every layer — while orthogonality buys independence *between* tickets — no ticket's boundary leaks into its neighbours'.

<vertical-slice-rules>

- Each slice cuts a narrow but COMPLETE path through every layer (schema, API, UI, tests) — vertical, NOT a horizontal slice of one layer
- A completed slice is demoable or verifiable on its own
- Each slice is sized to fit in a single fresh context window
- Any prefactoring should be done first

</vertical-slice-rules>

When the spec has IDs, assign every ticket the stories it delivers and the BS entries it makes pass. Every BS entry should land in at least one ticket; a BS entry that spans several tickets is a signal to check the boundary. Copy unresolved points (`### Unresolved behavior`) into the ticket as open questions, not as scenarios. Never write a scenario of your own — behavior the spec never specified stays an ordinary acceptance criterion.

Give each ticket its **blocking edges** — the other tickets that must complete before it can start. A ticket with no blockers can start immediately.

<orthogonality-rules>

Apply this test to every proposed ticket: **"If the requirement behind this ticket changed substantially, which other tickets would also have to change?"** The ideal answer is "none" — though some dependencies are intrinsic to the problem and can't be designed away.

Orthogonality means independence of **behavioral responsibility**, not separation by file, module, or layer — two tickets may legitimately touch the same files. What matters is whether changing one ticket's requirement forces a change in another ticket's requirement, not whether their diffs overlap.

When the test fails — when several tickets would have to change together — reconsider the boundary rather than accepting it: merge the overlapping slices into one ticket, redefine what each ticket is responsible for, or prefactor an explicit interface between them before the dependent work starts (see step 2, "Explore the codebase").

Blocking edges must represent genuine prerequisites — one ticket's output is actually required as another's input — never a substitute for a clean boundary. If a "blocks" edge exists mainly to paper over two tickets sharing responsibility, that's a signal to redraw the boundary, not to add the edge.

A dense, highly-connected dependency graph is a **decomposition smell**: it usually means responsibilities are overlapping rather than orthogonal, and the tickets should be reconsidered — not accepted as the shape of the work.

</orthogonality-rules>

**Wide refactors are the exception to vertical slicing.** A **wide refactor** is one mechanical change — rename a column, retype a shared symbol — whose **blast radius** fans across the whole codebase, so a single edit breaks thousands of call sites at once and no vertical slice can land green. Don't force it into a tracer bullet; sequence it as **expand–contract**. First expand: add the new form beside the old so nothing breaks. Then migrate the call sites over in batches sized by blast radius (per package, per directory), each batch its own ticket blocked by the expand, keeping CI green batch to batch because the old form still exists. Finally contract: delete the old form once no caller remains, in a ticket blocked by every migrate batch. When even the batches can't stay green alone, keep the sequence but let them share an integration branch that all block a final integrate-and-verify ticket — green is promised only there. This sequence is exempt from the orthogonality test above: expand, migrate, and contract batches are intentionally chained by design, so their blocking edges stay genuine prerequisites rather than the decomposition smell the test warns against.

### 4. Quiz the user

Present the proposed breakdown as a numbered list. For each ticket, show:

- **Title**: short descriptive name
- **Blocked by**: which other tickets (if any) must complete first
- **What it delivers**: the end-to-end behaviour this ticket makes work
- **Traces**: the story and BS IDs it delivers (only when the spec has them)

Immediately after the list, render the dependency graph — don't hand-draw it, don't re-derive it, don't reason about layout yourself. Serialize the same tickets used for the list above as the canonical `{id, title, blocked_by}` JSON (`id` is each ticket's number, `blocked_by` is the list of blocking tickets' `id`s) and pipe it via stdin to the graph script bundled with this skill:

```bash
python3 scripts/dependency_graph.py --format both
```

**Validation gate:** if the script exits non-zero — a cycle or an unknown/invalid `blocked_by` reference reported on stderr — do not show that output to the user. Fix the decomposition that produced the error (the offending blocking edges or ticket boundaries) and rerun the script before proceeding. Never present an unvalidated or errored graph.

Once the script exits cleanly, include its output inline in your response, in this order: the terminal diagram first, the Mermaid source after as a secondary/complementary block.

Then apply the orthogonality diagnostic from step 3's `<orthogonality-rules>` above to the rendered graph — the change-impact test and the decomposition-smell check — looking at what the graph makes visible: unexpected chains, tickets that seem unrelated but end up coupled, suspicious density, or a missing prefactor boundary. Don't restate that guidance here; apply it to what the script just rendered.

Ask the user:

- Does the granularity feel right? (too coarse / too fine)
- Are the blocking edges correct — does each ticket only depend on tickets that genuinely gate it?
- Should any tickets be merged or split further?

Iterate until the user approves the breakdown. If the breakdown changes, re-serialize and rerun the graph script — the graph shown to the user must always match the current proposal.

### 5. Publish the tickets to the configured tracker

Publish the approved tickets. **How** depends on the tracker `/setup-matt-pocock-skills` configured — the tickets are the same either way, only the shape of the blocking edges changes:

- **Local files** → write one file per ticket under `.scratch/<feature-slug>/issues/<NN>-<slug>.md`, numbered from `01` in dependency order (blockers first). Each file's "Blocked by" lists the numbers/titles it depends on. Use the per-ticket file template below — one ticket per file, never a single combined file.
- **A real issue tracker (GitHub, Linear, …)** → publish one issue per ticket in dependency order (blockers first) so each ticket's blocking edges can reference real identifiers. Use the platform's native blocking / sub-issue relationship where it has one; otherwise set each ticket's "Blocked by" to the blocking issues. Apply the `ready-for-agent` triage label unless instructed otherwise — the tickets are agent-grabbable by construction.

Work the **frontier**: any ticket whose blockers are all done. For a purely linear chain that means top to bottom.

Do NOT close or modify any parent issue.

<local-ticket-template>

# <NN> — <Ticket title>

**What to build:** the end-to-end behaviour this ticket makes work, from the user's perspective — not a layer-by-layer implementation list.

**Blocked by:** the numbers/titles of the tickets that gate this one, or "None — can start immediately".

**Status:** ready-for-agent

**Stories:** `US-001`, `MS-002` — IDs with their titles. Omit when the spec has no story IDs.

**Behavior:** `BS-003`, `BS-004` — followed by each named scenario's Gherkin, copied verbatim from the spec, so the ticket is self-contained. Omit when the spec has no BS entries.

- [ ] Acceptance criterion 1
- [ ] Acceptance criterion 2

</local-ticket-template>

<issue-template>

## Parent

A reference to the parent issue on the tracker (if the source was an existing issue, otherwise omit this section).

## What to build

The end-to-end behaviour this ticket makes work, from the user's perspective — not layer-by-layer implementation.

## Stories

Story IDs with titles this ticket delivers. Omit when the spec has no story IDs.

## Behavior

The BS IDs this ticket makes pass, each followed by its Gherkin copied verbatim from the spec, so the ticket is self-contained. Omit when the spec has no BS entries.

## Acceptance criteria

- [ ] Criterion 1
- [ ] Criterion 2

## Blocked by

- A reference to each blocking ticket, or "None — can start immediately".

</issue-template>

In either form, cited BS scenarios are copied, never reworded, and acceptance criteria add to them rather than restating them. Avoid specific file paths or code snippets — they go stale fast. Exception: if a prototype produced a snippet that encodes a decision more precisely than prose can (state machine, reducer, schema, type shape), inline it and note briefly that it came from a prototype. Trim to the decision-rich parts — not a working demo, just the important bits.
