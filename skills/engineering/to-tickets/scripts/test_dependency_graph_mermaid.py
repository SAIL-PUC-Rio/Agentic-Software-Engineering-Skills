"""Tests for the ``--format mermaid`` and ``--format both`` renderers in
dependency_graph.py.

Kept separate from test_dependency_graph.py (validation/leveling) and
test_dependency_graph_terminal.py (terminal rendering) so each rendering
mode's tests stay focused, matching the split those two files already
established.

Run with:
    python3 -m unittest test_dependency_graph_mermaid

from the scripts directory, or via ``unittest discover``.
"""

from __future__ import annotations

import os
import subprocess
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from dependency_graph import (  # noqa: E402
    _mermaid_escape_label,
    _render_both,
    _render_mermaid,
    _render_terminal,
    validate_and_level,
)

SCRIPT_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "dependency_graph.py"
)


class BasicMermaidRenderTest(unittest.TestCase):
    def test_linear_chain_renders_graph_td_with_nodes_and_edges(self):
        tickets = [
            {"id": "a", "title": "A", "blocked_by": []},
            {"id": "b", "title": "B", "blocked_by": ["a"]},
        ]
        graph = validate_and_level(tickets)
        output = _render_mermaid(graph)

        lines = output.splitlines()
        self.assertEqual(lines[0], "graph TD")
        # Node declarations carry id and title.
        self.assertIn('["a — A"]', output)
        self.assertIn('["b — B"]', output)
        # Edge points from prerequisite (a) to dependent (b): a --> b.
        self.assertRegex(output, r"\bn_a --> n_b\b")

    def test_fan_out_edges_point_from_blocker_to_each_dependent(self):
        # a blocks both b and c: two separate edges, both starting at a.
        tickets = [
            {"id": "a", "title": "A", "blocked_by": []},
            {"id": "b", "title": "B", "blocked_by": ["a"]},
            {"id": "c", "title": "C", "blocked_by": ["a"]},
        ]
        graph = validate_and_level(tickets)
        output = _render_mermaid(graph)

        self.assertRegex(output, r"\bn_a --> n_b\b")
        self.assertRegex(output, r"\bn_a --> n_c\b")

    def test_fan_in_emits_one_edge_per_blocker(self):
        # d is blocked by both a and b: two edges arrive at d.
        tickets = [
            {"id": "a", "title": "A", "blocked_by": []},
            {"id": "b", "title": "B", "blocked_by": []},
            {"id": "d", "title": "D", "blocked_by": ["a", "b"]},
        ]
        graph = validate_and_level(tickets)
        output = _render_mermaid(graph)

        self.assertRegex(output, r"\bn_a --> n_d\b")
        self.assertRegex(output, r"\bn_b --> n_d\b")

    def test_root_ticket_has_no_incoming_edge(self):
        tickets = [{"id": "a", "title": "A", "blocked_by": []}]
        graph = validate_and_level(tickets)
        output = _render_mermaid(graph)

        self.assertIn('n_a["a — A"]', output)
        self.assertNotIn("-->", output)

    def test_empty_graph_still_produces_valid_minimal_source(self):
        graph = validate_and_level([])
        output = _render_mermaid(graph)
        self.assertEqual(output, "graph TD")


