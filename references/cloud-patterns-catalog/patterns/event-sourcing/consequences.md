# Event Sourcing — Consequences

Replay requires a starting state and retained events. Checkpoints can shorten reconstruction. External side effects may need compensation, and storage and query costs grow with history; replay is not automatically safe for external systems.

Source: [Book](../../SOURCES.md#book), “Event Sourcing,” pp. 289–298 (physical PDF 333–342), closing trade-offs. Book supplement to the website draft.

[Back to Event Sourcing](README.md)
