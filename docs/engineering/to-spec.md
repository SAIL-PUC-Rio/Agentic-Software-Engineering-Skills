## What it does

`to-spec` turns the conversation you have just had into a **spec**, and publishes it to your issue tracker as a single issue.

It does not interview you. By the time you reach for it the deciding is already done, so it synthesises what is known — from the thread, from the codebase, from your `CONTEXT.md` and ADRs — rather than opening a fresh round of questions. The spec is a record of decisions already made, not a place where new ones get made.

## When to reach for it

You invoke this by typing `/to-spec` — the agent won't reach for it on its own.

Reach for it when the build is too big for one agent session and has to survive being split across several. That is the whole trigger:

| Where you are | What to run |
| --- | --- |
| You haven't decided anything yet | [grill-with-docs](../../skills/engineering/grill-with-docs/SKILL.md) first |
| Decided, and the work fits one context window | [implement](implement.md) — skip the spec |
| Decided, and the work spans several sessions | `/to-spec`, then [to-tickets](to-tickets.md) |
| A [wayfinder](../../skills/engineering/wayfinder/SKILL.md) map has cleared | `/to-spec #<map_issue>` |

## Prerequisites

`to-spec` publishes the spec as an issue, so [setup-sail-skills](../../skills/engineering/setup-sail-skills/SKILL.md) must have configured a tracker and the triage-label vocabulary for this repo first. Either kind works: a real tracker like GitHub, or local markdown files under `.scratch/`, which is supported out of the box.

## The spec is a decision record

The spec exists because context windows end. Everything you settled while grilling — the shape of the solution, the choices you argued through, what you deliberately refused — is in one conversation that is about to be cleared. The spec is what survives that.

So it does not validate anything, and it does not decide anything. It captures what was decided, in your project's own vocabulary, so that a fresh session can pick the work up without you re-explaining it. Anything the spec asserts that you never actually said is a defect.

## Stories are typed

The spec's story section is not fixed to user stories. Before drafting it, `to-spec` sorts the work you already agreed into one of four kinds, each with its own required fields and a stable ID:

| Kind | ID | Reach for it when the work is about | Core fields |
| --- | --- | --- | --- |
| User Story | `US-###` | An actor-visible capability or workflow | actor, capability, value |
| Data Story | `DS-###` | Acquiring, preparing, or managing data or context | goal, source, data type, approximate quantity |
| Model Story | `MS-###` | Training, evaluating, or deploying a learned model | learning goal, learning type, data source, expected performance |
| Agent Story | `AS-###` | An agent built around a foundation model | agent goal, possible tasks, available artifacts, autonomy, expected performance |

Only the kinds the work uses appear, and a feature can mix them. A consumed foundation model is an Agent Story, not a Model Story: the Model kind is for when the model itself is what you build. Work that fits no kind, such as a refactor, stays an Implementation Decision instead of being forced into a story. A field you never settled is written as unresolved, not filled in.

A short ML feature, a support-ticket classifier, comes out like this:

```markdown
## Stories

### US-001 — See a suggested category

**Type:** User Story

As a support agent, I want a suggested category on each new ticket, so that I can route it faster.

### DS-001 — Labeled ticket history

**Type:** Data Story

- Goal: train and evaluate the classifier
- Source: closed tickets from the helpdesk export
- Data type: ticket text with a category label
- Approximate quantity: Unresolved: volume was never discussed

### MS-001 — Ticket classifier

**Type:** Model Story

- Learning goal: predict the ticket category from its text
- Learning type: supervised classification
- Data source: DS-001
- Expected performance: Unresolved: no accuracy target was agreed
```

Older specs with a `## User Stories` section still read as user stories and are not rewritten.

## Custom kinds

If your project needs a kind the four do not cover, define it once in `.agents/spec/story-types.yaml`. Each custom kind gets an ID prefix, a note on when to choose it, and its required fields. The same file can also narrow the built-in set, so a project with no ML work can drop Model Stories.

| Situation | What `to-spec` does |
| --- | --- |
| No file | Uses the four built-in kinds, unchanged |
| A configured kind fits a requirement | Uses it, even when a built-in would also fit |
| Work fits no configured or available kind | Leaves it as an Implementation Decision and never invents a kind |