class MermaidEscapingTest(unittest.TestCase):
    def test_escape_helper_maps_each_reserved_character_to_its_entity(self):
        self.assertEqual(_mermaid_escape_label('"'), "#quot;")
        self.assertEqual(_mermaid_escape_label("#"), "#35;")
        self.assertEqual(_mermaid_escape_label("["), "#91;")
        self.assertEqual(_mermaid_escape_label("]"), "#93;")
        self.assertEqual(_mermaid_escape_label("("), "#40;")
        self.assertEqual(_mermaid_escape_label(")"), "#41;")
        self.assertEqual(_mermaid_escape_label("{"), "#123;")
        self.assertEqual(_mermaid_escape_label("}"), "#125;")
        self.assertEqual(_mermaid_escape_label("|"), "#124;")
        self.assertEqual(_mermaid_escape_label("<"), "#60;")
        self.assertEqual(_mermaid_escape_label(">"), "#62;")
        self.assertEqual(_mermaid_escape_label("plain text"), "plain text")

    def test_inserted_entities_are_not_themselves_re_escaped(self):
        # A raw '"' becomes "#quot;" — the '#' inside that replacement must
        # not be picked up by the "#" -> "#35;" rule on a later pass. This
        # is only guaranteed by a single left-to-right character walk, not
        # sequential str.replace() calls (which would double-encode).
        self.assertEqual(_mermaid_escape_label('"'), "#quot;")
        self.assertNotIn("#35;quot", _mermaid_escape_label('"'))

    def test_title_with_quotes_and_brackets_produces_parseable_label(self):
        # This is the specific acceptance-criteria case: a title containing
        # quotes and brackets must not break out of the Mermaid quoted
        # label or be misread as node/edge syntax.
        tickets = [
            {
                "id": "a",
                "title": 'Fix the "quoted" [bracketed] (parenthetical) bug',
                "blocked_by": [],
            }
        ]
        graph = validate_and_level(tickets)
        output = _render_mermaid(graph)

        # None of the raw special characters reach the output unescaped...
        self.assertNotIn('"quoted"', output)
        self.assertNotIn("[bracketed]", output)
        self.assertNotIn("(parenthetical)", output)
        # ...they were replaced by their Mermaid entity equivalents.
        self.assertIn("#quot;quoted#quot;", output)
        self.assertIn("#91;bracketed#93;", output)
        self.assertIn("#40;parenthetical#41;", output)
        # The node declaration line still has exactly one opening and one
        # closing structural quote/bracket pair — i.e. the label content
        # did not introduce extra unescaped ones that would shift parsing.
        node_line = next(
            line for line in output.splitlines() if line.strip().startswith("n_a[")
        )
        self.assertTrue(node_line.strip().startswith('n_a["'))
        self.assertTrue(node_line.strip().endswith('"]'))

    def test_title_with_hash_pipe_and_angle_brackets_is_escaped(self):
        tickets = [
            {
                "id": "a",
                "title": "Ticket #123 <urgent> a|b",
                "blocked_by": [],
            }
        ]
        graph = validate_and_level(tickets)
        output = _render_mermaid(graph)

        self.assertNotIn("#123 <urgent> a|b", output)
        self.assertIn("#35;123", output)
        self.assertIn("#60;urgent#62;", output)
        self.assertIn("a#124;b", output)

    def test_ticket_id_itself_is_escaped_in_the_label(self):
        # Ticket IDs are only constrained to be a non-empty string by
        # validate_and_level() — an id containing reserved characters must
        # be escaped in the label text just like the title is.
        tickets = [{"id": 'weird"id', "title": "Title", "blocked_by": []}]
        graph = validate_and_level(tickets)
        output = _render_mermaid(graph)

        self.assertNotIn('weird"id', output)
        self.assertIn("weird#quot;id", output)


class MermaidNodeIdTest(unittest.TestCase):
    def test_node_ids_are_stable_and_distinct_for_normal_ids(self):
        tickets = [
            {"id": "a", "title": "A", "blocked_by": []},
            {"id": "b", "title": "B", "blocked_by": ["a"]},
        ]
        graph = validate_and_level(tickets)
        output = _render_mermaid(graph)
        self.assertIn("n_a", output)
        self.assertIn("n_b", output)

    def test_ticket_id_with_special_characters_gets_a_safe_node_id(self):
        # Ticket IDs can contain characters that aren't valid in a bare
        # Mermaid node identifier; the node id derived from them must still
        # be a safe, single, unquoted token.
        tickets = [
            {"id": "weird id!", "title": "Weird", "blocked_by": []},
        ]
        graph = validate_and_level(tickets)
        output = _render_mermaid(graph)
        self.assertIn("n_weird_id_", output)
        self.assertNotIn("weird id!", output.split('["')[0])


