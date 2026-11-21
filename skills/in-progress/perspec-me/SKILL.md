---
name: perspec-me
description: Resolve one project question through a PerSpecML concern-guided interview — select the relevant Concerns from the catalog, gather evidence, interview the user in short rounds, and persist the answer into per-Concern Resolution pages for that Topic. Use when the user runs `/perspec-me <question>`, asks to work through a Topic with PerSpecML's Concerns and Perspectives, or another skill routes a `resolver: perspec-me` call.
---

# perspec-me

`perspec-me` is a catalog-driven interview that resolves one **Topic** at a time using **Concern** lenses from the PerSpecML catalog shipped in `skills/in-progress/perspec-me/catalog/`, and rolls the result into a durable **Map** toward an agreed **Destination**. This `SKILL.md` is the single entry point for both a human typing `/perspec-me` and another skill routing a `resolver: perspec-me` call (see `docs/adr/0001-one-model-invoked-skill-thin-routing-section.md`) — there is no separate thin command file.

Read `CONTEXT.md` before anything else. It defines Concern, Topic, Session, Map, Destination, Fog, Frontier, Blocked, Resolution page, Perspective coverage, Delegated work, and the seven Concern states, and this skill's prose uses those terms exactly as defined there — never a synonym.

This `SKILL.md` holds the routing section and the direct-session procedure. Four companion files hold what would otherwise make it unwieldy: [map.md](./map.md) is the map-charting procedure (fit-in-one-session decision, Destination, Fog, Topics, Frontier, and the Map file's structure), [local-backend.md](./local-backend.md) is the local Markdown topic-store's five operations (create topic, claim, list frontier, record resolution, wire blockers — ADR 0002's seam, this backend's mechanics), [work-a-map.md](./work-a-map.md) is the procedure for working an existing Map across sessions (`resolve`, `resume`, `status`, `review`), and [issue-seed.md](./issue-seed.md) is the procedure for a seed that is a reference to an existing issue rather than free text (read-first, investigate, extract the decision question, locate Concerns, classify, then the same fit decision as any other seed). All four are referenced from here rather than duplicated.

## Routing

The input to `perspec-me` is either a bare **seed** (a question, idea, or short text with no recognized verb) or one of the verbs below.

- **Bare `<seed>` that is an issue reference** — a bare integer (`42`), a `#42`-style reference, or a URL matching this repo's issue-tracker pattern ([docs/agents/issue-tracker.md](../../../docs/agents/issue-tracker.md)) is an **issue-seed**, not free text. Hand off to [issue-seed.md](./issue-seed.md): read the issue body and every comment before asking the user anything, investigate, extract the underlying decision question (an issue is often phrased as a task or a solution, not a question), locate the related Concerns, state the extracted question and Concerns to the user, then classify it into exactly one of four outcomes — seed for a new Map, a Topic to add to an existing Map, evidence on an existing Topic, or a premature implementation attempt pushed back to the decision it presupposes. Whichever outcome applies, the underlying decision question then goes through the same **fit-in-one-session decision** below as any other seed (never a special-cased issue-only path). The remote issue itself is never modified by any of this without explicit user authorization.
- **Bare `<seed>` that is plain text** — first runs the **fit-in-one-session decision** in [map.md](./map.md#fit-in-one-session-decision): read the seed, inspect the repo breadth-first, take a low-resolution pass over the catalog, and estimate how many independent decisions remain. Say the outcome plainly, then:
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
8. **Map completion and handoff.** Build (or reason precisely against, per the dry run below) a Map where every [Handoff readiness](./map.md#the-map-file) criterion holds: Destination reached, Fog empty (or every remaining entry already lined up in Out of scope), no material Topic left on the Frontier or in Blocked, every touched Concern `resolved`/`deferred`/`not-applicable` with every `deferred`/`not-applicable` one carrying a justification, no unresolved contradiction, and a recorded user-confirmation line already on the Map from an earlier session. Run `status`. Expect: `status` states the Map is complete, names each of the six criteria as holding, and tells the user to run `to-spec` — phrased as a plain instruction to the human, never a Skill tool call.
9. **Handoff without implementation.** Confirm nothing in the `status` completion check or its reporting ever touches a path outside `requirements/perspec-me/<map-slug>/` — no product code path is ever written to, whether the Map turns out complete or not. See the executed check in the dry run below.
10. **A deliberately incomplete Map is correctly refused.** Same constructed Map as test 8, but with one Concern set `not-applicable` and its Resolution page's "Current resolution" left without a justification, and, separately, two Resolution pages recorded as stating incompatible decisions about a shared Concern with no acceptance line in Decisions so far. Expect: `status` does not report completion — it names the specific Concern ID failing the justification gate and the specific pages/Topics in the unresolved contradiction, and it never tells the user to run `to-spec` while either holds, regardless of how complete every other criterion looks.

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

**Dry run — map completion and handoff, verified with an executed script.** Built a throwaway `MAP.md` plus two `resolved` Topics (`topic-ranking-signals`, concern `m5-performance-metrics`; `topic-coldstart-data`, concern `d16-golden-dataset`) and their two Concern Resolution pages, under a scratch `requirements/perspec-me/reco-feature/` tree (outside the skill repo, not committed) — Destination confirmed, Fog/Frontier/Blocked all empty, `m5-performance-metrics` `resolved`, `d16-golden-dataset` `not-applicable` with a multi-sentence justification in its "Current resolution", no contradiction between the two pages, and a `Handoff readiness` line reading "confirmed complete by Eduardo, 2026-09-18". A Python script re-implementing [work-a-map.md](./work-a-map.md#status-map)'s four completion checks (Destination/Fog/Frontier/Blocked read off `MAP.md`; per-Concern deferred/not-applicable justification; cross-page contradiction scan; recorded user-confirmation line) was run read-only against the fixture:

```
- Destination reached: yes
- Relevant Fog empty: yes
- No material Topic on Frontier/Blocked: yes
- d16-golden-dataset: not-applicable, justified
- m5-performance-metrics: resolved
- Contradictions check: none found
- User confirmation: recorded (confirmed complete by Eduardo, 2026-09-18)
RESULT: COMPLETE -- tell the user to run to-spec
```

This confirms `status` reports completion and names `to-spec` as the next step exactly when every criterion holds — matching test 8 above.

**Then, the deliberately-incomplete case (test 10).** The same fixture was copied and mutated two ways: `d16-golden-dataset`'s "Current resolution" was cut down to the bare word "Not applicable." (no reasoning), and both Concern pages' "Decisions" sections were given a mutual `CONTRADICTS:` tag with no matching "ACCEPTED CONTRADICTION" line in the Map's Decisions so far. Running the same script against this mutated fixture:

```
- d16-golden-dataset: not-applicable, NO JUSTIFICATION -- BLOCKS completion
- m5-performance-metrics: resolved
- Contradiction d16-golden-dataset vs m5-performance-metrics: UNRESOLVED -- BLOCKS completion
- Contradiction m5-performance-metrics vs d16-golden-dataset: UNRESOLVED -- BLOCKS completion
- User confirmation: recorded (confirmed complete by Eduardo, 2026-09-18)
RESULT: INCOMPLETE -- completion refused, see BLOCKS lines above
```

`status` correctly refuses to declare completion and names the exact blocking Concern ID (`d16-golden-dataset`, missing justification) and the exact contradicting pair (`d16-golden-dataset` vs `m5-performance-metrics`) — never a vague "some concerns need work," and never `to-spec` mentioned while either hard gate fails, even though every other criterion (Destination, Fog, Frontier/Blocked, user confirmation) still holds.

**Handoff without implementation, verified with an executed check (test 9).** `grep -n -E "Write|Edit\(|write to|writes? to|edit " map.md` and an equivalent scan of `work-a-map.md`'s entire `status [map]` section turned up no file-path reference outside `requirements/perspec-me/<map-slug>/` in either — the only hit in `map.md` is the pre-existing Fog/Topic-file invariant sentence, itself scoped to `requirements/perspec-me/`. Combined with the fixture runs above (the completion-check script only opened files under the scratch `requirements/perspec-me/reco-feature/` tree and wrote nothing, anywhere, in either run), this confirms the completion and handoff procedure never touches a product-code path — the Map/Topic/Resolution-page files are the only artifacts touched, at handoff exactly as during wayfinding.

### Issue-seed smoke tests

Procedure in [issue-seed.md](./issue-seed.md), run against a bare seed recognized as an issue reference.

1. **An issue becomes a Topic on an existing Map.** See the dry run below — a real, small, open repo issue is read in full (body and comments), its decision question is extracted, and it is classified as a Topic to add to an existing Map. Expect: no new Map created, `create topic` runs exactly once under the existing Map, any apparent blockers from the issue's own text are wired to the corresponding existing Topics, and the extracted question (not the issue's literal title) is what's written into the new Topic file.
2. **Read-before-ask ordering holds.** Feed an issue-seed and check the transcript order: the `gh issue view <n> --comments` call (or its result) must appear before any sentence addressed to the user, including the extracted-question statement. Expect: zero user-facing text before the read completes.
3. **An issue maps to no existing Map.** Feed an issue-seed whose decision question is not covered by any existing Map's Destination (or no Map exists yet in the project at all). Expect: classified as **seed for a new Map**, and from there the ordinary fit-in-one-session decision runs unchanged — the issue's origin is not visible anywhere in the resulting Map-or-session path.
4. **An issue is evidence, not a new Topic.** Feed an issue-seed whose extracted question substantially restates a Topic that's already open (or resolved) on an existing Map. Expect: no `create topic` call; the issue's content is folded into the matching Topic's Notes or the relevant Concern Resolution page's Evidence section, and the report to the user states explicitly that no new Topic was created.
5. **A premature-implementation issue is pushed back.** Feed an issue-seed phrased entirely as an implementation step (a specific library, config, or file change) with no stated rationale. Expect: the skill does not implement it and does not treat the proposed solution as already-decided; it states the presupposed decision question instead and classifies *that* question into one of the other three outcomes.
6. **The remote issue is untouched.** Before and after every one of the above, run `gh issue view <n> --json body,state,comments` (or equivalent) on the traced issue. Expect: byte-identical body, state, and comment count before and after — no comment posted, no label changed, no edit, no close — regardless of which of the four classifications the issue received.

**Dry run — a real issue becomes a Topic on an existing Map.** Traced against real issue [#22](https://github.com/Esduard/skills/issues/22) in this repo ("Promote perspec-me to engineering/ (optional)"), read in full via `gh issue view 22 --json number,title,body,labels,comments` (no comments on it at the time of this trace) — read-only, nothing on the issue was changed by this trace.

- **Read first.** The issue's body: it asks to move `perspec-me` from `in-progress/` to `engineering/` "once the full behaviour is in place," with acceptance criteria that are all mechanical steps (move the folder, re-run `scripts/link-skills.sh`, update the top-level README and `plugin.json`, write the four-section docs page, re-sync `ask-sail`), and an explicit "Blocked by" list naming issues #17, #18, #19, #20, #21.
- **Investigate.** Cross-checked the "Blocked by" list against this repo's actual state: #17 and #18 are already closed-out by commits `614f4f9` and `7f97184`; #19 is this very ticket, in progress; #20 and #21 are still open. `skills/in-progress/perspec-me/` and its bucket-promotion rules (`CLAUDE.md`, `.agents/writing-docs.md`) confirm the mechanical steps the issue lists are exactly what promotion requires — nothing about the "how" is in question.
- **Extract the underlying decision question.** The issue is phrased as a task ("promote X"), not a question, and its acceptance criteria presuppose "yes, promote it" is already settled — except the title's own "(optional)" qualifier and the open "Blocked by" list show the real decision hasn't actually been made yet. Extracted question: *"Once perspec-me's remaining behavior (delegated work, issue-seeding, map completion/handoff, tracker backend) is built and validated, should perspec-me be promoted from `in-progress/` to `engineering/` — and what does 'ready' mean here: every blocking issue closed, or a looser bar given the issue's own 'optional' framing?"*
- **Locate related Concerns.** This is where the trace surfaces a genuine limit: `perspec-me`'s catalog (`catalog/README.md`'s five Perspectives — O, U, I, M, D) exists to specify **ML-enabled systems**. Issue #22 is about this skill's own repo-promotion readiness, not about specifying an ML system — this repo is a skill-authoring repo, not the kind of project the catalog's Perspectives describe. Low-resolution pass over `catalog/README.md` and a skim of the Perspective READMEs turned up **no Concern that plausibly applies** — stated explicitly rather than forced. This is a legitimate, reportable outcome per issue-seed.md's "when nothing plausibly fits" step, and it doesn't block classification, which turns on Map/Topic territory, not Concern applicability.
- **State to the user (as this trace's report):** the extracted question above, and "no catalog Concerns apply — this issue is about the skill's own shipping readiness, not an ML-system-specification question."
- **Classify.** For this trace, a throwaway example Map was constructed (not committed, not written to the real repo) at a scratch `requirements/perspec-me/perspec-me-shipping/` path, with Destination "perspec-me's remaining behavior is built and each promotion prerequisite (docs packaging, router wiring, tracker backend) is resolved or explicitly deferred, so a promotion decision can be made without reopening core design questions," and two existing open Topics: `topic-tracker-backend-readiness` (corresponds to #21) and `topic-map-handoff-shape` (corresponds to #20) — neither of which asks the promotion-timing question itself. Against that constructed Map: the Destination plausibly covers issue #22's decision, and no existing Topic already asks it → **classified as a Topic to add to an existing Map.** This explicitly does not start a new Map.
- **Act.** `create topic` would create `topic-promote-to-engineering.md` under that Map with the extracted question (not the issue's title) and `concerns: []` (none applied, stated explicitly in the Topic's own Notes rather than left blank without explanation). `wire blockers` would set `blocked_by: [topic-map-handoff-shape, topic-tracker-backend-readiness]` — the two apparent blockers from the issue's own list that correspond to still-open Topics on this Map; #17 and #18 are not wired since their corresponding work is already done and nothing in this constructed Map tracks them as open Topics.
- **Remote-issue safety, verified.** No `gh issue comment`, `gh issue edit`, or `gh issue close` call was made against #22 at any point in this trace — only `gh issue view` reads.
- **Finding worth recording:** this trace is honest evidence that not every real repo issue turns on a genuine PerSpecML Concern — the extraction and classification steps still produce a clean, actionable answer (a new Topic, correctly placed, correctly blocked) even when the Concern-mapping step comes back empty. A future trace against an actual ML-enabled consuming project's issue would be expected to exercise the Concern-mapping step non-trivially; this repo's own issues, being about a skill-authoring tool rather than an ML system, are a weak fit for that part specifically, and the procedure says so rather than fabricating a mapping to look thorough.

### Tracker-backend smoke tests

Procedure in [tracker-backend.md](./tracker-backend.md), run against a Wayfinder map issue instead of local Topic files. Both traces below are **reasoned through by hand against constructed, illustrative examples — never executed against this repo's real tracker.** This ticket's own instructions forbid creating, commenting on, closing, or editing any real issue in `Esduard/skills` while doing this work; every `gh` command shown below is what *would* run, not a command actually issued.

1. **Wayfinder delegates a topic to `perspec-me`.** Construct two illustrative ticket bodies. First, a perspec-me Topic:

   ```markdown
   ## Question

   Which signals should feed the ranker?

   resolver: perspec-me
   concerns:
     - m5-performance-metrics
     - d16-golden-dataset
   ```

   Second, for contrast, an ordinary Wayfinder grilling ticket with no `resolver:` line:

   ```markdown
   ## Question

   Should the ranker retrain nightly or weekly?
   ```

   Trace [wayfinder/SKILL.md](../../engineering/wayfinder/SKILL.md#work-through-the-map)'s edited step 3 by hand against both: scan the body's lines for one matching `resolver:\s*(\S+)`. The first body matches, capturing `perspec-me` — step 3 calls the Skill tool with `"perspec-me"` instead of the default grilling pair. The second body has no such line — no match — so step 3 falls through unchanged to "call the Skill tool twice, for 'grilling' and 'domain-modeling'," exactly as it did before this edit. Expect: the hook is additive and concretely verifiable, not just asserted in prose — a ticket without the line is provably unaffected.

2. **A topic splits into new issues.** Constructed, illustrative example — no real issues created or touched — under a fictitious Wayfinder map issue #100 ("Recommendation feature — Map"): a child issue #105, "How should the recommendation feature handle personalization?", body carrying `resolver: perspec-me` and `concerns: [m5-performance-metrics, d16-golden-dataset, u3-onboarding-flow, i2-serving-latency]`, assigned (claimed) by the driving session. Mid-`resolve`, the split signal fires (per [work-a-map.md](./work-a-map.md#alternative-outcomes)'s test — three unrelated threads, not one coherent 2-5-line summary) and the user confirms three independent questions, split by question rather than by Concern (four Concerns, three new issues — `d16-golden-dataset` relevant to two of them, the expected N:N shape). Traced `gh` commands (none executed):

   - `gh issue create --title "Which signals should feed personalization ranking?" --body "$(cat <<'EOF'\nPart of #100\n\n## Question\n\nWhich signals should feed personalization ranking?\n\nresolver: perspec-me\nconcerns:\n  - m5-performance-metrics\n  - d16-golden-dataset\nEOF\n)"` → hypothetically creates #106.
   - `gh issue create ...` with the same shape for "How should cold-start users be handled?" (`concerns: [u3-onboarding-flow, d16-golden-dataset]`) → hypothetically #107.
   - `gh issue create ...` for "What latency budget applies to personalization scoring?" (`concerns: [i2-serving-latency]`) → hypothetically #108.
   - Wiring `topic-coldstart` (#107) as depending on `topic-ranking-signals` (#106), the one apparent dependency: `gh api repos/Esduard/skills/issues/106 --jq .id` to read #106's database id, then `gh api --method POST repos/Esduard/skills/issues/107/dependencies/blocked_by -F issue_id=<106's database id>`.
   - Aggregator: `gh issue comment 105 --body "Split into: [Which signals should feed personalization ranking?](#106), [How should cold-start users be handled?](#107), [What latency budget applies to personalization scoring?](#108)"` — a **comment**, the allowed write; #105's body and labels are left untouched, #105 is **not** closed (`record resolution` never runs on it, mirroring the local backend's aggregator rule exactly) and keeps its existing assignee.
   - `list frontier`, traced (not queried live) against this resulting state: #106 and #108 qualify (open, unblocked, unassigned, `resolver: perspec-me`); #107 is excluded by its one open blocker (#106) and would render in Blocked instead; #105 is excluded from both because it still carries an assignee (the retained claim) — matching the local backend's aggregator behavior with no special case needed.

   **Confirmed: no real `gh issue create`, `gh issue comment`, `gh issue close`, or `gh api .../dependencies/blocked_by` call was made against `Esduard/skills` for this trace** — every command above is illustrative, reasoned through by hand the same way #16-#20's subagents traced local-backend mechanics against constructed fixtures, never executed against the real repo.
