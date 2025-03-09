import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from hackerrank_alternating_characters import alternating_characters


class TestAlternatingCharacters(unittest.TestCase):
    def test_no_deletion_needed(self):
        self.assertEqual(alternating_characters("ABABAB"), 0)
        self.assertEqual(alternating_characters("BABABA"), 0)
        self.assertEqual(alternating_characters("A"), 0)

    def test_all_same_characters(self):
        self.assertEqual(alternating_characters("AAAA"), 3)
        self.assertEqual(alternating_characters("BBBBBB"), 5)
        self.assertEqual(alternating_characters("CCCCC"), 4)

    def test_one_deletion_needed(self):
        self.assertEqual(alternating_characters("AABB"), 2)
        self.assertEqual(alternating_characters("ABBA"), 1)
        self.assertEqual(alternating_characters("BBBA"), 2)

    def test_edge_case_empty_string(self):
        self.assertEqual(alternating_characters(""), 0)

    def test_edge_case_single_character(self):
        self.assertEqual(alternating_characters("A"), 0)
        self.assertEqual(alternating_characters("B"), 0)


if __name__ == "__main__":
    unittest.main()
