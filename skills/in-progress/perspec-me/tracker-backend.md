# Tracker backend: the topic-store operations

ADR 0002 (topic-store seam) defines five operations — **create topic**, **claim**, **list frontier**, **record resolution**, **wire blockers** — independent of where a Topic lives. This file is the concrete mechanics for the issue-tracker backend: Topics as Wayfinder decision tickets, resolved by `perspec-me`, against a repo that has an issue tracker configured (the file `/setup-matt-pocock-skills` writes) and the Wayfinder skill available. It reuses exactly the mechanics [docs/agents/issue-tracker.md](../../../docs/agents/issue-tracker.md)'s "Wayfinding operations" section already defines — never a parallel `gh` call invented here. [local-backend.md](./local-backend.md) is this file's sibling, not a competing definition; the two implement the same five operations under the same names, for the local Markdown backend and this backend respectively.

**Every** perspec-me procedure that touches a Topic — the map-charting procedure in [map.md](./map.md), the direct-session procedure in `SKILL.md`, and the `resolve`/`resume`/`status`/`review` verbs in [work-a-map.md](./work-a-map.md) — writes against these five operations, never against an ad hoc `gh` call invented on the spot. If a step needs a sixth thing, that's a gap in this file to fix here, not a one-off workaround in the caller.

## Where things live

