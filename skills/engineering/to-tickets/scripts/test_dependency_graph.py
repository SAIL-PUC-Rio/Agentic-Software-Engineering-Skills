"""Tests for dependency_graph.py.

Run with:
    python3 -m unittest skills/engineering/to-tickets/scripts/test_dependency_graph.py

or, from this directory:
    python3 -m unittest test_dependency_graph
"""

from __future__ import annotations

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from dependency_graph import (  # noqa: E402
    DependencyGraphError,
    validate_and_level,
)


def levels_by_id(graph):
    """Helper: {ticket_id: level} for easy assertions."""
    return {t.id: t.level for t in graph.tickets}


class SingleIndependentTicketTest(unittest.TestCase):
    def test_single_ticket_with_no_blockers_is_level_zero(self):
        graph = validate_and_level(
            [{"id": "a", "title": "A", "blocked_by": []}]
        )
        self.assertEqual(levels_by_id(graph), {"a": 0})


class LinearChainTest(unittest.TestCase):
    def test_linear_chain_assigns_increasing_levels(self):
        tickets = [
            {"id": "a", "title": "A", "blocked_by": []},
            {"id": "b", "title": "B", "blocked_by": ["a"]},
            {"id": "c", "title": "C", "blocked_by": ["b"]},
        ]
        graph = validate_and_level(tickets)
        self.assertEqual(levels_by_id(graph), {"a": 0, "b": 1, "c": 2})


class FanOutTest(unittest.TestCase):
    def test_fan_out_from_one_ticket(self):
        # a blocks both b and c
        tickets = [
            {"id": "a", "title": "A", "blocked_by": []},
            {"id": "b", "title": "B", "blocked_by": ["a"]},
            {"id": "c", "title": "C", "blocked_by": ["a"]},
        ]
        graph = validate_and_level(tickets)
        self.assertEqual(levels_by_id(graph), {"a": 0, "b": 1, "c": 1})


class FanInTest(unittest.TestCase):
    def test_fan_in_to_one_ticket(self):
        # d is blocked by both a and b
        tickets = [
            {"id": "a", "title": "A", "blocked_by": []},
            {"id": "b", "title": "B", "blocked_by": []},
            {"id": "d", "title": "D", "blocked_by": ["a", "b"]},
        ]
        graph = validate_and_level(tickets)
        self.assertEqual(levels_by_id(graph), {"a": 0, "b": 0, "d": 1})

    def test_fan_in_uses_longest_path_for_level(self):
        # d is blocked by a (level 0) and c (level 1, since c is blocked by b)
        # d's level must be 1 + max(0, 1) = 2, not 1 + min(...)
        tickets = [
            {"id": "a", "title": "A", "blocked_by": []},
            {"id": "b", "title": "B", "blocked_by": []},
            {"id": "c", "title": "C", "blocked_by": ["b"]},
            {"id": "d", "title": "D", "blocked_by": ["a", "c"]},
        ]
        graph = validate_and_level(tickets)
        self.assertEqual(
            levels_by_id(graph), {"a": 0, "b": 0, "c": 1, "d": 2}
        )


class MultipleIndependentRootsTest(unittest.TestCase):
    def test_multiple_roots_all_level_zero(self):
        tickets = [
            {"id": "a", "title": "A", "blocked_by": []},
            {"id": "b", "title": "B", "blocked_by": []},
            {"id": "c", "title": "C", "blocked_by": []},
        ]
        graph = validate_and_level(tickets)
        self.assertEqual(levels_by_id(graph), {"a": 0, "b": 0, "c": 0})


class DisconnectedSubgraphsTest(unittest.TestCase):
    def test_disconnected_subgraphs_leveled_independently(self):
        tickets = [
            {"id": "a", "title": "A", "blocked_by": []},
            {"id": "b", "title": "B", "blocked_by": ["a"]},
            {"id": "x", "title": "X", "blocked_by": []},
            {"id": "y", "title": "Y", "blocked_by": ["x"]},
            {"id": "z", "title": "Z", "blocked_by": ["y"]},
        ]
        graph = validate_and_level(tickets)
        self.assertEqual(
            levels_by_id(graph),
            {"a": 0, "b": 1, "x": 0, "y": 1, "z": 2},
        )


