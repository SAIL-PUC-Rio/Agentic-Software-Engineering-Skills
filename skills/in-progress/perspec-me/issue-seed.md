# Issue seed: treating an existing issue as this skill's input

This is the procedure `SKILL.md`'s routing section hands off to when a bare seed is recognized as a reference to an **existing issue** rather than free text. An issue-seed is not a special mode of `perspec-me` — it is one more way a seed arrives. Every step below ends by handing the extracted question to the exact same [fit-in-one-session decision](./map.md#fit-in-one-session-decision) any other seed goes through; this file only adds the classification work that has to happen *before* that decision can run, because an issue (unlike a freshly typed question) might already be covered by an existing Map, an existing Topic, or might not even be phrased as a question yet.

## Recognizing an issue-seed

A bare `<seed>` is an **issue-seed** when it is one of:

- a bare integer (`42`),
- a `#`-prefixed reference (`#42`), or
- a URL matching this repo's issue-tracker pattern from [docs/agents/issue-tracker.md](../../../docs/agents/issue-tracker.md) (a GitHub issue URL for the repo `gh` resolves via `git remote -v`, e.g. `https://github.com/<owner>/<repo>/issues/42`).

Anything else — prose, a pasted paragraph, a question, a half-written doc excerpt — is a plain seed and never goes through this file, even if it happens to mention an issue number in passing. The distinction is structural (does the whole seed *resolve to* one issue reference) not semantic (does it *talk about* an issue).

## Hard ordering rule: read first, ask nothing yet

Before any question goes to the user — before even stating the extracted decision question — fetch the issue in full: `gh issue view <n> --comments` (per [docs/agents/issue-tracker.md](../../../docs/agents/issue-tracker.md)), reading the body and **every** comment. This is not "good practice, do it early" — it is an ordering rule: no round, no clarifying question, no restating of what the issue "probably means" happens until this read has completed. An issue's comments routinely contain the clarification, scope-narrowing, or reversal that the body alone would get wrong (see issue #31's own comment thread in this repo for an example of a comment materially changing what the issue means).

## Investigate

