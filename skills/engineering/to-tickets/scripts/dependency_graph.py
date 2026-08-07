#!/usr/bin/env python3
"""Dependency graph engine for the to-tickets skill.

Reads structured ticket data — a JSON list of
``{"id": ..., "title": ..., "blocked_by": [...]}`` objects — validates the
graph, and computes a deterministic topological level assignment.

This module is the shared engine both renderers (terminal, Mermaid) build on.
It does not infer, add, or second-guess any semantic dependency: it only
validates and orders what it is given.

Importable surface:
    validate_and_level(tickets: list[dict]) -> LeveledGraph
    DependencyGraphError

CLI usage:
    python3 dependency_graph.py < tickets.json                    # plain
    python3 dependency_graph.py --format terminal < tickets.json  # diagram
    python3 dependency_graph.py --format mermaid < tickets.json   # Mermaid
    python3 dependency_graph.py --format both < tickets.json      # both

``--format both`` is the mode ``to-tickets`` actually invokes: it prints the
terminal diagram (or its degraded listing) followed by the Mermaid source,
both derived from a single ``validate_and_level()`` call.
"""

from __future__ import annotations

import argparse
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

    This is the base rendering this module ships. Terminal (#4) and Mermaid
    (#5) rendering are separate CLI ``--format`` modes that consume the same
    LeveledGraph produced by validate_and_level() instead of re-deriving
    validation or leveling.
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


# Degradation thresholds for the terminal diagram (see _needs_degraded_
# rendering). Each one is a proxy for "would the boxed diagram still be
# skimmable at a glance": too many tickets overall means too much vertical
# scroll; too many tickets in one level means the diagram can't show
# "parallel roots" as a small cluster; too much fan-out/fan-in on a single
# ticket means its "blocks:"/"blocked by:" annotation line would itself wrap
# or dominate the screen. Past any of these, a flat level+edges listing
# (already produced by _render_plain_text) stays readable while box art
# would not.
_MAX_TOTAL_TICKETS_FOR_DIAGRAM = 14
_MAX_TICKETS_PER_LEVEL_FOR_DIAGRAM = 6
_MAX_FAN_FOR_DIAGRAM = 4


def _compute_blocks_by_id(graph):
    """Reverse of blocked_by: for each ticket, which tickets it blocks.

    Returns a dict of id -> sorted tuple of dependent ticket IDs, computed
    entirely from the already-validated LeveledGraph (no re-validation).
    """
    blocks = {ticket.id: [] for ticket in graph.tickets}
    for ticket in graph.tickets:
        for blocker in ticket.blocked_by:
            blocks[blocker].append(ticket.id)
    return {ticket_id: tuple(sorted(ids)) for ticket_id, ids in blocks.items()}


def _needs_degraded_rendering(graph):
    """Decide whether the boxed diagram would stay legible for this graph.

    Pure function of the LeveledGraph — the model never has to judge this;
    the script owns the decision so the same graph always degrades (or
    doesn't) the same way.
    """
    if len(graph.tickets) > _MAX_TOTAL_TICKETS_FOR_DIAGRAM:
        return True
    if any(
        len(level) > _MAX_TICKETS_PER_LEVEL_FOR_DIAGRAM
        for level in graph.by_level()
    ):
        return True
    blocks_by_id = _compute_blocks_by_id(graph)
    for ticket in graph.tickets:
        if len(ticket.blocked_by) > _MAX_FAN_FOR_DIAGRAM:
            return True
        if len(blocks_by_id[ticket.id]) > _MAX_FAN_FOR_DIAGRAM:
            return True
    return False


def _render_ticket_box(ticket):
    """Render a single ticket as a fixed Unicode box, sized to its content."""
    label = f"{ticket.id} — {ticket.title}"
    width = len(label) + 2
    top = "┌" + "─" * width + "┐"
    middle = "│ " + label + " │"
    bottom = "└" + "─" * width + "┘"
    return [top, middle, bottom]


def _render_diagram(graph):
    """Render the graph as level-grouped boxes with blocking-direction
    annotations.

    Tickets are grouped by level (top to bottom = earlier to later in the
    dependency order, matching LeveledGraph's own (level, id) ordering).
    Each box is annotated with its incoming edges ("blocked by:") and
    outgoing edges ("blocks:") rather than drawn as connector lines —
    routing arbitrary connector lines between boxes across levels is exactly
    the kind of fragile ASCII art this format is meant to avoid, and the
    annotation form still communicates direction, fan-out, and fan-in
    unambiguously.
    """
    blocks_by_id = _compute_blocks_by_id(graph)
    lines = []
    for level_index, level_tickets in enumerate(graph.by_level()):
        lines.append(f"Level {level_index} — {len(level_tickets)} ticket(s)")
        for ticket in level_tickets:
            lines.extend(_render_ticket_box(ticket))
            if ticket.blocked_by:
                lines.append(
                    "  ◀── blocked by: " + ", ".join(sorted(ticket.blocked_by))
                )
            dependents = blocks_by_id[ticket.id]
            if dependents:
                lines.append("  └─▶ blocks: " + ", ".join(dependents))
            lines.append("")
    while lines and lines[-1] == "":
        lines.pop()
    return "\n".join(lines)


def _render_degraded_listing(graph):
    """Fallback for graphs too large/dense for the boxed diagram.

    Reuses the same deterministic level+edges listing the plain-text CLI
    format already produces, prefixed with a note explaining why the boxed
    diagram was skipped.
    """
    return (
        "Dependency graph (level + edges listing; diagram degraded for "
        "readability — see _needs_degraded_rendering):\n\n"
        + _render_plain_text(graph)
    )


def _render_terminal(graph):
    """Render a LeveledGraph for a terminal: boxed diagram, or a degraded
    level+edges listing when the graph is too large or dense to stay
    legible as boxes (see _needs_degraded_rendering).
    """
    if not graph.tickets:
        return "(no tickets)"
    if _needs_degraded_rendering(graph):
        return _render_degraded_listing(graph)
    return _render_diagram(graph)


# Characters that are structurally significant inside a Mermaid quoted node
# label (`id["..."]`) and must not reach the output literally, mapped to the
# Mermaid-documented numeric HTML entity that displays as that character
# without being re-parsed as syntax. "#" itself is escaped first-and-always
# by walking the string one character at a time (never via sequential
# str.replace calls) so an entity this function inserts — e.g. the "#" in
# "#quot;" — can never be picked up and re-escaped by a later substitution.
# Verified against the real `mermaid` npm package (v11.16.1) parser: quotes,
# brackets, parens, braces, pipe, angle brackets, and "#" all round-trip
# through this map as valid `graph TD` syntax, and the same titles fail to
# parse without it (see ticket #5 evidence pack for the verification
# transcript).
_MERMAID_LABEL_ESCAPES = {
    '"': "#quot;",
    "#": "#35;",
    "[": "#91;",
    "]": "#93;",
    "(": "#40;",
    ")": "#41;",
    "{": "#123;",
    "}": "#125;",
    "|": "#124;",
    "<": "#60;",
    ">": "#62;",
    "\n": " ",
    "\r": " ",
}


def _mermaid_escape_label(text):
    """Escape text for safe use inside a Mermaid quoted node label.

    Single left-to-right pass over ``text`` — never a chain of ``str.replace``
    calls — so an entity this function inserts (e.g. the "#" in "#quot;")
    is never itself picked up and re-escaped by a later substitution.
    """
    return "".join(_MERMAID_LABEL_ESCAPES.get(ch, ch) for ch in text)


def _mermaid_node_ids(graph):
    """Assign each ticket a safe, deterministic, unique Mermaid node ID.

    Ticket IDs are arbitrary non-empty strings (validate_and_level() places
    no other constraint on them), but Mermaid node IDs are safest as a
    restricted identifier charset. Rather than special-case which raw
    ticket IDs happen to already be safe, every node ID is derived the same
    way: keep only ASCII letters/digits/underscore from the ticket ID
    (everything else becomes "_"), always prefix with "n_" so the result
    can never start with a digit or be empty, and disambiguate any
    resulting collisions with a numeric suffix.

    Iterates graph.tickets in its existing (level, id) order, which is
    itself deterministic, so assignment is stable for a given input.

    Returns a dict of ticket id -> mermaid node id.
    """
    node_ids = {}
    used = set()
    for ticket in graph.tickets:
        sanitized = "".join(
            ch if (ch.isalnum() and ch.isascii()) or ch == "_" else "_"
            for ch in ticket.id
        )
        candidate = "n_" + sanitized
        suffix = 0
        while candidate in used:
            suffix += 1
            candidate = f"n_{sanitized}_{suffix}"
        used.add(candidate)
        node_ids[ticket.id] = candidate
    return node_ids


def _render_mermaid(graph):
    """Render a LeveledGraph as Mermaid ``graph TD`` syntax.

    Nodes are declared in the graph's existing (level, id) order (matching
    the terminal renderer's top-to-bottom reading). Edges point from
    prerequisite to dependent — i.e. for a ticket blocked by another, the
    arrow is ``blocker --> ticket`` — matching the "blocked by:"/"blocks:"
    direction the terminal renderer (#4) already uses, and are emitted in
    (ticket, sorted blocker) order, so output is fully deterministic.

    Node labels are "<id> — <title>", HTML-entity-escaped via
    _mermaid_escape_label so quotes, brackets, parens, braces, pipes, angle
    brackets, and literal "#" characters in either the ID or the title can
    never break out of the quoted label or be misread as Mermaid syntax.
    """
    node_ids = _mermaid_node_ids(graph)
    lines = ["graph TD"]
    for ticket in graph.tickets:
        label = _mermaid_escape_label(f"{ticket.id} — {ticket.title}")
        lines.append(f'    {node_ids[ticket.id]}["{label}"]')
    for ticket in graph.tickets:
        for blocker in sorted(ticket.blocked_by):
            lines.append(f"    {node_ids[blocker]} --> {node_ids[ticket.id]}")
    return "\n".join(lines)


def _render_both(graph):
    """Render terminal output followed by Mermaid source, from one graph.

    This is the mode ``to-tickets`` actually invokes. Both renderers consume
    the same already-validated-and-leveled ``graph`` — the structure is
    derived exactly once (by the caller's single validate_and_level() call);
    this function only renders it twice, in two unrelated output formats.
    """
    return _render_terminal(graph) + "\n\n" + _render_mermaid(graph)


def _parse_args(argv):
    parser = argparse.ArgumentParser(
        description=(
            "Validate and level a ticket dependency graph read as JSON "
            "from stdin."
        )
    )
    parser.add_argument(
        "--format",
        choices=["plain", "terminal", "mermaid", "both"],
        default="plain",
        help=(
            "Output format: 'plain' (default) prints one line per ticket; "
            "'terminal' prints a Unicode diagram, degrading to a "
            "level+edges listing for large or dense graphs; 'mermaid' "
            "prints Mermaid 'graph TD' source; 'both' prints the terminal "
            "output followed by the Mermaid source, from a single "
            "validated graph (this is the mode to-tickets invokes)."
        ),
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = _parse_args(sys.argv[1:] if argv is None else argv)

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

    if args.format == "terminal":
        output = _render_terminal(graph)
    elif args.format == "mermaid":
        output = _render_mermaid(graph)
    elif args.format == "both":
        output = _render_both(graph)
    else:
        output = _render_plain_text(graph)
    if output:
        print(output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
