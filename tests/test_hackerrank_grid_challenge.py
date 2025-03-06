import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from hackerrank_grid_challenge import grid_challenge


class TestGridChallenge(unittest.TestCase):
    def test_sorted_grid(self):
        self.assertEqual(grid_challenge(["abc", "def", "ghi"]), "YES")

    def test_unsorted_grid(self):
        self.assertEqual(grid_challenge(["mpxz", "abcd", "wlmf"]), "NO")

    def test_single_row(self):
        self.assertEqual(
            grid_challenge(
                ["zxcv"],
            ),
            "YES",
        )

    def test_all_same_character(self):
        self.assertEqual(grid_challenge(["aaaa", "aaaa", "aaaa"]), "YES")

    def test_edge_case_minimum_input(self):
        self.assertEqual(grid_challenge(["a"]), "YES")


if __name__ == "__main__":
    unittest.main()
