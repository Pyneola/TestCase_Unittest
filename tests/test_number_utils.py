import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from number_utils import is_prime_list


class TestNumberUtils(unittest.TestCase):
    def test_all_prime_numbers(self):
        self.assertTrue(is_prime_list([2, 3, 5, 7]))
        self.assertTrue(is_prime_list([11, 13, 17, 19]))

    def test_contains_non_prime(self):
        self.assertFalse(is_prime_list([4, 6, 8]))
        self.assertFalse(is_prime_list([2, 3, 5, 9]))

    def test_empty_list(self):
        self.assertFalse(is_prime_list([]))

    def test_contains_one(self):
        self.assertFalse(is_prime_list([1]))
        self.assertFalse(is_prime_list([1, 2, 3]))

    def test_large_prime_numbers(self):
        self.assertTrue(is_prime_list([101, 103, 107]))
        self.assertTrue(is_prime_list([197, 199, 211]))

    def test_mixed_numbers(self):
        self.assertFalse(is_prime_list([2, 3, 4, 5]))
        self.assertFalse(is_prime_list([10, 11, 12, 13]))

    def test_large_non_prime_numbers(self):
        self.assertFalse(is_prime_list([200, 300, 400]))
        self.assertFalse(is_prime_list([201, 202, 203]))


if __name__ == "__main__":
    unittest.main()
