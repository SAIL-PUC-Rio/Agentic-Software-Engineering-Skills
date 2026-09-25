# Sources and attribution

[Catalog](README.md) · [Inventory](INVENTORY.md) · [Website-only material](WEBSITE-ONLY.md)

## Book

Kyle Brown, Bobby Woolf, and Joseph Yoder, *Cloud Application Architecture Patterns: Designing, Building, and Modernizing for the Cloud*, O’Reilly Media, first edition, April 2025; first release 2025-04-15. Print ISBN 978-1-098-11690-3. The supplied PDF contains 650 physical pages. Edition and copyright details were inspected on physical page 10; the title page is physical page 9. [Publisher reading edition](https://learning.oreilly.com/library/view/cloud-application-architecture/9781098116897/).

The List of Patterns occupies printed **i–iv**, physical PDF **3–6**, including the List of Supporting Patterns on iv. Arabic book page **1** is physical PDF **45**; for the cited chapters, physical PDF page = printed page + 44. These are one-based viewer positions. The list is physically before the title and copyright pages; later front matter does not use the same offset as the list.

The list contains 70 main entries and six supporting entries. Repositories appears in both lists, yielding **75 canonical patterns**, not 76. The supporting-list description for Repositories agrees with the body; the conflicting main-list description is recorded in the inventory. The list determines names, membership, and the original paraphrases used as introductions. Chapter headings determine navigation groups only.

The PDF copyright notice reserves rights to Kyle Brown, Bobby Woolf, and Joseph Yoder Enterprises. This catalog contains brief original summaries and source pointers. The user's local PDF is research input, ignored by the catalog's `.gitignore`, and is not part of the deliverable. No extracted chapters or reproduced book figures are included. The inspected PDF SHA-256 is `20b27da705ff2072d7df60cc43b7fca218ba37eee96ec882327e22586c8fcbe0`.

## Website

[Cloud Adoption Patterns](https://kgb1001001.github.io/cloudadoptionpatterns/) is the authors' draft site. Retrieved and compared on **2026-09-19**. Its [source repository](https://github.com/kgb1001001/cloudadoptionpatterns/tree/dbb57a1) was inspected at revision `dbb57a1`; all 50 mapped draft URLs returned HTTP 200 on that date. The inventory uses 50 mapped drafts and 25 book fallbacks. The short Global Configs draft is mapped to Configuration Database, with the book supplying its missing detail. Several Cloud-Native Application Considerations drafts and Bounded Context are present even though the homepage navigation omits them.

The homepage identifies these as early drafts and says Organization, Security, and DevOps patterns were omitted from the book. It gives a May 20, 2025 release date, whereas the PDF copyright page specifies the April first edition and April 15 first release. Both observations are retained rather than treated as different catalog editions.

Expanded summaries use the mapped website draft first. Book-only patterns and aspects insufficiently covered by a draft use an explicitly cited book fallback or supplement. A related predecessor is not automatically an exact alias: the inventory describes substantive differences. Sources are identified per aspect; the book reference is also supplied to let readers compare the final treatment with the draft. The sources often express aspects in unlabelled prose; the catalog's section divisions are editorial.

No repository license file or explicit reusable-content license was found in the inspected website source; the repository API reported no license. Links to original draft figures preserve access without redistributing them. Text diagrams in this catalog are identified as editorial adaptations. This observation is not a legal determination.

## Boundaries and known differences

- Circuit Breaker, Results Cache, Service Mesh, and many operational drafts are outside book-list membership, even when mentioned inside the book. See the [unmapped draft inventory](WEBSITE-ONLY.md).
- The website's Extract Component and Add Façade requires a facade; the final Extract Component pattern makes the facade optional and permits recursive extraction.
- The Stateless Application draft keeps session state in a backend store; the book emphasizes passing client-maintained session context in each request. Both externalize durable domain state. The catalog records the book's more specific client/session distinction.
- Application Runtime is a predecessor of Application Package, Event Consumer covers only part of Reactive Component, and Event Topic Registry covers only part of Event API. Their book supplements are necessary to describe the final patterns accurately.
- The columnar-store draft favors stable schemas while the book groups semi-structured and wide-column examples under Columnar Database. The catalog preserves that ambiguity and avoids treating all examples as identical storage engines.
- Draft examples and product names are historical source illustrations, not claims about current product offerings.
- Related-pattern links summarize source-stated relationships. Editorial diagrams are labelled; reciprocal relationships are not inferred.

## File contract

The reader index contains one sentence per canonical pattern. Landing pages hold the name, aliases, introduction, available-aspect links, explicit gaps and source pointers. Aspect pages identify their pattern, cover one aspect, cite the source passage, and link back. Source page ranges include shared boundary pages where one pattern ends and the next begins. Supporting patterns can be embedded in a larger pattern's discussion; their gap notes identify the limited treatment.

`inventory.json` is the coverage inventory used by the checker, not a runtime loader. The Markdown inventory supplies a readable reconciliation record. The existing PerSpecML checker checks target existence but deliberately strips anchors and does not check inventory or citations; this catalog keeps its small inline-link approach and adds those required checks.
