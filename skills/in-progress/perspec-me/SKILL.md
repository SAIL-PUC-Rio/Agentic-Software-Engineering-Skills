---
name: perspec-me
description: Resolve one project question through a PerSpecML concern-guided interview — select the relevant Concerns from the catalog, gather evidence, interview the user in short rounds, and persist the answer into per-Concern Resolution pages for that Topic. Use when the user runs `/perspec-me <question>`, asks to work through a Topic with PerSpecML's Concerns and Perspectives, or another skill routes a `resolver: perspec-me` call.
---

# perspec-me

`perspec-me` is a catalog-driven interview that resolves one **Topic** at a time using **Concern** lenses from the PerSpecML catalog shipped in `skills/in-progress/perspec-me/catalog/`, and rolls the result into a durable **Map** toward an agreed **Destination**. This `SKILL.md` is the single entry point for both a human typing `/perspec-me` and another skill routing a `resolver: perspec-me` call (see `docs/adr/0001-one-model-invoked-skill-thin-routing-section.md`) — there is no separate thin command file.

Read `CONTEXT.md` before anything else. It defines Concern, Topic, Session, Map, Destination, Fog, Frontier, Blocked, Resolution page, Perspective coverage, Delegated work, and the seven Concern states, and this skill's prose uses those terms exactly as defined there — never a synonym.

