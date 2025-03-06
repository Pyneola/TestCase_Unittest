import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from staircase import staircase


class TestStaircase(unittest.TestCase):
    def test_height_2(self):
        self.assertEqual(staircase(2), " #\n##")

    def test_height_3(self):
        self.assertEqual(staircase(3), "  #\n ##\n###")

    def test_height_4(self):
        self.assertEqual(staircase(4), "   #\n  ##\n ###\n####")

    def test_custom_pattern(self):
        self.assertEqual(staircase(2, "*"), " *\n**")

    def test_single_step(self):
        self.assertEqual(staircase(1), "#")


if __name__ == "__main__":
    unittest.main()
