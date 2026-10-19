# Stateless Application

<!-- pattern: stateless-application -->

Handle concurrent requests and recover from process failures without keeping essential data inside the application instance.

Aliases / draft labels: None recorded.

The draft stores session state in a backend service; the book emphasizes client-held session context passed in requests. Both keep durable domain state outside application processes.

## Read one aspect

- [Context — when it applies](context.md)
- [Problem — the design question](problem.md)
- [Forces — competing constraints](forces.md)
- [Solution — what to change](solution.md)
- [Sketch — structure at a glance](sketch.md)
- [Results — the resulting design](results.md)
- [Consequences — benefits and costs](consequences.md)
- [Related patterns — where to go next](related-patterns.md)
- [Examples — source illustrations](examples.md)

## Sources

Introduction: [book list](../../SOURCES.md#book), printed iv; expanded book discussion pp. 80–88 (physical PDF 124–132). [Website draft](https://kgb1001001.github.io/cloudadoptionpatterns/Cloud-Native-Application-Considerations/Stateless-Application/).

[Pattern index](../../INDEX.md) · [Source reconciliation](../../INVENTORY.md#stateless-application) · [Catalog](../../README.md)
