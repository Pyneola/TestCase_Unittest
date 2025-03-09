import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from src.hackerrank_caesar_cipher import caesar_cipher


class TestCaesarCipher(unittest.TestCase):
    def test_shift_by_3(self):
        self.assertEqual(caesar_cipher("abc", 3), "def")

    def test_shift_by_26(self):
        self.assertEqual(caesar_cipher("xyz", 26), "xyz")
        self.assertEqual(caesar_cipher("ABC", 26), "ABC")

    def test_shift_with_uppercase(self):
        self.assertEqual(caesar_cipher("ABC", 3), "DEF")
        self.assertEqual(caesar_cipher("XYZ", 3), "ABC")

    def test_shift_with_large_k(self):
        self.assertEqual(caesar_cipher("abc", 29), "def")
        self.assertEqual(caesar_cipher("xyz", 52), "xyz")

    def test_no_shift(self):
        self.assertEqual(caesar_cipher("hello", 0), "hello")

    def test_edge_case_empty_string(self):
        self.assertEqual(caesar_cipher("", 5), "")

    def test_non_alphabetic_characters(self):
        self.assertEqual(caesar_cipher("1234!@#", 5), "1234!@#")

    def test_standard_case(self):
        self.assertEqual(caesar_cipher("middle-Outz", 2), "okffng-Qwvb")


if __name__ == "__main__":
    unittest.main()
