"""Tests for the ``--format terminal`` renderer in dependency_graph.py.

Kept separate from test_dependency_graph.py (which covers validation and
leveling) so rendering-specific tests don't bloat that file.

Run with:
    python3 -m unittest test_dependency_graph_terminal

from the scripts directory, or via ``unittest discover``.
"""

from __future__ import annotations

import os
import subprocess
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from dependency_graph import (  # noqa: E402
    _needs_degraded_rendering,
    _render_terminal,
    validate_and_level,
)

SCRIPT_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "dependency_graph.py"
)


class ChainTerminalTest(unittest.TestCase):
    def test_linear_chain_renders_boxes_with_blocked_by_direction(self):
        tickets = [
            {"id": "a", "title": "A", "blocked_by": []},
            {"id": "b", "title": "B", "blocked_by": ["a"]},
            {"id": "c", "title": "C", "blocked_by": ["b"]},
        ]
        graph = validate_and_level(tickets)
        self.assertFalse(_needs_degraded_rendering(graph))
        output = _render_terminal(graph)

        # IDs and titles are present.
        self.assertIn("a — A", output)
        self.assertIn("b — B", output)
        self.assertIn("c — C", output)
        # Blocking direction is shown for each non-root ticket.
        self.assertIn("blocked by: a", output)
        self.assertIn("blocked by: b", output)
        # It's actual box-drawn diagram output, not the degraded listing.
        self.assertIn("┌", output)
        self.assertNotIn("diagram degraded", output)


class FanOutTerminalTest(unittest.TestCase):
    def test_fan_out_shows_blocks_annotation_on_the_blocking_ticket(self):
        # a blocks both b and c.
        tickets = [
            {"id": "a", "title": "A", "blocked_by": []},
            {"id": "b", "title": "B", "blocked_by": ["a"]},
            {"id": "c", "title": "C", "blocked_by": ["a"]},
        ]
        graph = validate_and_level(tickets)
        output = _render_terminal(graph)

        self.assertIn("blocks: b, c", output)
        self.assertIn("blocked by: a", output)


class FanInTerminalTest(unittest.TestCase):
    def test_fan_in_lists_all_blockers_on_the_blocked_ticket(self):
        # d is blocked by both a and b.
        tickets = [
            {"id": "a", "title": "A", "blocked_by": []},
            {"id": "b", "title": "B", "blocked_by": []},
            {"id": "d", "title": "D", "blocked_by": ["a", "b"]},
        ]
        graph = validate_and_level(tickets)
        output = _render_terminal(graph)

        self.assertIn("blocked by: a, b", output)


class MultipleRootsTerminalTest(unittest.TestCase):
    def test_multiple_roots_share_level_zero_with_no_blocked_by_line(self):
        tickets = [
            {"id": "a", "title": "A", "blocked_by": []},
            {"id": "b", "title": "B", "blocked_by": []},
            {"id": "c", "title": "C", "blocked_by": []},
        ]
        graph = validate_and_level(tickets)
        output = _render_terminal(graph)

        self.assertIn("Level 0 — 3 ticket(s)", output)
        self.assertNotIn("blocked by:", output)


class TerminalDeterminismTest(unittest.TestCase):
    def test_same_input_produces_byte_identical_output(self):
        tickets = [
            {"id": "c", "title": "C", "blocked_by": ["a", "b"]},
            {"id": "a", "title": "A", "blocked_by": []},
            {"id": "b", "title": "B", "blocked_by": ["a"]},
        ]
        first = _render_terminal(validate_and_level(tickets))
        second = _render_terminal(validate_and_level(tickets))
        self.assertEqual(first, second)


class DegradedRenderingTest(unittest.TestCase):
    def test_high_fan_out_triggers_degraded_listing(self):
        # One root ticket blocks 6 others - exceeds the fan-out threshold
        # even though the graph is small and shallow.
        tickets = [{"id": "root", "title": "Root", "blocked_by": []}]
        for i in range(6):
            tickets.append(
                {
                    "id": f"child{i}",
                    "title": f"Child {i}",
                    "blocked_by": ["root"],
                }
            )
        graph = validate_and_level(tickets)
        self.assertTrue(_needs_degraded_rendering(graph))

        output = _render_terminal(graph)
        self.assertIn("diagram degraded", output)
        self.assertNotIn("┌", output)
        # Degraded output is still a deterministic level+edges listing.
        self.assertIn("level 0: root", output)
        self.assertIn("level 1: child0", output)

    def test_large_ticket_count_triggers_degraded_listing(self):
        # A long linear chain: shallow fan-out/fan-in, but enough total
        # tickets that per-ticket boxes would no longer be skimmable.
        tickets = [{"id": "t0", "title": "T0", "blocked_by": []}]
        for i in range(1, 20):
            tickets.append(
                {
                    "id": f"t{i}",
                    "title": f"T{i}",
                    "blocked_by": [f"t{i - 1}"],
                }
            )
        graph = validate_and_level(tickets)
        self.assertTrue(_needs_degraded_rendering(graph))

        output = _render_terminal(graph)
        self.assertIn("diagram degraded", output)
        self.assertNotIn("┌", output)

    def test_degraded_output_is_also_byte_identical_across_runs(self):
        tickets = [{"id": "root", "title": "Root", "blocked_by": []}]
        for i in range(6):
            tickets.append(
                {
                    "id": f"child{i}",
                    "title": f"Child {i}",
                    "blocked_by": ["root"],
                }
            )
        first = _render_terminal(validate_and_level(tickets))
        second = _render_terminal(validate_and_level(tickets))
        self.assertEqual(first, second)


class TerminalCliTest(unittest.TestCase):
    def _run_cli(self, stdin_text, extra_args=()):
        return subprocess.run(
            [sys.executable, SCRIPT_PATH, *extra_args],
            input=stdin_text,
            capture_output=True,
            text=True,
        )

    def test_format_terminal_flag_prints_diagram_to_stdout(self):
        tickets = (
            '[{"id": "a", "title": "A", "blocked_by": []}, '
            '{"id": "b", "title": "B", "blocked_by": ["a"]}]'
        )
        result = self._run_cli(tickets, ["--format", "terminal"])
        self.assertEqual(result.returncode, 0)
        self.assertIn("a — A", result.stdout)
        self.assertIn("blocked by: a", result.stdout)

    def test_default_format_is_unchanged_plain_listing(self):
        tickets = '[{"id": "a", "title": "A", "blocked_by": []}]'
        result = self._run_cli(tickets)
        self.assertEqual(result.returncode, 0)
        self.assertIn("level 0: a — A", result.stdout)


if __name__ == "__main__":
    unittest.main()
