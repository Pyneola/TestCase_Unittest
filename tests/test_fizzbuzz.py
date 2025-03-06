import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")

    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), "Buzz")

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")

    def test_number(self):
        self.assertEqual(fizzbuzz(7), "7")

    def test_large_number(self):
        self.assertEqual(fizzbuzz(30), "FizzBuzz")


if __name__ == "__main__":
    unittest.main()
