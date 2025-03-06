import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from hackerrank_alternating_characters import alternating_characters


class TestAlternatingCharacters(unittest.TestCase):
    def test_no_deletion_needed(self):
        self.assertEqual(alternating_characters("ABABAB"), 0)

    def test_all_same_characters(self):
        self.assertEqual(alternating_characters("AAAA"), 3)

    def test_one_deletion_needed(self):
        self.assertEqual(alternating_characters("AABB"), 2)

    def test_long_alternating_string(self):
        self.assertEqual(alternating_characters("AABBAABB"), 4)

    def test_edge_case_empty_string(self):
        self.assertEqual(alternating_characters(""), 0)


if __name__ == "__main__":
    unittest.main()
