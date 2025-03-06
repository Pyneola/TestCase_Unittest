import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from stub_database import StubDatabase
from test_double_example import fetch_user_name


class TestDatabaseStub(unittest.TestCase):
    def test_fetch_user_name_with_stub(self):
        stub_db = StubDatabase()
        result = fetch_user_name(stub_db, 1)
        self.assertEqual(result, f"StubUser1")

    def test_fetch_user_name_with_different_id(self):
        stub_db = StubDatabase()
        result = fetch_user_name(stub_db, 99)
        self.assertEqual(result, f"StubUser99")

    def test_fetch_user_name_with_zero_id(self):
        stub_db = StubDatabase()
        result = fetch_user_name(stub_db, 0)
        self.assertEqual(result, f"StubUser0")

    def test_fetch_user_name_with_negative_id(self):
        stub_db = StubDatabase()
        result = fetch_user_name(stub_db, -5)
        self.assertEqual(result, f"StubUser-5")


if __name__ == "__main__":
    unittest.main()
