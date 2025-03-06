import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from hackerrank_caesar_cipher import caesar_cipher


class TestCaesarCipher(unittest.TestCase):
    def test_shift_by_3(self):
        self.assertEqual(caesar_cipher("abc", 3), "def")

    def test_shift_by_26(self):
        self.assertEqual(caesar_cipher("xyz", 26), "xyz")

    def test_shift_with_uppercase(self):
        self.assertEqual(caesar_cipher("ABC", 3), "DEF")

    def test_shift_with_mixed_characters(self):
        self.assertEqual(caesar_cipher("Hello, World!", 5), "Mjqqt, Btwqi!")

    def test_shift_with_large_k(self):
        self.assertEqual(caesar_cipher("abc", 29), "def")


if __name__ == "__main__":
    unittest.main()
