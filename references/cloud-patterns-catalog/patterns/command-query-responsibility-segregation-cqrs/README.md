# Command Query Responsibility Segregation (CQRS)

<!-- pattern: command-query-responsibility-segregation-cqrs -->

Separate query and update responsibilities so each can serve its own access and throughput needs.

Aliases / draft labels: CQRS; Command Query Responsibility Separation

The website uses Separation rather than Segregation and emphasizes coexistence with a legacy write model. The book emphasizes concurrent queries and updates and presents a two-database design.

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

Introduction: [book list](../../SOURCES.md#book), printed ii; expanded book discussion pp. 382–392 (physical PDF 426–436). [Website draft](https://kgb1001001.github.io/cloudadoptionpatterns/Coexistence-Patterns/Command-Query-Responsibility-Separation/).

[Pattern index](../../INDEX.md) · [Source reconciliation](../../INVENTORY.md#command-query-responsibility-segregation-cqrs) · [Catalog](../../README.md)
