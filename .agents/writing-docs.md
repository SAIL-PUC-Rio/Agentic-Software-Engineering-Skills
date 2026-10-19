# Writing docs pages

A promoted skill that this repo authored or substantially reworked has a human-facing **docs page** at `docs/<bucket>/<skill-name>.md`. The page is not the skill and not a copy of `SKILL.md`. Skills kept from upstream unchanged have no page; their `SKILL.md` is the documentation. Skills in `in-progress/` and `deprecated/` have no page either.

Most of these skills are **user-invoked**: the agent will never fire them for you, so *you* are the index that has to remember they exist and when to reach for them. That memory is **cognitive load**. The job of a docs page is to relieve it — to orient one reader around one skill so they can hold it in their head, know when to reach for it, and see where it sits in the system.

Act whenever a skill with a page is renamed or has its behaviour changed, or a new skill lands in a promoted bucket: create or re-sync its page. A rename moves the file too (`docs/<bucket>/<old>.md` → `docs/<bucket>/<new>.md`); a skill that moves between `engineering/` and `productivity/` moves its docs file to the matching folder. A skill moving out of a promoted bucket loses its page.

Pages are read in the repository, so **links are repo-relative**: another skill's page is `./<name>.md` (or `../<bucket>/<name>.md`), a skill itself is `../../skills/<bucket>/<name>/SKILL.md`, and a page never carries install commands. The install block lives in `README.md`, copied from [install-block.md](./install-block.md).

There is no H1 — the page takes its title from the file name.

## Page structure

Fill the template below, keeping its order. The **fixed frame** (`## What it does`, `## When to reach for it`, `## Where it fits`) appears on every page. `## Prerequisites` and the free-form substance sections carry only what this particular skill needs; delete the rest.

Four sections make a page worth reading: `What it does`, `When to reach for it`, `Common questions`, `It's working if`. The first two orient the reader; the last two are where the page stops summarising the skill and starts answering the reader's own situation.

<page-template>

## What it does

One or two plain-language paragraphs. Lead with the skill's one-sentence job, then state the **defining constraint** — the single fact that makes this skill behave differently from the obvious default (for `to-spec`: it does not interview the user again, it synthesises what is already known). Write it as a plain declarative sentence, never a labelled aside. This line is the most valuable on the page; never omit it.

## When to reach for it

How and when you reach for the skill — two beats, both effectively always present:

- **Invocation mode.** State whether you type it or the agent fires it. A user-invoked skill: "You invoke this by typing `/<name>` — the agent won't reach for it on its own." A model-invoked skill: "Type `/<name>`, or the agent reaches for it automatically when a task fits."
- **Trigger boundary.** The index entry: "reach for this when …". Where the skill is confusable with a sibling, add the other half — "for <X> instead, use [<sibling>](./<sibling>.md)."

## Prerequisites

Optional — include only when the skill needs something in place to be functional; omit the heading entirely otherwise. Covers: a **workspace it writes into**, **prior setup** (`to-spec`, `to-tickets`, `triage` need `setup-sail-skills` to have configured an issue tracker), or **repo-specific tooling**. A stateless skill that runs anywhere has no prerequisites — drop the section.

## <free-form middle>

One to three short sections, in the skill's *own vocabulary*, that make it click — the loop it runs, the artifact it produces, the fork it makes, the one anti-pattern it kills. There is no prescribed heading.

The single non-negotiable: **surface the skill's leading word / defining idea** — `evidence pack`, `tracer bullet`, `Behavioral Specification`, red-green. The reader learns what the skill *is*, and learns the word they'll later think with to *reach for* it.

## Common questions

The questions readers really ask about this skill, each in bold with the answer in the lines beneath it — no sub-headings.

An observed question always beats an invented one, so find them before you write any: `gh issue list --repo Esduard/skills --search "<skill-name>" --state all`, and the evidence packs under `.scratch/_evidence/` where a skill's own runs recorded what went wrong. Where the hunt comes up thin, the section may carry a question a reader would plainly ask, but **the count stays honest to the evidence**. Omit the heading where there is nothing worth answering.

## It's working if

A few bullets naming what the reader sees when the skill is doing its job. The bar on each is that the reader can check it without opening `SKILL.md` — a signal in their own work, or in the trace in front of them. Omit the heading where the tells stay vague.

## Where it fits

Always present. Situate the skill in the system in a sentence or two:

- **Role.** A **chain step** (`grill-with-docs → to-spec → to-tickets → implement → evidence → code-review`), a **run-once setup** (`setup-sail-skills`), or a **reach-for-it-anytime standalone**.
- **Neighbours.** The one or two siblings that matter, each with a because-clause, linked.
- **The map.** Point to [`ask-sail`](../../skills/engineering/ask-sail/SKILL.md), the router over the whole set, so this page stays a node and never has to redraw the graph.

</page-template>

## Conventions

- Explain the **why**, not the process. The page orients and situates the skill; it never reproduces the `SKILL.md` steps or template dumps.
- **Never name an author.** State the substance as a plain claim about the skill and drop the frame. Quoting a *user* anonymously is fine; it is evidence about the skill in the wild.
- Use the skill's **leading words** so the page and the skill speak one language.
- **Branches go in a table or a list, never in a paragraph.** Where the page presents a choice, the reader is scanning for the one row that matches their situation.
- Keep the page itself low-load. Furniture (spare headings, restated links) is the thing it is arguing against.

## Done when

- The page exists at `docs/<bucket>/<name>.md`, and no stale page survives a rename or bucket move.
- The page writes no install command of its own.
- `## What it does` states the defining constraint, as plain prose.
- The page names no author and quotes no author.
- `## When to reach for it` states invocation mode and the trigger boundary.
- `## Where it fits` names the role and links to `ask-sail`.
- A prerequisite is stated where one exists, and the section is absent where none does.
- The middle surfaces the leading word.
- Every multi-way branch is a table or a list.
- `## Common questions` is sized to what the hunt found, not padded.
- Every `## It's working if` bullet is checkable without opening `SKILL.md`.
- The sections appear in the template's order.
- Every link is repo-relative and resolves.
