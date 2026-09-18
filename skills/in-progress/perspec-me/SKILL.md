---
name: perspec-me
description: Resolve one project question through a PerSpecML concern-guided interview — select the relevant Concerns from the catalog, gather evidence, interview the user in short rounds, and persist the answer into per-Concern Resolution pages for that Topic. Use when the user runs `/perspec-me <question>`, asks to work through a Topic with PerSpecML's Concerns and Perspectives, or another skill routes a `resolver: perspec-me` call.
---

# perspec-me

`perspec-me` is a catalog-driven interview that resolves one **Topic** at a time using **Concern** lenses from the PerSpecML catalog shipped in `skills/in-progress/perspec-me/catalog/`, and rolls the result into a durable **Map** toward an agreed **Destination**. This `SKILL.md` is the single entry point for both a human typing `/perspec-me` and another skill routing a `resolver: perspec-me` call (see `docs/adr/0001-one-model-invoked-skill-thin-routing-section.md`) — there is no separate thin command file.

Read `CONTEXT.md` before anything else. It defines Concern, Topic, Session, Map, Destination, Fog, Frontier, Blocked, Resolution page, Perspective coverage, Delegated work, and the seven Concern states, and this skill's prose uses those terms exactly as defined there — never a synonym.

This `SKILL.md` holds the routing section and the direct-session procedure. Three companion files hold what would otherwise make it unwieldy: [map.md](./map.md) is the map-charting procedure (fit-in-one-session decision, Destination, Fog, Topics, Frontier, and the Map file's structure), [local-backend.md](./local-backend.md) is the local Markdown topic-store's five operations (create topic, claim, list frontier, record resolution, wire blockers — ADR 0002's seam, this backend's mechanics), and [work-a-map.md](./work-a-map.md) is the procedure for working an existing Map across sessions (`resolve`, `resume`, `status`, `review`). All three are referenced from here rather than duplicated.

## Routing

The input to `perspec-me` is either a bare **seed** (a question, idea, or short text with no recognized verb) or one of the verbs below.

- **Bare `<seed>`** — first runs the **fit-in-one-session decision** in [map.md](./map.md#fit-in-one-session-decision): read the seed, inspect the repo breadth-first, take a low-resolution pass over the catalog, and estimate how many independent decisions remain. Say the outcome plainly, then:
  - **Fits one session** — no Map, no Frontier, no topic store involved. Run the **direct-session procedure** below, in full, on its own.
  - **Needs a Map** — hand off to the **map-charting procedure** in [map.md](./map.md). Greenfield and issue seeds are not different modes; any seed that fails the fit decision is charted the same way.
- **`map <effort-or-destination>`** — the user has already decided this needs a Map; skip the fit decision and run the map-charting procedure in [map.md](./map.md) directly, starting from the Destination step.
- **`resolve <topic-ref>`**, **`resume [session-or-map]`**, **`status [map]`**, **`review <concern-id>`** — operate against an existing Map. Dispatch to the matching procedure in [work-a-map.md](./work-a-map.md): `resolve` claims a Topic (named, or the first Frontier entry) and runs the interview against it; `resume` picks the Topic this session already claimed and continues it; `status` prints the Map's own sections; `review` opens one Concern's Resolution page. None of these chart a Map or create its first Topics — that's still `map <effort-or-destination>` above.

If the user invokes one of these verbs against a project with no Map yet (no `requirements/perspec-me/<map-slug>/MAP.md`), say so plainly and point at `map <effort-or-destination>` instead of faking Map/Frontier/Resolution-page behavior that has nothing to operate on.

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

### Work-a-map smoke tests

Verbs in [work-a-map.md](./work-a-map.md), run against an already-charted Map (see [map.md](./map.md) for how it got there).

1. **Fog graduates to a topic.** Mid-`resolve` on an open Topic, surface a question that matches an existing Fog entry closely enough to become precise. Expect: the Fog entry disappears from the Map's Fog section and a new Topic file appears under `topics/` in the same edit — never both present at once, even briefly.
2. **Topic completion updates the map.** Close a Topic that another open Topic names in its `blocked_by`. Expect, in one pass: the Map's Decisions so far gains one line naming the closed Topic and its touched Concern(s); the Map's rendered Frontier section drops the closed Topic and picks up the now-unblocked one, and Blocked shrinks accordingly; the Perspective resolution coverage table's row for the touched Concern's Perspective changes count.
3. **Resume without loading history.** Claim a Topic, answer enough of it to leave one Concern Resolution page `partial` with a stated open question, end the session, then run `resume` (a fresh conversation, session identifier supplied explicitly). Expect: the resumed session states the Destination and the last few Decisions-so-far lines (not the full history), finds the claimed Topic by scanning `claimed_by` rather than asking the user which one, loads only that Topic's own Concern(s), and picks up at the Resolution page's stated open question — it does not re-ask the already-confirmed part, does not open any resolved Topic's file, and does not open any other Concern's Resolution page.
4. **A claim blocks a second concurrent session on the same topic.** With Topic X claimed by session A, have session B attempt `resolve X` directly, and separately attempt `resolve` on an unclaimed Topic Y that shares a Concern with X. Expect both refused: the first because `claim`'s refusal rule fires on X's `claimed_by` belonging to a different open claim; the second because the concurrency check finds X (open, claimed by another session) overlapping Y on a shared Concern ID — both refusals name the conflicting Topic and the reason, and neither performs a write.
5. **An oversized topic splits.** Mid-`resolve` on a claimed Topic touching several Concerns, surface the split signal (`work-a-map.md`'s Alternative outcomes → Split: the current-understanding-can't-be-stated-in-2-5-lines or several-genuinely-independent-sub-questions test), propose the split, and have the user confirm it. Expect, in one pass: a short synthesis is written into the original Topic's own Notes before anything else; 2 or more new Topic files are created via **create topic**, each phrased as a question, none of them created one-per-Concern; any apparent dependency between the new Topics is wired via **wire blockers**; the original Topic is never passed to **record resolution** (no `resolved_at`) and instead gets a `children:` list naming the new Topics' slugs, with `status` staying `open`; and the session ends there — no further round runs against the original Topic. Then run **list frontier** by hand over the resulting `topics/` directory: expect every unblocked new Topic to appear, any blocked one to be absent (present in Blocked instead), and the aggregator Topic to appear in neither — its `claimed_by` is still set from before the split, which is what `list frontier`'s third condition already excludes, with no special case needed for `children`.
6. **A blocking research (or prototype) entry is created.** Mid-`resolve` on a claimed Topic, surface a question that fits Research (e.g. "what p99 latency budget does the platform's own SLA docs actually mandate?" — an external fact, not something interviewing the user can settle) per [work-a-map.md](./work-a-map.md#delegated-work)'s classification. Expect, in one pass: a `dw-<slug>` entry appears in the Map's Delegated work section with `type: research`, the surfaced `question`, `blocks: <topic-slug>`, and `status: pending`; the Topic's `blocked_by` gains a `dw:<id>` entry via **wire blockers**; the Topic's `claimed_by` is cleared in the same edit (the one named exception to "claimed_by is never cleared once set," [local-backend.md](./local-backend.md#claim)); and running **list frontier** afterward shows the Topic in Blocked (named by the `dw-<id>`, not by another Topic) and dropped from the Frontier, with no hand-edit to a "Blocked list" anywhere. The same trace holds for a Prototype entry, substituting the classification reason (conversation can't decide a look/behavior question) and `type: prototype`.
7. **Concern pages are updated after the delegated result returns.** Starting from the Blocked state test 6 produced, resolve the `dw-<id>` entry per [work-a-map.md](./work-a-map.md#when-a-delegated-result-returns): set `status: resolved`, `resolved_at`, and fill in `result.answer`/`evidence`/`sources`/`affected_concerns`/`new_topics`. Expect, in one pass: each Concern ID in `affected_concerns` gets its Resolution page's **Evidence** section appended with the delegated work's evidence/sources and its **Topic history** noted with the `dw-<id>` that contributed (create-once/append-after, `SKILL.md` section d — never a wholesale overwrite); any `new_topics` entries go through the same New-question classification as any other newly discovered question (a real Topic via **create topic**, Fog, or Out of scope — never a separate scheme); and running **list frontier** again shows the Topic back on the Frontier with no edit to its `blocked_by` list — only the `dw-<id>`'s own `status` changed.

**Dry run — traced against a constructed example Map.** Built a throwaway `MAP.md` plus Topic files `topic-a` ("Which retrain cadence should the ranker use?", concern `m5-performance-metrics`, unblocked), `topic-b` ("What should the golden dataset contain?", concern `d16-golden-dataset`, `blocked_by: [topic-a]`), and `topic-c` ("Should the ranker's evaluation metric be NDCG or MAP@k?", also concern `m5-performance-metrics`, unblocked) under a scratch `requirements/perspec-me/example-map/` tree (outside the skill repo, not committed), plus one Fog entry ("Latency modeling approach"). Traced by hand, no live user:

- Session `s1-2026-09-18` runs `resolve` with no topic named → **list frontier** returns only `topic-a` (`topic-b` fails the blocked-by check, `topic-c` would also qualify but isn't first) → claims `topic-a`.
- Session `s2-2026-09-18` tries `resolve topic-a` → refused: `topic-a`'s `claimed_by` is `s1-2026-09-18`, a different open claim → **claim**'s refusal rule fires, no write happens. Separately, `s2` tries `resolve topic-c` (itself unclaimed) → refused too: the concurrency check finds `topic-a` open and claimed by another session, and `topic-c` shares Concern `m5-performance-metrics` with it → named as the conflicting Topic, again no write. This confirms the concurrency rule blocks both the same-Topic case and the shared-Concern case, and that a refusal leaves the file set untouched.
- Mid-round on `topic-a`, three new questions surface and are classified: "should model versioning follow semver?" is small and inseparable → noted in `topic-a`'s own Notes, no new file; "should the ranker serve batch or online predictions?" is precise enough to graduate the Fog entry → the Fog entry is deleted from `MAP.md` and `topic-e.md` is created (unblocked, so it's on the Frontier immediately) in the same edit; "should we deprecate the old rules-based recommender in this same effort?" is beyond the Destination → one line added to `MAP.md`'s Out of scope section with its reason, never dropped silently.
- Closing `topic-a`: **record resolution** sets `status: resolved`/`resolved_at`, creates `concerns/m5-performance-metrics.md` (first touch), and in the same pass `MAP.md` gains a Decisions-so-far line, the Perspective resolution table gains an `M` row (`resolved: 1`), and the Frontier/Blocked rendering flips — `topic-b` moves from Blocked to Frontier (its one blocker is now resolved) alongside `topic-e`, and `topic-a` drops out of both.
- `s1` then claims `topic-b` (allowed — `topic-a`'s `claimed_by` is now on a `resolved` Topic, which the concurrency self-check correctly excludes; this is a real edge case the check has to get right, since **record resolution** deliberately leaves `claimed_by` in place as attribution) and leaves it `partial` after one round, with `concerns/d16-golden-dataset.md` recording a confirmed source fact, a decision, and one stated open question (sizing). A fresh conversation then runs `resume s1-2026-09-18`: it states the Destination, shows the (by-then one-line) Decisions so far, finds `topic-b` by scanning for `status: open` + `claimed_by: s1-2026-09-18` (not `topic-a`, which is `resolved`, and not `topic-e`, which is unclaimed), loads only `d16-golden-dataset.md` and `topic-b.md`, and would continue from the sizing question — without opening `topic-a.md`, `m5-performance-metrics.md`, or `topic-e.md`, and without re-asking what the golden set's source is.
- One incidental finding fed back into the write-up: the Map's rendered Frontier section goes stale the moment a Topic is claimed after the last regeneration (here, `topic-b` still shows in the last-rendered Frontier for a beat after `s1` claims it) — `resolve`'s topic-pick step and `resume`'s "show current Frontier" step both need the "prefer a live **list frontier** re-run over the stale rendering" hedge already written into `work-a-map.md`, not just a courtesy.

**Dry run — an oversized topic splits.** Built a throwaway `topic-personalization.md` ("How should the recommendation feature handle personalization?", claimed by `s1-2026-09-18`, touching four Concerns: `m5-performance-metrics`, `d16-golden-dataset`, `u3-onboarding-flow`, `i2-serving-latency`) under a scratch `requirements/perspec-me/reco-feature/` tree (outside the skill repo, not committed). Traced by hand, no live user:

- Mid-round, the current-understanding test fires: stating where the Topic stands now needs three unrelated threads ("separately, cold-start users..."; "meanwhile, the latency budget...") rather than one 2-5-line summary, and the three threads don't share an answer — the split signal, not just a feeling that the Topic is big. The split is proposed to the user (three tentative questions named) and confirmed before any file is written.
- **Preserve decisions so far**: a synthesis is appended to `topic-personalization.md`'s own Notes first — what's already settled (logged-in users only, implicit behavioral signals) — before any new Topic exists.
- **Split by question, not by Concern**: the four touched Concerns produce three new Topics, not four — `topic-ranking-signals.md` (concerns `m5-performance-metrics`, `d16-golden-dataset`), `topic-coldstart.md` (concerns `u3-onboarding-flow`, `d16-golden-dataset` — `d16` is relevant to two of the three new Topics, the expected N:N shape), and `topic-latency-budget.md` (concern `i2-serving-latency`), each created via **create topic**.
- **Wire blockers**: `topic-coldstart`'s fallback strategy plausibly depends on which signals exist, so **wire blockers** sets its `blocked_by: [topic-ranking-signals]` — the only dependency wired; nothing else was speculated.
- **Aggregator conversion**: `topic-personalization.md` is never passed to **record resolution** (no `resolved_at`); instead its `children:` field is set to `[topic-ranking-signals, topic-coldstart, topic-latency-budget]`, `status` stays `open`, and `claimed_by` stays `s1-2026-09-18` from before the split.
- **Frontier check**: running `list frontier`'s exact three-condition scan over the resulting `topics/` directory (verified with a small script, not just eyeballed) returned `topic-ranking-signals` and `topic-latency-budget` on the Frontier, `topic-coldstart` in Blocked (its one blocker still open), and `topic-personalization` in **neither** — its `claimed_by` is still set, which condition 3 already excludes, confirming the aggregator needs no special-case rule to stay off the Frontier.
- **Fog carried over**: one thread the split surfaced ("offline vs. real-time personalization scoring evaluation") wasn't yet phraseable as a fourth Topic, so it became a Fog entry on `MAP.md` instead, per the existing mechanic — not a Topic, not dropped.
- The session ends at the split — no further round runs against `topic-personalization` in this session; a later `resolve` would claim one of the three new Topics fresh.

**Dry run — a delegated-work entry blocks a Topic, then unblocks it.** Built a throwaway `MAP.md` plus `topics/topic-serving-latency-budget.md` ("What serving-latency budget should the ranker target?", concern `i2-serving-latency`, initially `claimed_by: s1-2026-09-18`, `blocked_by: []`) and `topics/topic-other.md` (an unrelated, unclaimed, unblocked Topic on a different Concern) under a scratch tree outside the skill repo, not committed. Traced by hand, then **verified with an executed script** re-implementing the extended `list frontier` predicate from [local-backend.md](./local-backend.md#list-frontier) (bare `blocked_by` entries checked against a Topic's `status`, `dw:`-prefixed entries checked against the named entry's `status` in the Map's Delegated work section):

- Mid-`resolve` on `topic-serving-latency-budget`, the question ("what does the platform's own SLA docs mandate for p99 latency on a synchronous ranking call?") is classified **Research** — an external fact, not something the user can be interviewed into knowing. A `dw-latency-benchmark` entry is created in `MAP.md`'s Delegated work section (`type: research`, `blocks: topic-serving-latency-budget`, `status: pending`), `dw:dw-latency-benchmark` is appended to the Topic's `blocked_by` via **wire blockers**, and its `claimed_by` is cleared in the same edit per the narrow claim-release exception ([local-backend.md](./local-backend.md#claim)).
- Running the frontier script against this state: `Frontier: ['topic-other']`, `Blocked: [('topic-serving-latency-budget', ['dw:dw-latency-benchmark'])]` — the Topic is Blocked, named by the delegated-work ID, exactly as [work-a-map.md](./work-a-map.md#delegated-work) describes, with no separate "mark Blocked" edit anywhere.
- The Skill tool is called with `"research"`, handing it the entry's question plus the Topic's Concern context; it returns a findings file citing the platform's SLA docs. The entry is updated: `status: resolved`, `resolved_at`, and `result.answer`/`evidence`/`sources`/`affected_concerns: [i2-serving-latency]`/`new_topics: []`.
- Running the frontier script again, with nothing changed on the Topic's own `blocked_by` list (the `dw:` entry stays put, only its target's `status` changed): `Frontier: ['topic-other', 'topic-serving-latency-budget']`, `Blocked: []` — the Topic returns to the Frontier automatically, confirming the "recompute, don't hand-edit" claim structurally rather than just in prose. The Concern `i2-serving-latency`'s Resolution page would, in the same pass, gain the delegated work's evidence/sources in its own **Evidence** section and a **Topic history** line naming `dw-latency-benchmark`, per the create-once/append-after rule (`SKILL.md` section d) — the same mechanics an interview answer already uses, not a new one.
