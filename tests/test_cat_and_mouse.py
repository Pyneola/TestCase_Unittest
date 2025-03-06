import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from cat_and_mouse import cat_and_mouse


class TestCatAndMouse(unittest.TestCase):
    def test_cat_a_wins(self):
        self.assertEqual(cat_and_mouse(1, 5, 2), "Cat A")

    def test_cat_b_wins(self):
        self.assertEqual(cat_and_mouse(1, 5, 4), "Cat B")

    def test_mouse_escapes(self):
        self.assertEqual(cat_and_mouse(1, 3, 2), "Mouse C")

    def test_edge_case_same_distance(self):
        self.assertEqual(cat_and_mouse(3, 7, 5), "Mouse C")

    def test_large_values(self):
        self.assertEqual(cat_and_mouse(10, 20, 15), "Mouse C")


if __name__ == "__main__":
    unittest.main()
