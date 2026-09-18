# Map-charting: turning a multi-session effort into a Map

This is the procedure `SKILL.md`'s routing section hands off to when a seed doesn't fit one Session, or when the user invokes `map <effort-or-destination>` directly. It produces a durable Map (`CONTEXT.md`'s definition) and the initial set of Topics under it, using the local Markdown backend's five topic-store operations defined in [local-backend.md](./local-backend.md). It never runs the interview itself — resolving a Topic once it's charted is the direct-session procedure in `SKILL.md`, run per Topic, later.

## Fit-in-one-session decision

Every bare seed goes through this before anything else — greenfield idea, existing issue, half-written doc, it makes no difference; the seed's origin never picks the mode.

1. **Read the seed** once, in full — the idea, document, issue body, or conversation excerpt the user gave.
2. **Inspect the repo breadth-first**: skim directory names and existing docs plausibly related to the seed (`CONTEXT.md`, ADRs, README files, obviously-relevant code paths) — a survey, not a deep read of any one file.
3. **Take one low-resolution pass over the catalog**: read `catalog/README.md`, then the `README.md` of each Perspective the seed plausibly touches (the same first two steps as the direct-session procedure's progressive disclosure, `SKILL.md` section a.1–a.2) — stop there. Do not open a Concern folder yet; that level of detail isn't needed to judge fit, only to resolve a Topic later.
4. **Estimate the number of independent decisions remaining** — questions that don't collapse into each other and that different stakeholders could plausibly answer differently or on different timelines.

State the outcome plainly, out loud, before continuing:

- **Fits one session** — one clear question, or a small number of tightly-coupled sub-questions, confined to one or two Perspectives, answerable in a single interview with no dependency structure between its parts. Say so explicitly ("this fits one session — running the direct session, no Map needed") and run the direct-session procedure. Nothing below this point runs.
- **Needs a Map** — several independent decisions, spanning three or more Perspectives, or the seed itself frames a multi-phase effort (an epic, a feature with several unresolved sub-questions, an initiative rather than a single question). Continue to the Destination step below.

This is a judgment call, not an arithmetic threshold — when genuinely unsure, say which way the estimate leans and why, rather than picking silently.

## Destination — confirm before any Topic exists

Propose one sentence stating the condition under which everyone will recognise this Map's elaboration work as done (`CONTEXT.md`'s Destination definition — e.g. "the recommendation feature's requirements are clear enough to become implementation tickets: input signals, model approach, serving latency budget, and success metrics are all decided").

**Hard gate: state the proposed Destination to the user and wait for explicit confirmation (agreement, or a corrected version they confirm in turn) before creating the Map file's Topics — before running create topic even once.** The Map file itself, with Destination filled in and every other section empty or marked pending, may exist before confirmation (there is nowhere else to write the proposal down), but no Topic file exists until the Destination is confirmed. This is not a suggestion to seek buy-in eventually — it is a stop-and-wait step, the same discipline the direct-session procedure already uses at the end of every interview round (`SKILL.md` section c).

If the user's confirmation changes the wording, use their wording — the Destination belongs to them, not to the skill's first draft of it.

## Low-resolution catalog read

Once the Destination is confirmed, read the catalog at the same resolution as the fit decision above — Perspectives and their tasks, not full Concern definitions:

- `catalog/README.md` for the five Perspectives.
- Each plausibly-relevant `catalog/perspectives/<perspective-slug>/README.md` for its tasks, recommended stakeholders, and the list of Concern links it groups under each task.

Do not open individual Concern `README.md`/`definition.md` files during charting — that depth belongs to the Session that later resolves a specific Topic (`SKILL.md` section a.3), not to charting the map.

## Fog

For each region the low-resolution read surfaces as clearly relevant but not yet sharp enough to phrase as a question, add one Fog entry: a short label, which Perspective(s)/task(s) it sits under, and one or two lines on what's known-but-imprecise about it (`CONTEXT.md`'s Fog definition). Fog entries live in the Map file's own Fog section (see below) — they are not Topic files, and no topic-store operation touches them.

## Topics — only what's already phraseable

