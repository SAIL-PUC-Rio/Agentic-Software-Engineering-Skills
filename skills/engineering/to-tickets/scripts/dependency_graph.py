#!/usr/bin/env python3
"""Dependency graph engine for the to-tickets skill.

Reads structured ticket data — a JSON list of
``{"id": ..., "title": ..., "blocked_by": [...]}`` objects — validates the
graph, and computes a deterministic topological level assignment.

This module is the shared engine both renderers (terminal, Mermaid) build on
in later tickets. It does not infer, add, or second-guess any semantic
dependency: it only validates and orders what it is given.

Importable surface:
    validate_and_level(tickets: list[dict]) -> LeveledGraph
    DependencyGraphError

CLI usage:
    python3 dependency_graph.py < tickets.json

Later tickets (terminal rendering, Mermaid export) are expected to add
``--format`` flags to the CLI below that branch on the same LeveledGraph
this module already produces, rather than re-deriving validation or leveling.
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass


class DependencyGraphError(ValueError):
    """Raised when ticket input fails validation.

    The message is written to be shown directly to a human — it names the
    offending ticket ID(s) and explains what's wrong, so callers can surface
    it as-is instead of silently misrendering a broken graph.
    """


@dataclass(frozen=True)
class LeveledTicket:
    """A single validated ticket, with its computed topological level."""

    id: str
    title: str
    blocked_by: tuple
    level: int


@dataclass(frozen=True)
class LeveledGraph:
    """A validated ticket graph, ordered deterministically.

    ``tickets`` is sorted by (level, id) — ascending level, then ascending
    ticket ID within a level — so the same input always yields the same
    output order, independent of dict/set iteration order.
    """

    tickets: tuple

    def by_level(self):
        """Group tickets into a list of lists, one per level, level order.

        Within each level, tickets are ordered by ID (ascending), matching
        the order of ``tickets``.
        """
        if not self.tickets:
            return []
        groups = []
        current_level = None
        current_group = []
        for ticket in self.tickets:
            if ticket.level != current_level:
                if current_group:
                    groups.append(current_group)
                current_group = []
                current_level = ticket.level
            current_group.append(ticket)
        if current_group:
            groups.append(current_group)
        return groups


def _require_ticket_shape(raw, index):
    if not isinstance(raw, dict):
        raise DependencyGraphError(
            f"Ticket at position {index} must be a JSON object with "
            "'id', 'title', and 'blocked_by' fields."
        )
    ticket_id = raw.get("id")
    if not isinstance(ticket_id, str) or not ticket_id:
        raise DependencyGraphError(
            f"Ticket at position {index} is missing a non-empty string 'id'."
        )
    title = raw.get("title")
    if not isinstance(title, str):
        raise DependencyGraphError(
            f"Ticket '{ticket_id}' is missing a string 'title'."
        )
    blocked_by = raw.get("blocked_by", [])
    if not isinstance(blocked_by, list) or not all(
        isinstance(b, str) for b in blocked_by
    ):
        raise DependencyGraphError(
            f"Ticket '{ticket_id}' has an invalid 'blocked_by' — it must be "
            "a list of ticket ID strings."
        )
    return ticket_id, title, blocked_by


def validate_and_level(tickets):
    """Validate a ticket graph and compute a deterministic level assignment.

    Args:
        tickets: a list of dicts, each with 'id', 'title', and 'blocked_by'
            (a list of ticket IDs that must complete before this one).

    Returns:
        A LeveledGraph whose tickets are sorted by (level, id).

    Raises:
        DependencyGraphError: on duplicate IDs, unknown blocker references,
            self-dependencies, or dependency cycles. The message identifies
            the offending ticket(s) by ID.
    """
    if not isinstance(tickets, list):
        raise DependencyGraphError(
            "Input must be a JSON array of ticket objects."
        )

    parsed = []
    seen_ids = set()
    duplicate_ids = []
    for index, raw in enumerate(tickets):
        ticket_id, title, blocked_by = _require_ticket_shape(raw, index)
        if ticket_id in seen_ids:
            duplicate_ids.append(ticket_id)
        seen_ids.add(ticket_id)
        parsed.append((ticket_id, title, blocked_by))

    if duplicate_ids:
        unique_duplicates = sorted(set(duplicate_ids))
        raise DependencyGraphError(
            "Duplicate ticket ID(s): "
            + ", ".join(f"'{d}'" for d in unique_duplicates)
            + " — each ticket ID must be unique."
        )

    all_ids = {ticket_id for ticket_id, _, _ in parsed}

    # Check self-dependencies and unknown blockers in a deterministic
    # (ID-sorted) order so the first error reported is stable across runs.
    for ticket_id, _, blocked_by in sorted(parsed, key=lambda t: t[0]):
        for blocker in blocked_by:
            if blocker == ticket_id:
                raise DependencyGraphError(
                    f"Ticket '{ticket_id}' lists itself in 'blocked_by' — "
                    "a ticket cannot block itself."
                )
            if blocker not in all_ids:
                raise DependencyGraphError(
                    f"Ticket '{ticket_id}' has an unknown blocker "
                    f"'{blocker}' — no ticket with that ID exists."
                )

    blockers_by_id = {
        ticket_id: blocked_by for ticket_id, _, blocked_by in parsed
    }

    UNVISITED, VISITING, DONE = 0, 1, 2
    state = {ticket_id: UNVISITED for ticket_id, _, _ in parsed}
    level_by_id = {}

    def compute_level(ticket_id, stack):
        if state[ticket_id] == DONE:
            return level_by_id[ticket_id]
        if state[ticket_id] == VISITING:
            cycle_start = stack.index(ticket_id)
            cycle = stack[cycle_start:] + [ticket_id]
            raise DependencyGraphError(
                "Dependency cycle detected: " + " -> ".join(cycle)
            )
        state[ticket_id] = VISITING
        stack.append(ticket_id)
        lvl = 0
        for blocker in blockers_by_id[ticket_id]:
            lvl = max(lvl, 1 + compute_level(blocker, stack))
        stack.pop()
        state[ticket_id] = DONE
        level_by_id[ticket_id] = lvl
        return lvl

    # Iterate in sorted ID order so cycle/level computation order — and
    # therefore which cycle gets reported first — is deterministic.
    for ticket_id in sorted(state.keys()):
        compute_level(ticket_id, [])

    titles_by_id = {ticket_id: title for ticket_id, title, _ in parsed}
    leveled = [
        LeveledTicket(
            id=ticket_id,
            title=titles_by_id[ticket_id],
            blocked_by=tuple(blockers_by_id[ticket_id]),
            level=level_by_id[ticket_id],
        )
        for ticket_id in blockers_by_id
    ]
    leveled.sort(key=lambda t: (t.level, t.id))
    return LeveledGraph(tickets=tuple(leveled))


def _render_plain_text(graph):
    """Default CLI output: one line per ticket, grouped by level.

    This is intentionally the only rendering this module ships. Terminal
    (#4) and Mermaid (#5) rendering are separate, later CLI ``--format``
    modes that consume the same LeveledGraph produced by
    validate_and_level() instead of re-deriving validation or leveling.
    """
    lines = []
    for group in graph.by_level():
        for ticket in group:
            blocked_by = ", ".join(ticket.blocked_by) if ticket.blocked_by else "-"
            lines.append(
                f"level {ticket.level}: {ticket.id} — {ticket.title} "
                f"(blocked by: {blocked_by})"
            )
    return "\n".join(lines)


def main(argv=None):
    raw = sys.stdin.read()
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        print(f"Error: invalid JSON on stdin: {exc}", file=sys.stderr)
        return 1

    try:
        graph = validate_and_level(data)
    except DependencyGraphError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    output = _render_plain_text(graph)
    if output:
        print(output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
