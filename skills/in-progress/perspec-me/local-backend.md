# Local Markdown backend: the topic-store operations

ADR 0002 (topic-store seam) defines five operations — **create topic**, **claim**, **list frontier**, **record resolution**, **wire blockers** — independent of where a Topic lives. This file is the concrete mechanics for the local Markdown backend (no tracker, no Wayfinder): plain files under a consuming project's `requirements/perspec-me/<map-slug>/`. The future issue-tracker backend (issue #21) implements the same five names against Wayfinder's own mechanics, per `docs/agents/issue-tracker.md`'s Wayfinding-operations section — that file is this one's sibling, not a competing definition.

**Every** perspec-me procedure that touches a Topic — the map-charting procedure in [map.md](./map.md), the direct-session procedure in `SKILL.md`, and the `resolve`/`resume`/`status`/`review` verbs in [work-a-map.md](./work-a-map.md) — writes against these five operations, never against an ad hoc `Read`/`Write`/`Edit` of a topic file invented on the spot. If a step needs a sixth thing (e.g. "rename a topic"), that's a gap in this file to fix here, not a one-off workaround in the caller.

## Where things live

- Map file: `requirements/perspec-me/<map-slug>/MAP.md` (structure: [map.md](./map.md#the-map-file)).
- Topic files: `requirements/perspec-me/<map-slug>/topics/<topic-slug>.md` — one file per Topic.
- Perspective pages: `requirements/perspec-me/<map-slug>/perspectives/<perspective-id>.md` — created on demand, never scaffolded for all five perspectives up front.
- Concern Resolution pages: `requirements/perspec-me/<map-slug>/concerns/<concern-id>.md` — same template as the direct-session procedure's Resolution page (`SKILL.md`, section d), created the first time a Topic under *this* Map touches that Concern.

`<map-slug>` and `<topic-slug>` are both short kebab-case identifiers (e.g. `map-slug`: `recommendation-feature`; `topic-slug`: `which-signals-feed-the-ranker`), chosen when the file is created and never renamed afterward — a later rename would break every `blocked_by` reference to it.

## Topic file shape

```markdown
---
question: <the Topic's question, verbatim, phrased as a question>
status: open            # open | resolved — set once, by record resolution
blocked_by:             # topic-slugs this Topic depends on; empty list if none
  - <topic-slug>
claimed_by:             # absent/empty until claimed; a session identifier once claimed
concerns:               # Concern IDs this Topic is expected to touch
  - <concern-id>
created_at: <ISO date>
resolved_at:            # absent/empty until record resolution sets it
children:               # topic-slugs this Topic was split into; absent/empty unless this Topic is a split aggregator
  - <topic-slug>
---

## Notes

<Anything worth carrying into the Session that doesn't belong in the one-line question — free text, optional.>
```

`status` is a **two-state** field, deliberately narrower than a Concern's seven states: a Topic is either still open (not yet closed by a Session) or `resolved`. Whether it's additionally *blocked* or *claimed* is never stored as a third status value — it's computed from `blocked_by` and `claimed_by`, per the operations below. This keeps "blocked" and "frontier" derived rather than two competing sources of truth for the same fact.

**`children` and the aggregator convention.** A Topic with a non-empty `children` list is an **aggregator**, produced only by the split mechanic ([work-a-map.md](./work-a-map.md#alternative-outcomes)) — it is a link to the Topics it was divided into, not a status, so `status` is never overloaded to mean "split." An aggregator's own question was never answered, only divided, so it never runs **record resolution** and never carries `resolved_at`; it stays `status: open` with whatever `claimed_by` it already had from being claimed before the split (this repo has no explicit "unclaim" step yet — see [work-a-map.md](./work-a-map.md#alternative-outcomes)'s "Left open" note — so an aggregator's claim is left in place the same way). That open-plus-claimed combination is also what keeps it off the Frontier without needing a special case: **list frontier**'s third condition below (`claimed_by` absent or empty) already excludes it. `children` is written exactly once, by the split mechanic, at split time — no other operation reads or writes it.

## The five operations

### create topic

Write a new file at `requirements/perspec-me/<map-slug>/topics/<topic-slug>.md` using the shape above: `status: open`, `blocked_by: []` unless dependencies are already known (wire them with **wire blockers** instead of hand-listing them here after the fact, once the blocking Topic exists), `claimed_by` absent, `concerns` set to whatever Concern IDs the charting pass already associated with this question, `created_at` set to today. Never create a Topic file for a question that isn't precisely phraseable yet — that's Fog, not a Topic (see [map.md](./map.md#fog)).

### claim

Add (or set) `claimed_by: <session identifier>` in the Topic file's frontmatter. This is the session's first write to the Topic file, mirroring `docs/agents/issue-tracker.md`'s `gh issue edit <n> --add-assignee @me` — a claim happens before any interview round starts, not after. A `<session identifier>` is anything that uniquely names the session (a date-stamped slug is enough for a solo project); its only job is to make "claimed" visible to `list frontier`.

**Refusal rule:** a Topic that is `status: open` and already has `claimed_by` set to a session identifier different from the claiming session's own refuses the claim — report which session holds it and stop, don't overwrite `claimed_by`. Claiming succeeds as a no-op if `claimed_by` already equals the claiming session's own identifier (re-affirming its own claim, e.g. on `resume`), and succeeds normally if `claimed_by` is absent/empty. A `status: resolved` Topic's `claimed_by` is historical attribution left by **record resolution**, not an active claim — it never triggers this refusal, whether the claiming session is the same one or a different one.

**Finding a session's claimed Topic:** scan every file in `topics/` and return the one that is `status: open` with `claimed_by` equal to the given session identifier — this is the same directory scan `list frontier` already makes, filtered on `status` and `claimed_by` instead of the three Frontier conditions, needing no new storage or index. There is at most one such file per session, per the one-Topic-per-Session rule (`work-a-map.md`'s concurrency section); a scan finding more than one is itself a bug to flag, not a case to silently pick from.

### list frontier

Scan every file in `requirements/perspec-me/<map-slug>/topics/`. A Topic file is in the Frontier if and only if all three hold:

1. `status: open`
2. every slug in `blocked_by` names a Topic file whose own `status` is `resolved` (an empty `blocked_by` list trivially satisfies this)
3. `claimed_by` is absent or empty

This is a computation over the directory, run fresh each time — never a separately maintained list edited by hand. The Map's own "Frontier" section (see [map.md](./map.md#the-map-file)) is a rendering of this query's result as of the last time the Map was regenerated, labelled as such, not an independent record.

### wire blockers

To make Topic B depend on Topic A: edit Topic B's frontmatter and append `A`'s topic-slug to B's `blocked_by` list. This is the only place a `blocked_by` edge is written — **create topic** only sets already-known blockers at creation time; adding a dependency discovered later always goes through this operation, on the dependent (blocked) Topic's own file. Wiring a blocker never touches the blocking Topic's file.

### record resolution

When a Session closes a Topic:

1. In the Topic's own file: set `status: resolved` and `resolved_at: <ISO date>`. Leave `claimed_by` as-is (it records who closed it).
2. In the Map file's "Decisions so far" section: append one line — what was decided, and a link to the Topic file and to the Concern Resolution page(s) it touched. This mirrors `docs/agents/issue-tracker.md`'s Resolve operation's "append a context pointer to the map's Decisions-so-far."
3. In each touched Concern's Resolution page under `requirements/perspec-me/<map-slug>/concerns/<concern-id>.md`: apply the same per-answer persistence rule the direct-session procedure already uses (`SKILL.md`, section d) — create the page only the first time that Concern is touched under this Map, otherwise append to / update its existing synthesis, never overwrite it wholesale.

A Topic's resolution never re-runs **list frontier** as a side effect — the next read of the Frontier naturally reflects the now-`resolved` status and any Topics it was blocking.