For example, an `experiment` kind with prefix `ES` and fields hypothesis, intervention, evidence, and success condition turns "we think a shorter onboarding raises activation" into `ES-001`. Copy the [story-type template](https://github.com/Esduard/skills/blob/main/skills/engineering/to-spec/STORY-TYPE-TEMPLATE.yaml) to start a file of your own.

## Story, behavior, seam

Three layers stay separate, and each answers a different question:

| Layer | Section | Answers |
| --- | --- | --- |
| Story | `## Stories` | What work was agreed, and for whom |
| Behavior | `## Behavioral Specifications` | What can be observed when it works, by a customer or by a developer at a component's interface |
| Seam | `## Testing Decisions` | Where that behavior is verified |

Behavior is written as Gherkin, one `BS-###` entry each, with a **Stories:** line naming the story IDs it specifies and an optional **Audience:** line. An entry with no audience line is customer-facing, so older specs read unchanged. `**Audience:** developer-facing` marks behavior observed at an internal component's interface, typical of Data, Model and Agent stories, and it is written with no invented end-user actor. A refactor that changes no behavior can carry `**Kind:** regression` entries: developer-facing scenarios that pin the existing module's observed behavior, built from its cited code and tests, with no story forced on them. Testing Decisions then states that the existing suite passes before and after and names the seam for each one. A project-defined kind can declare a default audience in `story-types.yaml`. One story can have several entries, one entry can span several stories (a User Story and a Model Story, say), and a story with no agreed behavior has none. The Gherkin is built with the [bdd-scenarios](https://github.com/Esduard/skills/tree/main/skills/in-progress/bdd-scenarios) skill, a beta skill that ships outside the plugin, and only scenarios that pass its quality gate are emitted.

Behavior nobody decided is not filled in. A branch or outcome the conversation never settled goes under an `Unresolved behavior` note in that entry, with no `Then` invented for it. If no behavior of either audience was agreed, as in a refactor that changes nothing or data work whose behavior nobody settled, the section is left out. If `bdd-scenarios` is not installed, the section is left out too and Further Notes says so.

A behavior entry never picks its own seam. Testing Decisions names the agreed seam that verifies each one by ID:

````markdown
## Behavioral Specifications

### BS-001 — Detect a smartphone

**Stories:** US-001, MS-001

```gherkin
Feature: Smartphone detection

  Scenario: Flag an image containing a smartphone
    Given an image eligible for smartphone detection
    When the image contains a smartphone
    Then the system reports a smartphone detection
```

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

## Testing Decisions

- Verify BS-001 through the public detection endpoint, not the model internals.
- Verify BS-002 at the detector's own interface.
````

## Seams before prose

Before it writes a word, `to-spec` sketches the **seams** the feature will be tested at, and checks them with you. It prefers seams that already exist to new ones, and takes the highest seam it can — the ideal number across a change is one.

Those agreed seams then travel. [tdd](../../skills/engineering/tdd/SKILL.md) works only at pre-agreed seams, and [code-review](code-review.md) reviews the diff against the spec, so a seam nobody agreed to shows up as a review finding. The binding is indirect — it runs through this document — which is exactly why the seam conversation is worth taking seriously here rather than deferring it to implementation.

## Common questions

**Where did `/to-prd` go?**
It is this skill, renamed in v1.1. "Spec" is now the single through-line term, and the old `to-prd` slug is dead — reinstall under the new name. The pair that replaced the old vocabulary is *spec* and *tickets*: the spec is the destination and the decisions that fix it, the tickets are the execution steps that get there. If you pivot, delete the unfinished tickets and keep the spec.

**Why does the spec get the `ready-for-agent` label? I don't want an agent implementing off it.**
The label means "no further triage needed" — the document is complete enough for an agent to work from. It is an input designation, not a work order. But if you run AFK agents that poll for `ready-for-agent`, that distinction isn't visible to them, and they will happily try to build the whole spec in one run instead of picking up the ticket slices. This is the most-reported rough edge on the skill. Until it changes, exclude the parent spec explicitly in your AFK agent's prompt, or strip the label once `/to-tickets` has run.

**Why not go straight from grilling to `/to-tickets` and skip the spec?**
Often you should — the spec earns its step only on multi-session work. Where it pays is that the tickets are disposable and the spec isn't: each ticket is sized for one fresh context window and gets deleted or closed, while the spec stays as the one place the reasoning behind them lives. On a single-session change that buys you nothing, and you have paid an extra synthesis step where the model can drift. Go grilling → `/implement`.

**I just finished a wayfinder map. What do I feed it?**
The main map issue — `/to-spec #<map_issue>`, not the individual decision tickets. [wayfinder](../../skills/engineering/wayfinder/SKILL.md) produces decisions rather than deliverables, scattered across a map; `to-spec` is the step that collapses them into one buildable document. Looping the map straight into `/implement` throws that collapse away.

**Is the spec for me to review, or is it just for the agent?**
Mostly for the agent, and it reads that way — complete, dense, reference-heavy. The parts worth your eyes are the seams and the out-of-scope section, because those are the two places a wrong decision is cheapest to catch and most expensive to discover later. Reading the whole thing end to end is a real complaint people have, and there is no summary mode: the honest answer is that if the spec surprises you, the grilling was too shallow, not the spec too long.

**Do I keep the spec frozen once tickets start, or let the agent rewrite it?**
Nothing keeps it in sync, so in practice it is a snapshot of what you knew at that moment, and it goes stale the first time implementation teaches you something. Treat it as throwaway once the work ships. The artifacts meant to outlive it are your `CONTEXT.md` and your ADRs — if something learned during implementation deserves to last, it belongs there, not in an edited spec.

**My work is a refactor or a module boundary, not a feature. Does the template fit?**
Better than it used to. Stories are optional now, so a refactor can have few or none, and with no behavior change it gets no agreed-behavior Behavioral Specifications, though it can carry `**Kind:** regression` entries that pin the current behavior so the refactor can be checked against it. The spec rests on its implementation decisions and testing decisions. Let the durable architectural calls land as ADRs via [grill-with-docs](../../skills/engineering/grill-with-docs/SKILL.md) rather than trying to make the spec carry them.

**Will it check the tracker for related work, or cite the ADRs it's respecting?**
No to both. It reads and respects the ADRs covering the area it touches, but it doesn't link them, and it doesn't search the tracker for overlapping issues before drafting — so a spec can quietly duplicate work someone already filed. Search the tracker yourself first if the area is busy.

**`/to-tickets` couldn't read my spec — it kept truncating.**
Very large specs can outgrow what a tracker issue will serve back cleanly, and there is no local copy to fall back on. The fix is context hygiene: don't clear or compact between `/to-spec` and `/to-tickets`. Run them in the same window and the spec never has to be re-fetched at all.

## It's working if

- It starts writing rather than asking you a fresh round of questions.
- It puts the seams to you before it writes, and proposes as few as it can get away with.
- It comes back in your project's nouns, not generic product-management boilerplate.
- Every decision in it is one you can remember making. Nothing was invented to fill a section.
- Stories carry a type and an ID, only for kinds your work uses, and a gap in your decisions shows as "Unresolved" rather than a made-up number.
- Behavior you agreed shows up as `BS-###` Gherkin tied to story IDs, with developer-facing entries marked as such, and behavior you left open shows up as unresolved, never as a guessed outcome.
- Each `BS-###` is named in Testing Decisions with the seam that verifies it, and a refactor's regression entries come with the before-and-after suite line.
- The out-of-scope section has real things in it — the things you refused are usually the most useful lines on the page.

## Where it fits

`to-spec` is a step in the main build chain, and only on the multi-session branch of it:

```txt
grill-with-docs → to-spec → to-tickets → implement → code-review
```

Its neighbours upstream are [grill-with-docs](../../skills/engineering/grill-with-docs/SKILL.md), which does the deciding this skill only records, and [wayfinder](../../skills/engineering/wayfinder/SKILL.md), whose finished map merges onto the chain right here. Downstream, [to-tickets](to-tickets.md) cuts the spec into tracer-bullet tickets for [implement](implement.md) to build. When you're unsure which skill or flow fits, [ask-sail](../../skills/engineering/ask-sail/SKILL.md) routes you.
