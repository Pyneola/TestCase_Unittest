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

    def test_three_characters(self):
        self.assertEqual(two_characters("abcabcabc"), 4)

    def test_empty_string(self):
        self.assertEqual(two_characters(""), 0)


if __name__ == "__main__":
    unittest.main()
