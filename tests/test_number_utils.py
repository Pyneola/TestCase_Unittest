import unittest
from src.number_utils import is_prime_list


class TestNumberUtils(unittest.TestCase):
    def test_all_prime_numbers(self):
        self.assertTrue(is_prime_list([2, 3, 5, 7]))

    def test_contains_non_prime(self):
        self.assertFalse(is_prime_list([4, 6, 8]))

    def test_empty_list(self):
        self.assertFalse(is_prime_list([]))

    def test_contains_one(self):
        self.assertFalse(is_prime_list([1]))

    def test_large_prime_numbers(self):
        self.assertTrue(is_prime_list([101, 103, 107]))


if __name__ == "__main__":
    unittest.main()