class UnknownBlockerTest(unittest.TestCase):
    def test_unknown_blocker_reference_is_rejected(self):
        tickets = [
            {"id": "a", "title": "A", "blocked_by": ["does-not-exist"]},
        ]
        with self.assertRaises(DependencyGraphError) as ctx:
            validate_and_level(tickets)
        message = str(ctx.exception)
        self.assertIn("a", message)
        self.assertIn("does-not-exist", message)


class DuplicateIdTest(unittest.TestCase):
    def test_duplicate_ticket_id_is_rejected(self):
        tickets = [
            {"id": "a", "title": "A first", "blocked_by": []},
            {"id": "a", "title": "A second", "blocked_by": []},
        ]
        with self.assertRaises(DependencyGraphError) as ctx:
            validate_and_level(tickets)
        self.assertIn("a", str(ctx.exception))
        self.assertIn("Duplicate", str(ctx.exception))


class SelfDependencyTest(unittest.TestCase):
    def test_self_dependency_is_rejected(self):
        tickets = [
            {"id": "a", "title": "A", "blocked_by": ["a"]},
        ]
        with self.assertRaises(DependencyGraphError) as ctx:
            validate_and_level(tickets)
        self.assertIn("a", str(ctx.exception))


class CycleDetectionTest(unittest.TestCase):
    def test_two_ticket_cycle_is_rejected(self):
        tickets = [
            {"id": "a", "title": "A", "blocked_by": ["b"]},
            {"id": "b", "title": "B", "blocked_by": ["a"]},
        ]
        with self.assertRaises(DependencyGraphError) as ctx:
            validate_and_level(tickets)
        self.assertIn("cycle", str(ctx.exception).lower())

    def test_three_ticket_cycle_is_rejected(self):
        tickets = [
            {"id": "a", "title": "A", "blocked_by": ["c"]},
            {"id": "b", "title": "B", "blocked_by": ["a"]},
            {"id": "c", "title": "C", "blocked_by": ["b"]},
        ]
        with self.assertRaises(DependencyGraphError) as ctx:
            validate_and_level(tickets)
        self.assertIn("cycle", str(ctx.exception).lower())


class DeterminismTest(unittest.TestCase):
    def test_same_input_produces_identical_output_across_runs(self):
        tickets = [
            {"id": "c", "title": "C", "blocked_by": ["a", "b"]},
            {"id": "a", "title": "A", "blocked_by": []},
            {"id": "b", "title": "B", "blocked_by": ["a"]},
        ]
        first = validate_and_level(tickets)
        second = validate_and_level(tickets)
        first_view = [(t.id, t.level) for t in first.tickets]
        second_view = [(t.id, t.level) for t in second.tickets]
        self.assertEqual(first_view, second_view)

    def test_output_order_is_stable_regardless_of_input_order(self):
        forward = [
            {"id": "a", "title": "A", "blocked_by": []},
            {"id": "b", "title": "B", "blocked_by": ["a"]},
        ]
        reversed_input = list(reversed(forward))
        graph_forward = validate_and_level(forward)
        graph_reversed = validate_and_level(reversed_input)
        view_forward = [(t.id, t.level) for t in graph_forward.tickets]
        view_reversed = [(t.id, t.level) for t in graph_reversed.tickets]
        self.assertEqual(view_forward, view_reversed)


class ByLevelGroupingTest(unittest.TestCase):
    def test_by_level_groups_tickets_in_level_order(self):
        tickets = [
            {"id": "a", "title": "A", "blocked_by": []},
            {"id": "b", "title": "B", "blocked_by": ["a"]},
            {"id": "c", "title": "C", "blocked_by": ["a"]},
        ]
        graph = validate_and_level(tickets)
        groups = graph.by_level()
        self.assertEqual([t.id for t in groups[0]], ["a"])
        self.assertEqual(sorted(t.id for t in groups[1]), ["b", "c"])


if __name__ == "__main__":
    unittest.main()
