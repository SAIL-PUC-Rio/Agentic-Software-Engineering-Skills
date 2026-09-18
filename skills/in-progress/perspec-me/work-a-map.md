# Working a map: resolve, resume, status, review

This is the procedure `SKILL.md`'s routing section hands off to for the four verbs that operate against an **existing** Map: `resolve <topic-ref>`, `resume [session-or-map]`, `status [map]`, and `review <concern-id>`. It never charts a Map or creates the first Topics — that's [map.md](./map.md). It never runs the interview mechanics from scratch either — `resolve` reuses the direct-session procedure's round shape and persistence rule (`SKILL.md` sections c and d) verbatim, scoped to one Map Topic's Concerns instead of a mapless seed. Every write against a Topic goes through the five operations in [local-backend.md](./local-backend.md) — never an ad hoc `Read`/`Write`/`Edit` of a topic file.

## Session identifier

Per [local-backend.md](./local-backend.md#claim), a session identifier is anything that uniquely names the session — a date-stamped slug is enough for a solo project. Within one conversation, `resolve` mints (or reuses) this identifier once, the first time it claims a Topic, and every later `resolve`/`resume`/status check in that same conversation reuses the same value. A fresh conversation resuming a Topic claimed by an earlier one has no way to recover that identifier on its own — the human must supply it as `resume`'s argument (see below).

## Low-resolution load, everywhere

Every one of these four verbs starts by loading the Map file (`requirements/perspec-me/<map-slug>/MAP.md`) at **low resolution**: read the **Destination**, **Frontier**, and **Blocked** sections (plus **Fog** where a verb needs it), never the full **Decisions so far** history, never every Topic file, and never every Concern Resolution page. Anything beyond that is loaded on demand, scoped to the one Topic or one Concern the verb is actually working — this mirrors the fit decision and charting pass in [map.md](./map.md), which apply the same discipline to reading the catalog.

## Concurrency: one Topic per Session, claim before work

Stated once here because all four verbs touch it in some way:

- A Session that has already claimed a Topic must **resolve** it, **leave it open**, or explicitly hand it off before claiming a different one. Before claiming a new Topic, scan `topics/` for any file that is both `status: open` **and** `claimed_by` equal to this session's own identifier; if one exists and isn't the Topic being claimed, stop and say so instead of claiming a second one. A Topic **record resolution** already closed keeps its old `claimed_by` as historical attribution (per [local-backend.md](./local-backend.md#record-resolution)) — a resolved Topic is never "still claimed" for this check, only an open one is.
- Before claiming a Topic, also check it against every Topic **currently claimed by another session** — scan `topics/` for files that are `status: open` with `claimed_by` set and not equal to this session's identifier (this scan, and the refusal rule on `claim` itself, are documented in [local-backend.md](./local-backend.md#claim)). A resolved Topic is excluded from this scan for the same reason. For each remaining other-claimed-and-open Topic, the target Topic conflicts if:
  - they share any Concern ID (their `concerns` lists intersect), or
  - either names the other in its `blocked_by`.
- On conflict: refuse to claim, name the conflicting Topic (its slug and question) and the reason (shared Concern `<id>`, or the `blocked_by` edge), and stop — no interview round runs.
- On no conflict: run **claim** ([local-backend.md](./local-backend.md#claim)) before any interview round starts, exactly as the direct-session procedure claims nothing today (it has no Topic to claim) but a Map Topic always does.

## `resolve <topic-ref>`

1. **Load the Map at low resolution** (above).
2. **Pick the Topic**: if `<topic-ref>` names one, use it; otherwise take the first entry in **list frontier**'s current result ([local-backend.md](./local-backend.md#list-frontier)) — the Map's rendered Frontier section is that query's last-regenerated snapshot, so prefer re-running **list frontier** live over trusting a stale rendering if the two could differ.
3. **Run the concurrency check and claim** (above) — before any interview work, not after.
4. **Load only this Topic's Concerns**: read the Topic file's `concerns:` list, then for each ID, the Concern's Resolution page under `requirements/perspec-me/<map-slug>/concerns/<concern-id>.md` (if one already exists) and its canonical catalog page. Nothing else — no other Topic's Concerns, no other Concern Resolution pages.
5. **Investigate + interview**: reuse `SKILL.md` section b (investigate) and section c (the six-part round) exactly as written, scoped to this Topic's question and Concerns instead of a mapless seed. Reuse section d's persistence rule exactly — write to `requirements/perspec-me/<map-slug>/concerns/<concern-id>.md` (the Map's Concern Resolution path, per [map.md](./map.md#resolution-layer-convention-once-a-map-exists)), never `_unmapped/`, after every answer. Do not re-describe the round shape or the persistence rule here — the six parts and the per-answer rule are section c/d's job, cited, not duplicated.

### New-question classification

Whenever a round surfaces a question beyond the one currently being resolved, classify it into exactly one of these four outcomes — never leave it unclassified or silently dropped:

- **Small and inseparable** — folds into the current Topic's remaining questions; it does not become a new Topic, a Fog entry, or an Out-of-scope line. Keep resolving it as part of this Topic.
- **Distinct and formulable** — precise enough to state as its own question. Run **create topic** ([local-backend.md](./local-backend.md#create-topic)) for it now, with `wire blockers` ([local-backend.md](./local-backend.md#wire-blockers)) if it depends on something already known. If it has no blockers (or all its blockers are already resolved), it is on the Frontier the moment it's created — that's just what **list frontier** computes over the directory, not a separate edit.
- **Known but nebulous** — real and relevant, but not yet phraseable as a precise question. Add one Fog entry to the Map's Fog section, per [map.md](./map.md#fog)'s shape (label, Perspective/task, one or two lines).
- **Beyond the destination** — outside what this Map's Destination covers. Add one line to the Map's **Out of scope** section with a one-line reason. Never drop it silently — a reader must be able to see it was considered and excluded on purpose.

**Fog graduation**: the moment a Fog entry becomes precise enough to state as a question — whether that happens mid-`resolve` on the current Topic or on an unrelated one — remove it from the Map's Fog section and run **create topic** for it in the same edit. This is [map.md](./map.md#hard-invariant)'s Hard invariant applied during `resolve`, not a competing rule: the same understanding never sits in both Fog and a Topic file at once, even briefly across two writes.

### Closure

When the Topic's question is settled and the user agrees it's resolved, these four things happen together, in one closing pass — not staggered across separate steps:

1. **Record resolution** ([local-backend.md](./local-backend.md#record-resolution)) — sets the Topic file's `status: resolved` and `resolved_at`, appends the decision line to the Map's Decisions so far, and creates/updates the touched Concern Resolution page(s).
2. The Topic **leaves the Frontier automatically** — **list frontier** no longer selects a `resolved` Topic, so this is not a separate edit.
3. Any Topic that named this one in its `blocked_by` is **unblocked** — the next **list frontier** run reflects that automatically on the data side, but explicitly **refresh the Map's rendered Frontier and Blocked sections** so a human reading the Map file sees the newly-unblocked Topic move over, not just the underlying directory state.
4. **Refresh the Map's Perspective resolution coverage table** ([map.md](./map.md#the-map-file)) for the Perspective(s) the touched Concern(s) belong to, from those Concerns' current `status`.

Also publish a short synthesis on the Topic (what was decided, which Concerns/Resolution pages were touched) as part of this same pass, the same shape the direct-session procedure's closure already produces (`SKILL.md` section e) — closing a Topic under a Map still never begins implementation.

### Alternative outcomes

- **Left open**: the session ends without the Topic reaching closure. Do not call **record resolution** — the Topic file stays `status: open` and still `claimed_by` this session. A later session either resumes it (see `resume` below, run by the same session identifier or a human-supplied one) or the claim eventually needs releasing; this ticket does not build an explicit "unclaim" step — note it as a gap for whichever future ticket needs it, don't invent one here.
- **Split**: a Topic that has grown past what one session can hold.

  **Recognizing the signal.** The trigger is the issue's own test — "the question cannot be settled without materially expanding the session" — made concrete against the six-part round (`SKILL.md` section c). Either of these, mid-round, is the signal:
  - Part 1's **current understanding** can no longer be written as one coherent 2-5-line summary without conflating two or more threads that don't share an answer — you find yourself reaching for "separately," "meanwhile," or a bulleted list of unrelated threads just to say where the Topic stands.
  - Part 2's **question being resolved** has turned out to be several genuinely independent sub-questions — answering one doesn't move the others forward, and different stakeholders could plausibly answer them on different timelines. This is the same test `map.md`'s fit-in-one-session decision applies before a Map exists, applied here mid-session to one Topic that's already past charting.

  Either symptom triggers *proposing* a split, never doing it silently. State the proposed split to the user — the tentative set of independent questions you'd carve out — and wait for explicit confirmation, the same Destination-confirmation-gate discipline `map.md` uses before any Topic exists: no **create topic** call runs before the user agrees. If the user declines, the session continues the interview on the original Topic as a single Topic — nothing is created, nothing about its file changes.

  Once the user confirms, in one pass:

  1. **Preserve decisions so far, before doing anything else.** Write a short synthesis into the original Topic's own Notes — what's already settled — the same shape as the direct-session procedure's closure synthesis (`SKILL.md` section e: what was decided, which Concerns/Resolution pages were touched). This doesn't touch Concern Resolution pages themselves — those already hold whatever was persisted per answer (`SKILL.md` section d); this synthesis is the Topic file's own record of where it stood at split time.
  2. **Identify the independent questions that remain — split by question or decision, never by Concern.** A Topic touching four Concerns does not automatically become four new Topics: the number of new Topics is however many genuinely independent questions remain, which may be fewer, or occasionally more, than the number of Concerns touched. Apply the same charting discipline `map.md` uses when charting a Map: only split off a question that's already precisely phraseable now; a thread that's real but not yet sharp enough to state as a question is Fog, not a new Topic (step 5).
  3. **Create the new Topics.** For each remaining independent question, run **create topic** ([local-backend.md](./local-backend.md#create-topic)), phrased as a question, with `concerns:` set to whichever Concern IDs it plausibly touches. A Concern may be relevant to more than one new Topic — that's the normal N:N shape (`CONTEXT.md`), not a sign the split is wrong.
  4. **Wire dependencies between the new Topics.** Where one new Topic's answer plausibly constrains another's, run **wire blockers** ([local-backend.md](./local-backend.md#wire-blockers)) on the dependent one — only wire what's already apparent from the split, the same restraint `map.md`'s Dependencies section uses; don't speculate a blocker to look thorough.
  5. **Route any leftover Fog or out-of-scope material** the split surfaces through the existing mechanics, unchanged: a region that's relevant but not yet phraseable as one of the new Topics becomes a Fog entry (`map.md`'s Fog section); a thread beyond this Map's Destination becomes a line in Out of scope — never dropped silently, same as the New-question classification above.
  6. **Turn the original Topic into an aggregator.** Do not run **record resolution** on it — an aggregator's question was divided, not answered, so it never carries `resolved_at`. Set its `children:` field (see [local-backend.md](./local-backend.md#topic-file-shape)) to the new Topics' slugs; this is the only write that ever populates `children:`. Its `status` stays `open` and its `claimed_by` stays whatever the concurrency check set when this session claimed it — an aggregator is not a third status value, it's an open, still-claimed Topic that happens to have children, which is exactly why it needs no special case to stay off the Frontier (next step).
  7. **The new Topics land on the Frontier exactly as usual.** An unblocked new Topic (no `blocked_by`, or every named blocker already resolved) is on the Frontier the moment it's created — that's just what **list frontier** ([local-backend.md](./local-backend.md#list-frontier)) computes over the directory, the same restatement the "Distinct and formulable" classification above already gives a newly-created Topic, not a separate mechanism for split-created ones.
  8. **End the session.** The split is where this session stops — no further interview rounds run against the now-split Topic in this session. A later `resolve` against one of the new Topics is a new claim, same as any other Frontier Topic.
  9. **Refresh the Map.** The Map's rendered Frontier and Blocked sections pick up the new Topics on next read/update — the same "regenerate, don't hand-edit" rule as the closure section above and `map.md`'s Frontier section. Any Fog or Out-of-scope lines from step 5 are already reflected, since they were written directly into the Map's own sections.

  A later reader landing on the aggregator Topic finds every child from its `children:` list.

## `resume [session-or-map]`

1. **Load the Map at low resolution** (above). If the optional argument names an existing `requirements/perspec-me/<arg>/MAP.md`, treat it as a map-slug and load that Map; otherwise treat it as a session identifier (see below). With no argument: if exactly one Map exists under `requirements/perspec-me/`, use it; if more than one, ask which.
2. **State the Destination** — one line, read verbatim from the Map's Destination section.
3. **Summarize recent Decisions so far** — the most recent 3-5 entries from that section, not the entire history.
4. **Show the current Frontier** — the Map's rendered Frontier section (or a fresh **list frontier** run if it looks stale).
5. **Find the claimed Topic**: scan `topics/` for the file whose `claimed_by` equals the session identifier — this conversation's own identifier if `resolve` already claimed something earlier in the same conversation, or the argument the human supplied if this is a fresh conversation resuming an earlier one's claim. Do not ask the user to name which Topic; the claim is what answers that.
6. **Load only that Topic's Concerns** — same restriction as `resolve` step 4.
7. **Continue from the next open question** — use the Topic's own persisted evidence (its Concern Resolution pages' Confirmed facts / Decisions / Open questions, and the Topic file's Notes) to determine what's already answered. Do not re-ask a question that evidence shows was already answered, and do not restart the round sequence from round 1 — pick up mid-round at the next open question, continuing to reuse `SKILL.md` sections c and d exactly as `resolve` does.

**What `resume` must not load**: any Topic file with `status: resolved` (closed Topics), and Concern Resolution pages for Concerns outside the currently-claimed Topic's own `concerns:` list. Both are outside what a resumed Session needs to keep going.

## `status [map]`

Print, from the low-resolution Map alone and nothing else:

- **Destination**
- **Perspective resolution** coverage table
- **Frontier**
- **Blocked**
- **Fog**
- **Delegated work**

This is a read of the Map file's own sections, verbatim or lightly rendered — `status` never opens an individual Concern Resolution page or a Topic file. The optional `[map]` argument selects which Map when a project has more than one, the same map-slug resolution `resume` uses in its step 1.

## `review <concern-id>`

Open exactly one file: `requirements/perspec-me/<map-slug>/concerns/<concern-id>.md`. Show its **current resolution**, its `status`, and the **Topic history** section (which Topics shaped it, and what each settled). This does not open the Map file's Decisions-so-far history, any Topic file, or any other Concern's Resolution page — one page in, one page shown.