This `SKILL.md` holds the routing section and the direct-session procedure. Two companion files hold what would otherwise make it unwieldy: [map.md](./map.md) is the map-charting procedure (fit-in-one-session decision, Destination, Fog, Topics, Frontier, and the Map file's structure) and [local-backend.md](./local-backend.md) is the local Markdown topic-store's five operations (create topic, claim, list frontier, record resolution, wire blockers — ADR 0002's seam, this backend's mechanics). Both are referenced from here rather than duplicated.

## Routing

The input to `perspec-me` is either a bare **seed** (a question, idea, or short text with no recognized verb) or one of the verbs below.

- **Bare `<seed>`** — first runs the **fit-in-one-session decision** in [map.md](./map.md#fit-in-one-session-decision): read the seed, inspect the repo breadth-first, take a low-resolution pass over the catalog, and estimate how many independent decisions remain. Say the outcome plainly, then:
  - **Fits one session** — no Map, no Frontier, no topic store involved. Run the **direct-session procedure** below, in full, on its own.
  - **Needs a Map** — hand off to the **map-charting procedure** in [map.md](./map.md). Greenfield and issue seeds are not different modes; any seed that fails the fit decision is charted the same way.
- **`map <effort-or-destination>`** — the user has already decided this needs a Map; skip the fit decision and run the map-charting procedure in [map.md](./map.md) directly, starting from the Destination step.
- **`resolve <topic-ref>`**, **`resume [session-or-map]`**, **`status [map]`**, **`review <concern-id>`** — operate against an existing Map. **Not implemented in this ticket** — see issue #16.

If the user invokes one of the not-yet-implemented verbs, say so plainly and name the issue that adds it. Do not silently fall through to the direct-session procedure for them, and do not fake Map/Frontier/Resolution-page behavior that isn't built yet.

## The direct-session procedure

This is the only procedure this ticket implements end to end: a bare seed with no existing Map, resolved in one bounded Session.

### a. Load the catalog by progressive disclosure

Never read all 60 Concern definitions. Walk the catalog top-down and stop loading as soon as you have enough:

1. Read `catalog/README.md` (the root index) to see the five Perspectives (O — System Objectives, U — User Experience, I — Infrastructure, M — Model, D — Data) and pick the one or two whose scope plausibly covers the question.
2. Read only those Perspectives' `catalog/perspectives/<perspective-slug>/README.md` files. Each lists its tasks, recommended stakeholders, and links to its own Concerns — use this to narrow further, not `catalog/concerns/README.md`'s full flat list.
3. Open only the Concern folders that plausibly bear on the question (typically 2-5 across the chosen Perspective(s)) — their `README.md`, then `definition.md`, then `relationships.md`/`elicitation.md` if present, for that concern.

A Concern's ID and canonical link look like `M5 — Performance metrics` → `skills/in-progress/perspec-me/catalog/concerns/m5-performance-metrics/README.md`; a Perspective's like `M — Model` → `skills/in-progress/perspec-me/catalog/perspectives/model/README.md`.

### b. Investigate

Before interviewing, look for evidence already in the repo and its docs that bears on the question — existing decisions, code, config, CONTEXT.md/ADR entries, prior Resolution pages for the same Concerns (see step d). Bring what you find into the round instead of asking the user to restate what's already on record.

### c. Run interview rounds

Each round has exactly these six parts, in this order, and nothing else:

1. **Current understanding** — 2 to 5 lines summarizing where the Topic stands so far.
2. **The question being resolved** — stated plainly, this round's focus.
3. **The Concerns used as lenses** — each named and linked into the catalog (e.g. `[M5 — Performance metrics](../../../skills/in-progress/perspec-me/catalog/concerns/m5-performance-metrics/)`, path relative to the consuming project).
4. **Evidence found** — what step (b) turned up, or "none found" if nothing did.
5. **A recommendation** — with rationale, and the main trade-off when one exists.
6. **One to three related questions** — for the human to react to or answer directly.

After part 6, the skill explicitly **stops and waits** for the human's real answer. Never simulate, invent, or guess the user's answer to move the round forward — a round with no real answer stays open.

### d. Persist after every answer

After **every** answer — not batched at the end — extract from it:

- confirmed facts,
- open hypotheses,
- decisions, and
- derived requirements or constraints,

and write them into the Resolution page(s) of the Concern(s) that answer touches, under the project's resolution layer.

**Resolution-layer path convention for a direct session (no Map yet):** `requirements/perspec-me/_unmapped/concerns/<concern-id>.md`, e.g. `requirements/perspec-me/_unmapped/concerns/m5-performance-metrics.md`. There is no map-slug yet for a mapless direct session, so this ticket uses a fixed `_unmapped` bucket rather than a per-topic-slug directory — a later topic that touches the same Concern lands in the same file regardless of which seed started it, which is exactly the "append, don't fork" behavior required below. Once a real Map exists (`<map-slug>`, [map.md](./map.md)), the convention becomes `requirements/perspec-me/<map-slug>/concerns/<concern-id>.md` per ADR 0003 — see [map.md](./map.md#resolution-layer-convention-once-a-map-exists) for that convention and the explicit note that migrating pre-existing `_unmapped/` content into a newly-charted Map is out of scope here.

A Resolution page is created **only the first time** its Concern is touched. A later Session or a later Topic touching the same Concern **appends to / updates this same file's synthesis** — it never overwrites the whole file, and it never discards an earlier, unrelated decision already recorded there.

**Resolution page template:**

```markdown
---
concern_id: m5-performance-metrics
concern: <link to the canonical catalog page, e.g. skills/in-progress/perspec-me/catalog/concerns/m5-performance-metrics/README.md>
perspective: model
status: partial
topics:
  - <topic-slug-1>
  - <topic-slug-2>
updated_at: <ISO date>
---

## Current resolution

<This project's current synthesis for this Concern — never the catalog's generic description.>

## Confirmed facts

- ...

## Decisions

- ...

## Derived requirements and constraints

- ...

## Open questions

- ...

## Evidence

- ...

## Topic history

- <topic-slug-1>: <one line on what this topic settled or changed here>
- <topic-slug-2>: <one line>
```

`status` is one of the seven states from `CONTEXT.md`, verbatim: `unexamined`, `open`, `partial`, `resolved`, `deferred`, `not-applicable`, `superseded`. **Hard rule: `not-applicable` must always carry its justification** in "Current resolution" — never set it bare.

### e. Closure

The Topic closes when: its question has a clear enough answer, the decisions and affected Concerns are recorded, derived requirements/constraints are captured, and the user agrees the Topic is settled. Closing a Topic ends the Session with a short synthesis (what was decided, which Concerns/Resolution pages were touched) and explicitly **does not begin implementation** — that is a later, separate step outside this skill.

## Hard rule: the catalog is read-only

This skill must **never** write to `skills/in-progress/perspec-me/catalog/`. It is immutable reference material (see the catalog's own `NOTE.md` and `docs/adr/0003-catalog-read-only-resolution-layer-in-project.md`) — every write this skill makes goes into the consuming project's `requirements/perspec-me/` resolution layer, never into the skill folder itself.

Verify this after every session: run

```sh
git status --porcelain skills/in-progress/perspec-me/catalog/
```

before and after the session and confirm the output is empty both times (or compare a checksum, e.g. `find skills/in-progress/perspec-me/catalog -type f | sort | xargs sha256sum | sha256sum`, taken before and after). Any diff is a bug in this skill, not an acceptable side effect.

## Smoke tests

These are manual test recipes to run against a real (or throwaway) consuming project — not automated test code, since this is a prompt-driven skill.

### Direct-session smoke tests

1. **Small direct topic, end to end.** Pick a narrow question (e.g. "How will the credit model be evaluated before launch?"). Run the direct-session procedure through catalog load → evidence → at least one round → a real (human-typed) answer → persistence → closure. Expect: one or more Resolution pages created under `requirements/perspec-me/_unmapped/concerns/`, each following the template, and a closing synthesis that does not start implementation.
2. **One topic, several concerns at once.** Pick a question broad enough to plausibly touch 3+ Concerns in one round (e.g. the same credit-model question above touches M5, M6, D16, and O8). Expect: one round names all the relevant Concerns as lenses, and after the answer, a separate Resolution page exists per touched Concern.
3. **A concern left `partial`.** Run a topic where the user's answer resolves only part of a Concern's territory. Expect: that Concern's Resolution page is written with `status: partial` and an "Open questions" entry describing what's still unresolved — not forced to `resolved`.
4. **Two topics touching the same concern.** Run one topic to closure touching Concern X, then start a second, unrelated topic that also touches Concern X. Expect: Concern X's Resolution page still has the first topic's decisions in "Decisions" untouched, the second topic's slug is appended to `topics` and "Topic history", and "Current resolution" is updated to reflect both — the file is never replaced wholesale.
5. **Catalog unchanged.** Before and after every one of the smoke tests above, run `git status --porcelain skills/in-progress/perspec-me/catalog/` (or the checksum command above). Expect: empty output / identical checksum every time.

### Map-charting smoke tests

1. **Greenfield map.** Feed a seed that clearly spans several Perspectives and independent decisions (e.g. "we want to add a recommendation feature that suggests products based on browsing history"). Expect: the fit-in-one-session decision states "needs a Map" with a reason, a `MAP.md` is created under `requirements/perspec-me/<map-slug>/` with a proposed Destination, and charting produces at least one Topic file and at least one Fog entry before stopping to report.
2. **Destination-before-topics.** On the same seed, check the sequence of writes: the Destination sentence must be proposed and the skill must explicitly wait for the user's confirmation before **create topic** runs even once. Expect: no file exists under `requirements/perspec-me/<map-slug>/topics/` until after a confirmation turn; if the user pushes back on the wording, the Map's Destination section is updated to their wording before any Topic is created. See the dry run below.
3. **Fog identified.** During the greenfield charting pass, expect at least one region that's clearly relevant (named in a Perspective's task list) but not yet phraseable as a precise question to land in the Map's Fog section, not as a Topic file and not omitted.
4. **Frontier built.** After charting produces 2+ Topics where one is wired as `blocked_by` the other (via **wire blockers**), run **list frontier** by hand over the real topic files. Expect: only the unblocked, unclaimed, open Topic appears; the blocked one appears in the Map's Blocked section instead; regenerating the Map's Frontier section after resolving the blocker moves the previously-blocked Topic into it without any hand edit.
5. **Too-small-for-a-map fallthrough.** Feed a seed that's a single, narrow question confined to one Perspective (e.g. the credit-model evaluation question from direct-session smoke test 1). Expect: the fit-in-one-session decision states "fits one session" with a reason, no `MAP.md` or `topics/` directory is created, and the direct-session procedure runs exactly as it does today.

**Dry run — destination-before-topics gate.** Traced by hand against a throwaway example rather than a live user: seed = "we want to add a recommendation feature to our e-commerce app that suggests products to users based on browsing history." Fit decision: touches O (why recommend at all — profit hypothesis), U (how suggestions surface to the shopper), M (ranking approach), D (what browsing-history data is available and how clean it is), and I (serving latency) — five Perspectives, several independently-answerable questions (which signals feed the ranker vs. what latency budget vs. how success is measured are not the same decision and could land with different owners on different timelines) → **needs a Map**, not one session. Proposed Destination: "the recommendation feature's requirements are clear enough to become implementation tickets: input signals, ranking approach, serving latency budget, and success metric are all decided." At that point the structural check is: has any file under `topics/` been written yet? No — the only file that may exist is `MAP.md` with Destination filled in and every other section still empty/pending. Only after a real confirmation turn (the user agreeing to that sentence, or handing back a reworded one, e.g. narrowing it to exclude cold-start users explicitly) does the first `create topic` run. This confirms the gate is structural and checkable (file existence under `topics/`), not just a good intention stated in prose — and that it does not depend on fabricating what the user would say, only on withholding the write until they actually do.