class MermaidDeterminismTest(unittest.TestCase):
    def test_same_input_produces_byte_identical_output(self):
        tickets = [
            {"id": "c", "title": "C", "blocked_by": ["a", "b"]},
            {"id": "a", "title": "A", "blocked_by": []},
            {"id": "b", "title": "B", "blocked_by": ["a"]},
        ]
        first = _render_mermaid(validate_and_level(tickets))
        second = _render_mermaid(validate_and_level(tickets))
        self.assertEqual(first, second)


class RenderBothTest(unittest.TestCase):
    def test_both_prints_terminal_output_then_mermaid_source_from_one_graph(self):
        tickets = [
            {"id": "a", "title": "A", "blocked_by": []},
            {"id": "b", "title": "B", "blocked_by": ["a"]},
        ]
        graph = validate_and_level(tickets)

        terminal_output = _render_terminal(graph)
        mermaid_output = _render_mermaid(graph)
        combined = _render_both(graph)

        # Terminal output comes first, Mermaid source after, and the
        # combined output is exactly the concatenation of the two
        # renderers run against the same graph object (no re-derivation).
        self.assertEqual(combined, terminal_output + "\n\n" + mermaid_output)
        self.assertTrue(combined.startswith(terminal_output))
        self.assertIn("graph TD", combined)
        terminal_end = combined.index("graph TD")
        self.assertIn("a — A", combined[:terminal_end])

    def test_both_is_byte_identical_across_runs(self):
        tickets = [
            {"id": "a", "title": "A", "blocked_by": []},
            {"id": "b", "title": "B", "blocked_by": ["a"]},
        ]
        first = _render_both(validate_and_level(tickets))
        second = _render_both(validate_and_level(tickets))
        self.assertEqual(first, second)


class MermaidCliTest(unittest.TestCase):
    def _run_cli(self, stdin_text, extra_args=()):
        return subprocess.run(
            [sys.executable, SCRIPT_PATH, *extra_args],
            input=stdin_text,
            capture_output=True,
            text=True,
        )

    def test_format_mermaid_flag_prints_graph_td_source(self):
        tickets = (
            '[{"id": "a", "title": "A", "blocked_by": []}, '
            '{"id": "b", "title": "B", "blocked_by": ["a"]}]'
        )
        result = self._run_cli(tickets, ["--format", "mermaid"])
        self.assertEqual(result.returncode, 0)
        self.assertTrue(result.stdout.startswith("graph TD"))
        self.assertIn("n_a --> n_b", result.stdout)

    def test_format_both_flag_prints_terminal_then_mermaid(self):
        tickets = (
            '[{"id": "a", "title": "A", "blocked_by": []}, '
            '{"id": "b", "title": "B", "blocked_by": ["a"]}]'
        )
        result = self._run_cli(tickets, ["--format", "both"])
        self.assertEqual(result.returncode, 0)
        self.assertIn("a — A", result.stdout)
        self.assertIn("graph TD", result.stdout)
        # Terminal content precedes the Mermaid source in stdout.
        self.assertLess(
            result.stdout.index("a — A"), result.stdout.index("graph TD")
        )

    def test_format_mermaid_still_reports_validation_errors_on_stderr(self):
        # A cycle: mermaid rendering must never be reached for invalid
        # input — the same validate_and_level() error path other formats
        # use applies uniformly.
        tickets = (
            '[{"id": "a", "title": "A", "blocked_by": ["b"]}, '
            '{"id": "b", "title": "B", "blocked_by": ["a"]}]'
        )
        result = self._run_cli(tickets, ["--format", "mermaid"])
        self.assertEqual(result.returncode, 1)
        self.assertIn("Dependency cycle detected", result.stderr)
        self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
