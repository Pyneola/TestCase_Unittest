import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from hackerrank_two_characters import two_characters


class TestTwoCharacters(unittest.TestCase):
    def test_standard_case(self):
        self.assertEqual(two_characters("beabeefeab"), 5)

    def test_single_character(self):
        self.assertEqual(two_characters("aaaa"), 0)

    def test_alternating_characters(self):
        self.assertEqual(two_characters("ababab"), 6)

    def test_empty_string(self):
        self.assertEqual(two_characters(""), 0)

    def test_large_input(self):
        self.assertEqual(two_characters("a" * 1000 + "b" * 1000), 2000)

    def test_three_distinct_characters(self):
        self.assertEqual(two_characters("ababac"), 4)


if __name__ == "__main__":
    unittest.main()
