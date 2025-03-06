import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from hackerrank_funny_string import funny_string


class TestFunnyString(unittest.TestCase):
    def test_funny_string(self):
        self.assertEqual(funny_string("acxz"), "Funny")

    def test_not_funny_string(self):
        self.assertEqual(funny_string("bcxz"), "Not Funny")

    def test_single_character(self):
        self.assertEqual(funny_string("a"), "Funny")

    def test_palindrome(self):
        self.assertEqual(funny_string("abba"), "Funny")


if __name__ == "__main__":
    unittest.main()
