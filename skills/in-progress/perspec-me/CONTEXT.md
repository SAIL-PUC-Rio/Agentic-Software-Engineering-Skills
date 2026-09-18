# perspec-me

The vocabulary of PerSpecML-concern-guided wayfinding: a catalog-driven interview that resolves one Topic at a time and rolls the result into a durable Map toward an agreed Destination.

## Language

**Concern**:
A stable lens from the PerSpecML catalog (e.g. `O3 — ML functionality`, `D6 — Accuracy`) describing something a specification may need to address. Ships with the skill's catalog (`skills/in-progress/perspec-me/catalog/`) and is never modified, recreated, or re-scraped by a project's use of the skill.
_Avoid_: requirement, criterion (a Concern is a lens to look through, not the requirement itself — the requirement is what a Topic's resolution derives)

**Topic**:
A project-specific question or decision narrow enough to resolve in one Session (e.g. "How will the credit model be evaluated before launch?"). Many-to-many with Concern: one Topic can touch several Concerns, and one Concern can be touched by several Topics across a Map's life.
_Avoid_: issue (a Topic is the domain question itself; when it is held on the repo's **Issue tracker** it *is* a **Decision ticket** — see Relationships, and reuse that existing term rather than inventing a synonym)

**Session**:
One bounded `perspec-me` execution: it loads a Topic and only that Topic's related Concerns, interviews the user in short rounds, updates Concern Resolution pages after each round, and stops — resolving, splitting, or leaving the Topic open, but never starting implementation.
_Avoid_: run, conversation (a Session is scoped to one Topic; a single chat can span, resume, or hand off several Sessions)

**Map**:
The durable, low-resolution index toward a Destination: current understanding, decisions so far, Perspective coverage, Concern states, Frontier, Blocked, Fog, Delegated work, and out of scope. It indexes Topics and Concern states rather than holding their detail — that detail lives in Topics and Resolution pages.
_Avoid_: backlog, plan (a completed Map is not automatically a specification or an implementation plan; it hands off to a later synthesis step, e.g. `to-spec`)

**Destination**:
The agreed condition that tells a Map when its elaboration work is done (e.g. "requirements for the new training pipeline are clear enough to become implementation tickets"). Fixed and confirmed before a Map's first Topics are created.
_Avoid_: goal, definition of done (reserve those for an Issue's own acceptance criteria; Destination names this specific Map artifact)

**Fog**:
A region of the catalog known to matter but not yet sharp enough to state as a Topic's question. A Session that clarifies Fog removes the entry and creates a Topic in its place — the same understanding never sits in both sections at once.
_Avoid_: unknown unknown, backlog item

**Frontier**:
The subset of a Map's Topics that are open, unblocked, precisely enough defined, and available for the next Session — each phrased as a question, never as an implementation step.
_Avoid_: ready queue, next up (when the issue-tracker backend is in play, this is computed with the same frontier query Wayfinder already defines — see Flagged ambiguities)

**Blocked**:
A Topic that cannot enter the Frontier because it depends on another open Topic or on Delegated work still in flight. It clears once its blocker(s) close.
_Avoid_: stuck, on hold

**Resolution page**:
The project-specific synthesis for one Concern — current resolution, confirmed facts, decisions, derived requirements and constraints, open questions, evidence, and Topic history — kept under a project's own `requirements/perspec-me/<map-slug>/concerns/` layer. It never restates the catalog's generic definition, only what this project has decided.
_Avoid_: concern page, concern doc (ambiguous with the catalog's own canonical page for the Concern)

**Perspective coverage**:
A Map's summary table of how many Concerns in each of the catalog's five Perspectives sit in each Concern state, read at a glance without opening every Resolution page.
_Avoid_: progress, completion percentage (a full row of `resolved` is sufficient for the current Destination and scope, not permanent — see the `resolved` state below)

**Delegated work**:
A Research, Prototype, or Unblocking task a Map records when a Topic can't be resolved by interview alone — an external fact, a need for a working artifact to judge, or manual access/experimentation. Its result updates the Topic it unblocks, the affected Resolution pages, Fog, Frontier, and the Map.
_Avoid_: task, ticket (as a stand-in for an implementation ticket — Delegated work is never that; see the top-level **Issue** definition for the thing it explicitly is not)

**Concern state**:
The fixed vocabulary a Resolution page's `status` and a Map's Perspective coverage table draw from — one of `unexamined` (not yet considered for this project), `open` (relevant, not enough investigation yet), `partial` (some decisions made, material questions remain), `resolved` (enough understanding for the current Destination and scope — not permanent), `deferred` (deliberately postponed), `not-applicable` (examined and judged out of this project's context), or `superseded` (a later decision replaced this resolution).
_Avoid_: done, n/a, closed, skipped, wontfix (use the seven states verbatim; this is a closed set, the same way the top-level **Claim** status is)

## Relationships

- Topic N:N Concern
- Session resolves one Topic
- Map indexes Topics and Concern states
- Topic on a tracker is a Decision ticket
- Fog graduates into a Topic once it can be phrased as a precise question; the same understanding is never carried in both sections at once
- A Frontier Topic is a Map's Topic that is open, unblocked, and ready; a Blocked Topic leaves the Frontier until its blocker(s) close
- A Resolution page belongs to one Concern; Perspective coverage summarizes Resolution pages' Concern states across a Perspective
- Delegated work belongs to the Topic it unblocks

## Flagged ambiguities

- "Map", "Frontier", and "Blocked" name concepts the skills context's Wayfinder conventions (`docs/agents/issue-tracker.md`) already use for generic Issues — resolved: these are not new types. When perspec-me's issue-tracker backend is in play, its Map, Frontier, and Blocked *are* the same Wayfinder mechanics (native issue dependencies, the map's open-children query, `@me` claim), scoped to Topics instead of generic tickets; the local Markdown backend computes the same operations without a tracker. No perspec-me term redefines the Wayfinder one.
- The originating spec (issue #10, written in Portuguese) uses "assunto" for Topic, "mapa" for Map, and "sessão" for Session — resolved: this glossary, and every perspec-me artifact, uses the English terms above; the Portuguese words are not domain terms in this repo.
- "Issue", "Issue tracker", and "Decision ticket" are owned by the top-level `CONTEXT.md` — resolved: this glossary reuses them by reference (see Topic and Delegated work above) rather than restating or drifting from their definitions.