Once the issue is read, look at the related code and docs it references or plausibly touches, before interviewing anyone — this is the same "investigate" step the direct-session procedure already runs ([SKILL.md](./SKILL.md#b-investigate)), just seeded by the issue's content instead of a typed question. Bring back what already exists: prior art, an already-shipped partial answer, a CONTEXT.md/ADR entry that bears on it, a related closed issue. An issue-seed frequently references specific files or a specific prior decision by name — follow those references before forming the extracted question below, not after.

## Extract the underlying decision question

An issue's title and body are frequently phrased as a **task** or a **proposed solution** ("Add caching to the search endpoint," "Promote the widget to the new pipeline") rather than as a **question**. This skill's job is not to accept the issue's phrasing at face value — it is to extract the decision the issue presupposes, the same way a Topic is always phrased as a question ([CONTEXT.md](./CONTEXT.md)'s Topic definition), never as a task.

**Worked example (illustrative — not a real issue in this repo):** an issue titled "Add caching to the search endpoint," with a body that jumps straight to implementation ("use Redis, 5-minute TTL, invalidate on reindex") is not itself a Topic. The decision it presupposes is: *should search results be cached at all, and if so, with what invalidation strategy and staleness tolerance?* "Redis, 5-minute TTL" is one candidate answer to that question, smuggled into the issue as if it were already settled — extracting the question surfaces that it wasn't.

Do this extraction for every issue-seed before doing anything else with it. State the extracted question in the skill's own words — not a copy-paste of the issue title — so a reader can immediately see the difference between what the issue asked for and what decision it actually turns on.

## Locate the related Concerns

Reuse the exact progressive-disclosure discipline from [SKILL.md section a](./SKILL.md#a-load-the-catalog-by-progressive-disclosure) / [map.md's low-resolution catalog read](./map.md#low-resolution-catalog-read): read `catalog/README.md`, then only the `README.md` of the Perspective(s) the extracted question plausibly touches, then (only once map/session scope is already decided) the individual Concern folders that plausibly bear on it. Never open a Concern folder, and never open more than one or two Perspectives' READMEs, just because an issue could plausibly touch many — the same restraint applies whether the seed came from typed prose or from an issue.

**When nothing plausibly fits:** state that plainly instead of forcing a mapping. Not every issue in a project using `perspec-me` turns on an ML-system-specification question the catalog's five Perspectives cover (see the smoke test below for a real example of this). A thin or absent Concern mapping does not block classification below — it is itself part of what gets reported to the user.

## State before acting

Before running any classification below, state to the user, in this order:

1. The extracted decision question (in the skill's own words).
2. The Concern(s) it maps to, named and linked into the catalog — or an explicit "no Concerns from the catalog plausibly apply, and here's why" if the low-resolution pass above turned up nothing.

Only after stating both does classification (below) or the fit-in-one-session decision run. This ordering is the acceptance criterion, not a style preference: an issue-seed must never be silently classified and acted on before the human has seen what the skill extracted from it.

## Classify the issue

Exactly one of four outcomes — never left unclassified, never split across two:

- **Seed for a new Map** — no existing Map's Destination plausibly covers this issue's decision (including the case where no Map exists yet at all in this project). Proceed exactly as any other seed would: run the [fit-in-one-session decision](./map.md#fit-in-one-session-decision) using the extracted question as the seed text, and follow wherever it leads (direct session or map-charting). The issue's origin changes nothing else about this path.
- **A Topic to add to an existing Map** — an existing Map's Destination plausibly covers this issue's decision, **and** no existing Topic (open or resolved) already asks substantially this question. Run [**create topic**](./local-backend.md#create-topic) under that Map for the extracted question — phrased as a question, never as the issue's literal task wording — and [**wire blockers**](./local-backend.md#wire-blockers) for any dependency the issue itself names or that's already apparent (e.g. an issue's own "Blocked by" list, where those blockers correspond to Topics already tracked on the Map). **State explicitly that this does not start a new Map.**
- **Evidence attached to an existing Topic** — an existing Topic (open, or resolved if the issue adds a genuinely new angle) already asks substantially this question, or a Concern Resolution page already covers this ground. Fold the issue's content in as evidence using the exact same create-once/append-after persistence rule as everywhere else in this skill ([SKILL.md section d](./SKILL.md#d-persist-after-every-answer)) — into the more specific of the matching Topic's own Notes or the relevant Concern Resolution page's **Evidence** section. **State explicitly that this does not create a new Topic.**
- **A premature implementation attempt** — the issue jumps straight to "how" (a specific mechanism, library, file layout, or config) without a settled "whether/what," the same smuggled-answer pattern the worked example above shows. Push it back to the decision level: state the decision question the issue presupposes (the same extraction as above) and treat *that* question as the seed going forward — through whichever of the three outcomes above it actually resolves to — instead of the issue's literal ask. **Never silently implement the issue's proposed solution, and never silently accept it as an already-settled decision** just because the issue is phrased that way.

These four are meant to be distinguishable, not a spectrum to eyeball: the first two turn on whether a covering Map already exists; the third turns on whether the *same question* (not just an adjacent one) already has a home; the fourth turns on whether the issue itself has skipped the decision, regardless of whether a Map exists yet. An issue can only land in the fourth bucket *before* the first three are even evaluated, because the first three all assume there's a decision question to place — the fourth is what happens when there isn't one yet, only a proposed answer.

## Then apply the fit-in-one-session decision

Once classified as **new-map-seed**, hand the extracted question straight to [map.md's fit-in-one-session decision](./map.md#fit-in-one-session-decision) — no issue-specific variant of that decision exists; `map.md` already says the seed's origin "makes no difference." The **add-to-existing-map** and **evidence** outcomes above skip this decision entirely (there is no fit question left to ask — the territory is already a Map or already a Topic). The **push-back** outcome defers to whichever of the other three the pushed-back question resolves to.

## Remote-issue safety

Hard rule, no exceptions absent explicit authorization: the GitHub issue itself — its title, body, labels, comments, or state — is **never modified** by this procedure. No comment posted, no label added or removed, no edit, no close. This holds regardless of outcome: even when the issue clearly becomes a Topic on a Map, the issue on the tracker is left exactly as read. The only exception is the user explicitly authorizing a specific edit in the conversation — and even then, that authorization covers only what was asked, not a general license to keep writing to the issue.

There is no mandatory "revised issue" artifact this procedure produces. The outcome is the updated Map/Topic/Resolution-page state in the project's own `requirements/perspec-me/` layer — never a rewritten issue body, and never a comment summarizing the session back onto the tracker, unless the user asks for exactly that.

**Note on "Decision ticket":** the top-level [CONTEXT.md](../../../CONTEXT.md) defines a **Decision ticket** as a Topic already living on an issue tracker (a Wayfinder child issue) — this skill's own [CONTEXT.md](./CONTEXT.md) relates the two terms directly ("Topic on a tracker is a Decision ticket"). That relationship describes the future issue-tracker backend (issue #21), where a Topic *is* a tracked issue. For this procedure, an issue read as a seed is always just a seed's source text — plain evidence to extract a question from — regardless of whether that issue happens to already look like a Decision ticket in its own right. Distinguishing "this issue already functions as a Wayfinder Decision ticket" from "this issue is ordinary tracker content being read as a seed" is issue #21's job, not this one's.