For each question precise enough to state now, run **create topic** ([local-backend.md](./local-backend.md#create-topic)) with the question phrased as a question — never as an implementation step or a task ("should the ranker retrain nightly or weekly?", not "define retraining cadence"). Associate the Concern IDs the low-resolution read suggests it touches; a Concern folder does not need to be opened to guess this at Perspective/task granularity.

**Discipline: chart only what can already be phrased precisely.** Do not pre-generate a Topic for every task or Concern a Perspective lists "to be thorough" — a Perspective with ten Concerns does not imply ten Topics on day one. A region that isn't yet phraseable as a question stays Fog, even if it's obviously going to matter eventually. The Frontier growing slowly, one graduated Fog entry at a time, is the intended shape of a Map's life — not a backlog dumped up front.

## Dependencies

Where one Topic's answer plausibly constrains another's, run **wire blockers** ([local-backend.md](./local-backend.md#wire-blockers)) on the dependent Topic, naming the blocking Topic's slug. Only wire a dependency that's already apparent from the charting pass — don't speculate blockers into existence to look thorough.

## Frontier

Never hand-maintain a Frontier list. After Topics and blockers are charted, the Frontier is whatever **list frontier** ([local-backend.md](./local-backend.md#list-frontier)) returns — open, unblocked, unclaimed — and the Map file's Frontier section is a labelled rendering of that query's result, regenerated whenever the Map is next read or updated, not a separate editable record.

## Hard invariant

**Nothing appears in both Fog and Frontier (or anywhere among the Topic files) at the same time.** The moment a Fog entry becomes precise enough to state as a question, remove the Fog entry and run **create topic** for it in the same edit — never leave both the Fog line and the new Topic file present together, even briefly across two separate writes.

## The Map file

Lives at `requirements/perspec-me/<map-slug>/MAP.md` (ADR 0003). Exactly these sections, in this order:

```markdown
# <Effort name> — Map

## Destination

<The confirmed one-sentence Destination. State the confirmation date and, if the user's own wording differs from the first proposal, that it's theirs verbatim.>

## Current understanding

<2-5 lines, kept current: where this effort stands right now, in prose. Rewritten as the Map evolves — this is a snapshot, not a log.>

## Perspective resolution

A summary table only — never a Concern description. One row per Perspective actually touched so far (a Perspective with zero touched Concerns doesn't get a row yet):

| Perspective | unexamined | open | partial | resolved | deferred | not-applicable | superseded | Perspective page |
|---|---|---|---|---|---|---|---|---|
| M — Model | — | 1 | 2 | 0 | 0 | 0 | 0 | [perspectives/model.md](perspectives/model.md) |

Counts come from that Perspective's Concern Resolution pages under `concerns/` (`local-backend.md`'s Concern Resolution page convention) — a Concern with no Resolution page yet is implicitly `unexamined` and isn't counted individually until a Topic actually touches it. The "Perspective page" link points at `requirements/perspec-me/<map-slug>/perspectives/<perspective-id>.md`, created on demand the first time any Concern in that Perspective is touched — never scaffolded for all five Perspectives up front. A Perspective page lists that Perspective's touched Concerns with a one-line state and a link into its own Resolution page; it still never repeats a Concern's description, only links to the canonical catalog entry and to the project's Resolution page.

## Decisions so far

<One line per resolved Topic, appended by record resolution (local-backend.md) — what was decided, link to the Topic file, link to the Concern Resolution page(s) it touched. Newest last.>

## Frontier

<Rendering of list frontier's current result — open, unblocked, unclaimed Topics, each as its question with a link to its Topic file. Labelled with when it was last regenerated. Never hand-edited.>

## Blocked

<Topics that are open but fail list frontier's blocked-by check — each with the blocker(s) still open. Clears automatically (moves to Frontier) once every named blocker is resolved.>

## Fog

<Entries per the Fog section above: label, Perspective/task, one or two lines. None of these also appear as a Topic file or in Frontier/Blocked — see Hard invariant.>

## Delegated work

<One entry per Research, Prototype, or Unblocking task Delegated work record (`CONTEXT.md`'s definition), created and resolved per [work-a-map.md](./work-a-map.md#delegated-work). Delegated work is a Map-level record, not a Topic — it has no file of its own under `topics/`; it lives here, inline. Newest entries last.>

### dw-<slug>

```markdown
- type: research | prototype | unblocking-task
- question: <the one question this entry exists to answer, stated plainly>
- blocks: <topic-slug>              # the one Topic this entry unblocks; a Topic names this entry back via its own blocked_by: [dw:dw-<slug>]
- status: pending | in-progress | resolved
- created_at: <ISO date>
- resolved_at:                      # absent until resolved
- parallel_safe_with:               # dw-ids this entry was determined safe to run alongside, per the concurrency overlap check (work-a-map.md#delegated-work); empty/absent if untested or unsafe
  - <dw-id>
- checklist:                        # unblocking-task only — one concrete, human-actionable line per item; absent for research/prototype
  - <e.g. "get read access to the events warehouse">
- result:                           # absent until resolved
    answer: <the answer this entry settled>
    evidence: <what backs the answer — links, artifacts, findings file, prototype branch>
    sources: <primary sources, if research; the prototype's branch/commit, if prototype; the human's report, if unblocking-task>
    affected_concerns:
      - <concern-id>
    new_topics:
      - <topic-slug>                # any newly discovered Topic created from this result, or empty if none
```

A `dw-<slug>` ID is stable once created — never renamed, for the same reason a topic-slug isn't (it's referenced from a Topic's `blocked_by`). `status` starts `pending`, moves to `in-progress` once a Skill tool call (research/prototype) or a human checklist (unblocking-task) is actually underway, and `resolved` once the result is written back (per [work-a-map.md](./work-a-map.md#when-a-delegated-result-returns)). Rendering this section in the Map means listing every entry not yet `resolved` prominently (these are the ones keeping a Topic in Blocked) and resolved entries below them or trimmed to one line — a reader should see at a glance what's still in flight.

## Out of scope

<What this Map's Destination explicitly excludes, so a later reader doesn't re-litigate it as an oversight.>

## Handoff readiness

<A checklist, never a percentage — one line per completion criterion, its current hold/not-hold state, and a link to whatever's outstanding for it instead of restating the Topic/Concern/Fog detail already recorded elsewhere in this Map.>

- [ ] **Destination reached** — <yes, with the date last reaffirmed as still current | no, with what's still open toward it, linked.>
- [ ] **Relevant Fog is empty** — <N remaining entries (0 when complete), each linked. "Relevant" means Fog inside this Map's own Destination scope; a Fog entry already reasoned into a line in Out of scope is Out-of-scope-adjacent and does not count against this criterion — say so explicitly rather than leaving "relevant" unexplained.>
- [ ] **No material Topic remains on the Frontier or in Blocked** — <every remaining Frontier/Blocked Topic, linked, unless the user has explicitly said — in a line recorded here or in Decisions so far — that it's non-material (a genuinely optional refinement they've waved off, not a load-bearing decision). This skill never decides materiality on its own; an open Topic nobody has explicitly waved off always counts against this criterion, however minor it looks.>
- [ ] **Every relevant Concern is `resolved`, `deferred`, or `not-applicable`** — hard gate — <state drawn from the Perspective resolution table: any Concern still `unexamined`/`open`/`partial` fails this outright, named by ID. Independently, any Concern currently `deferred` or `not-applicable` whose Resolution page's "Current resolution" section carries no justification (the hard rule already in [SKILL.md](./SKILL.md) section d: "`not-applicable` must always carry its justification", extended here to `deferred` for the same reason) blocks completion outright — name it by Concern ID (e.g. "d16-golden-dataset: not-applicable, no justification — blocks completion"), never pass it silently.>
- [ ] **Contradictions between Concern resolutions are resolved or explicitly accepted** — hard gate — <a contradiction here means two Resolution pages, or two Topics' recorded decisions, stating incompatible things about a shared Concern or an overlapping requirement. Surfacing these is a mechanical check run before completion is declared, never something smoothed over silently. Each one is either reconciled (state how, and by which Topic/decision) or explicitly accepted by the user as tolerable — an acceptance is recorded as its own line in Decisions so far, not just implied here. An unresolved, unaccepted contradiction blocks completion exactly like a missing justification above; name both sides.>
- [ ] **User confirms no material decision is missing** — <the final gate, always a human confirmation, never inferred by the skill from how complete everything else looks. Record it here once given, e.g. "confirmed complete by <name>, <ISO date>" — this line is what a later `status` call reads to know this gate already passed in an earlier session.>

**Invariant:** reaching every checkbox above, and the handoff itself, never produces or edits product code. The Map file, its Topic files, and its Concern Resolution pages under this Map's own `requirements/perspec-me/<map-slug>/` are the only artifacts `perspec-me` ever writes — during wayfinding and at handoff alike. A completed Map is not a spec and not an implementation plan; handing off means telling the user to run `to-spec` (a user-invoked skill — an instruction to the human, never a Skill tool call, per [.agents/invocation.md](../../../.agents/invocation.md)), not calling it.
```

## Topic files

One file per Topic, structure and the create/claim/frontier/blockers/resolution mechanics defined in [local-backend.md](./local-backend.md) — this document only decides *when* a Topic is created (once it's phraseable, never before) and *what question it holds*, never how the file itself is written; that's local-backend.md's job, so the mechanics are defined once.

## Resolution-layer convention once a Map exists

Before a Map exists, a direct session writes Concern Resolution pages to the fixed `requirements/perspec-me/_unmapped/concerns/<concern-id>.md` bucket (`SKILL.md` section d). Once map-charting produces a real `<map-slug>`, every Resolution page a Topic under *this* Map touches goes to `requirements/perspec-me/<map-slug>/concerns/<concern-id>.md` instead (ADR 0003) — a fresh file, or an update to one already created by an earlier Topic under the *same* Map, following the same append-don't-overwrite rule as the direct session's Resolution pages.

**Out of scope for this ticket:** migrating any pre-existing `requirements/perspec-me/_unmapped/` content into a newly-charted Map's `concerns/` directory. If a project charts a Map for an effort that already accumulated `_unmapped/` Resolution pages from earlier direct sessions, reconciling the two is left as a follow-up for a dedicated ticket — issue #16's `resolve`/`resume`/`status`/`review` verbs ([work-a-map.md](./work-a-map.md)) only ever read and write a Map's own `<map-slug>/concerns/` pages, and do not read or move `_unmapped/` content either. This procedure only ever writes fresh Resolution pages under the new `<map-slug>`.
