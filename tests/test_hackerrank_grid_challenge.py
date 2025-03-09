import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from src.hackerrank_grid_challenge import grid_challenge


class TestGridChallenge(unittest.TestCase):
    def test_sorted_grid(self):
        self.assertEqual(grid_challenge(["abc", "def", "ghi"]), "YES")

    def test_unsorted_grid(self):
        self.assertEqual(grid_challenge(["mpxz", "abcd", "wlmf"]), "NO")
        self.assertEqual(grid_challenge(["zyx", "wvu", "tsr"]), "NO")

    def test_single_row(self):
        self.assertEqual(grid_challenge(["zxcv"]), "YES")
        self.assertEqual(grid_challenge(["qwerty"]), "YES")

    def test_all_same_character(self):
        self.assertEqual(grid_challenge(["aaaa", "aaaa", "aaaa"]), "YES")
        self.assertEqual(grid_challenge(["bbbb", "bbbb", "bbbb"]), "YES")

    def test_edge_case_minimum_input(self):
        self.assertEqual(grid_challenge(["a"]), "YES")
        self.assertEqual(grid_challenge(["z"]), "YES")

    def test_large_grid(self):
        self.assertEqual(
            grid_challenge(
                [
                    "abcdefgh",
                    "ijklmnop",
                    "qrstuvwx",
                    "yzabcdef",
                    "ghijklmn",
                    "opqrstuv",
                    "wxyzabcd",
                    "efghijkl",
                ]
            ),
            "YES",
        )

    def test_standard_case(self):
        self.assertEqual(
            grid_challenge(["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]), "YES"
        )

    def test_large_grid(self):
        self.assertEqual(grid_challenge(["zzzz", "zzzz", "zzzz", "zzzz"]), "YES")


if __name__ == "__main__":
    unittest.main()