- **Map**: the `wayfinder:map` issue ([wayfinder/SKILL.md](../../engineering/wayfinder/SKILL.md#the-map)) — the same issue Wayfinder itself already treats as canonical for Destination, Notes, Decisions so far, Not yet specified (Fog), and Out of scope. This backend never duplicates those sections anywhere else; see [map.md](./map.md#the-map-file) for the leaner project-side file it keeps alongside the issue.
- **Topics**: child issues of that `wayfinder:map` issue, carrying `resolver: perspec-me` and `concerns:` in their body (see [Topic issue shape](#topic-issue-shape) below). **The fallback topic directory (`topics/`) is not used on this backend** — a Topic's only home is the tracker issue itself.
- **Concern Resolution pages**: `requirements/perspec-me/<map-slug>/concerns/<concern-id>.md` — plain Markdown files in the consuming project, exactly as on the local backend. ADR 0003's rule (the resolution layer lives in the project) doesn't change per-backend.
- **Perspective pages**: `requirements/perspec-me/<map-slug>/perspectives/<perspective-id>.md` — created on demand, never scaffolded for all five perspectives up front, same as the local backend.
- **Project-side Map file**: `requirements/perspec-me/<map-slug>/MAP.md`, but leaner than the local backend's — see [map.md](./map.md#the-map-file) for its tracker-backend shape (a Perspective-resolution table plus links, only).

`<map-slug>` is the same short kebab-case identifier the local backend uses (ADR 0003), chosen when the project-side Map file and its `concerns/`/`perspectives/` directories are first created, never renamed afterward. A Topic issue has no separate slug of its own — its tracker id is its identity, and Wayfinder's "Refer by name" convention applies to it exactly as to any other Wayfinder ticket: refer to it by its issue title in prose, never by a bare `#42`.

## Topic issue shape

```markdown
Part of #<map-issue-number>   <!-- only when the sub-issues API isn't enabled; docs/agents/issue-tracker.md's Child ticket fallback -->

## Question

<the Topic's question, verbatim, phrased as a question>

resolver: perspec-me
concerns:
  - <concern-id>
  - <concern-id>
```

This extends Wayfinder's own ticket body template ([wayfinder/SKILL.md](../../engineering/wayfinder/SKILL.md#tickets) — `## Question` holding the decision text) with two additional fields; it never replaces `## Question`.

**Title**: the Topic's question, verbatim — Wayfinder's "refer by name" convention applies to a perspec-me Topic exactly as to any other Wayfinder ticket.

**Labels**: Wayfinder's `wayfinder:<type>` scheme (`research`/`prototype`/`grilling`/`task`, [wayfinder/SKILL.md](../../engineering/wayfinder/SKILL.md#ticket-types)) classifies a ticket by *which of Wayfinder's own four resolution paths* applies. A `resolver: perspec-me` ticket takes none of those four — it's resolved by this skill's own interview procedure (`SKILL.md`), not by grilling, research, a prototype, or manual task work. **Perspec-me-resolved tickets are exempt from the `wayfinder:<type>` labeling scheme** — they carry no `wayfinder:<type>` label at all. The `resolver: perspec-me` body line is what identifies them, both to Wayfinder's own resolver hook and to this backend's **list frontier** query below. They still carry the ordinary child-issue relationship to the `wayfinder:map` issue like any other ticket — only the type label is skipped.

## The five operations

### create topic

`gh issue create --title "<question>" --body "<body>"` (a heredoc for the multi-line body, per [docs/agents/issue-tracker.md](../../../docs/agents/issue-tracker.md)'s general create convention), wired as a child of this Map's `wayfinder:map` issue per that doc's **Child ticket** convention: the sub-issues API where this repo has it enabled, or — where it doesn't — a task-list entry on the map issue plus a `Part of #<map>` line at the top of the new issue's body. The body is [Topic issue shape](#topic-issue-shape) above: `## Question` holding the Topic's question, plus `resolver: perspec-me` and a `concerns:` list of the Concern IDs the charting (or splitting) pass already associated with this question. Never create a Topic issue for a question that isn't precisely phraseable yet — same discipline as [local-backend.md](./local-backend.md#create-topic). No `wayfinder:<type>` label is applied (see [Topic issue shape](#topic-issue-shape) above). Wire any already-known blockers with **wire blockers** below, in a second pass, once the new issue has an id — never hand-listed in the body at creation time.

### claim

Exactly [docs/agents/issue-tracker.md](../../../docs/agents/issue-tracker.md)'s **Claim** operation: `gh issue edit <n> --add-assignee @me` — the session's first write to the Topic issue, mirroring the role [local-backend.md](./local-backend.md#claim)'s `claimed_by` field plays for the local backend. This backend does not restate or extend that mechanic with parallel rules.

### list frontier

[docs/agents/issue-tracker.md](../../../docs/agents/issue-tracker.md)'s **Frontier query** — list the map's open children, drop any with an open blocker (`issue_dependencies_summary.blocked_by > 0`) or an assignee — **restricted to children whose body carries a `resolver: perspec-me` line**. A Wayfinder map may mix perspec-me Topics with ordinary Wayfinder tickets (research/prototype/grilling/task); this backend's frontier is scoped to the ones it resolves, the same query filtered to that subset, not a second query. In practice: `gh issue list --state open --json number,title,body,assignees,issue_dependencies_summary` scoped to the map's children (the sub-issues set, or the task-list/`Part of #<map>` fallback set), keep only entries whose `body` contains a `resolver: perspec-me` line, `assignees` is empty, and `issue_dependencies_summary.blocked_by == 0` — first in map order wins, same as the tracker's own Frontier query.

### wire blockers

Native issue dependencies, exactly [docs/agents/issue-tracker.md](../../../docs/agents/issue-tracker.md)'s **Blocking** operation: `gh api --method POST repos/<owner>/<repo>/issues/<child>/dependencies/blocked_by -F issue_id=<blocker-db-id>`, where `<blocker-db-id>` is the blocker issue's numeric **database id** (`gh api repos/<owner>/<repo>/issues/<n> --jq .id` — never the `#number` or `node_id`). A Topic issue is unblocked once every issue blocking it is closed, read from `issue_dependencies_summary.blocked_by`. This is the only place a blocking edge is written for this backend, the same restriction [local-backend.md](./local-backend.md#wire-blockers) states for the local backend's `blocked_by` field.

### record resolution

When a Session closes a Topic issue, exactly [docs/agents/issue-tracker.md](../../../docs/agents/issue-tracker.md)'s **Resolve** operation, in order:

1. `gh issue comment <n> --body "<answer>"` — the resolution comment: what was decided, and which Concern(s) it touched.
2. `gh issue close <n>`.
3. Append a context pointer (the Topic issue's name, wrapping its link, plus a one-line gist) to the Wayfinder map issue's own **Decisions so far** section — an edit to the map issue's own body, which the map already owns and updates as part of its own lifecycle ([wayfinder/SKILL.md](../../engineering/wayfinder/SKILL.md#work-through-the-map) step 4), not a write this backend performs to a *Topic* issue beyond comment/close.

Backend-independent, per ADR 0003: in each Concern the Topic touched, update `requirements/perspec-me/<map-slug>/concerns/<concern-id>.md` using the same create-once/append-after rule the local backend and the direct-session procedure already use (`SKILL.md` section d; [local-backend.md](./local-backend.md#record-resolution) step 3) — create the page only the first time that Concern is touched under this Map, otherwise append to its existing synthesis, never overwrite it wholesale.

## Remote-write discipline

This backend performs exactly four kinds of remote write, ever, without asking the user first:

1. **Claim** — `gh issue edit <n> --add-assignee @me`.
2. **Comment** — `gh issue comment <n> --body "..."` (a resolution comment, or a split aggregator's child-issue-links comment — see [work-a-map.md](./work-a-map.md#alternative-outcomes)).
3. **Close** — `gh issue close <n>`.
4. **Create** — `gh issue create ...` for a new Topic issue (including the Map's own `wayfinder:map` issue, per [wayfinder/SKILL.md](../../engineering/wayfinder/SKILL.md#chart-the-map)'s charting procedure), and the one-time `dependencies/blocked_by` POST that wires a newly-created issue's blockers.

**Anything else requires the user's explicit authorization in-conversation before it runs** — naming a few concretely: editing a ticket's body after creation, changing a label beyond whatever **create topic** sets once at creation time, deleting an issue, reopening a closed one, editing an existing comment, removing an assignee. This mirrors ADR 0002/0003's read-only-catalog discipline, applied to the remote tracker: the four writes above are this seam's entire footprint on the consuming project's issue tracker; nothing else happens without the user saying so.
