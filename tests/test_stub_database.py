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
        self.assertEqual(result, "StubUser1")

    def test_fetch_user_name_with_different_id(self):
        stub_db = StubDatabase()
        result = fetch_user_name(stub_db, 99)
        self.assertEqual(result, "StubUser99")

    def test_fetch_user_name_with_zero_id(self):
        stub_db = StubDatabase()
        result = fetch_user_name(stub_db, 0)
        self.assertEqual(result, "StubUser0")

    def test_fetch_user_name_with_negative_id(self):
        stub_db = StubDatabase()
        result = fetch_user_name(stub_db, -5)
        self.assertEqual(result, "StubUser-5")

    def test_fetch_user_name_with_large_id(self):
        stub_db = StubDatabase()
        result = fetch_user_name(stub_db, 1000000)
        self.assertEqual(result, "StubUser1000000")


if __name__ == "__main__":
    unittest.main()
