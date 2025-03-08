import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(6), "Fizz")
        self.assertEqual(fizzbuzz(9), "Fizz")

    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(10), "Buzz")
        self.assertEqual(fizzbuzz(20), "Buzz")

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(30), "FizzBuzz")
        self.assertEqual(fizzbuzz(45), "FizzBuzz")

    def test_number(self):
        self.assertEqual(fizzbuzz(7), "7")
        self.assertEqual(fizzbuzz(8), "8")
        self.assertEqual(fizzbuzz(13), "13")

    def test_large_number(self):
        self.assertEqual(fizzbuzz(100), "Buzz")
        self.assertEqual(fizzbuzz(300), "FizzBuzz")
        self.assertEqual(fizzbuzz(299), "299")

    def test_negative_numbers(self):
        self.assertEqual(fizzbuzz(-3), "Fizz")
        self.assertEqual(fizzbuzz(-5), "Buzz")
        self.assertEqual(fizzbuzz(-15), "FizzBuzz")

    def test_zero(self):
        self.assertEqual(fizzbuzz(0), "FizzBuzz")


if __name__ == "__main__":
    unittest.main()
