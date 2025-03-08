import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from unittest.mock import MagicMock
from double_example import fetch_user_name


class TestDatabaseMocking(unittest.TestCase):
    def test_fetch_user_name_with_mock(self):
        mock_db = MagicMock()
        mock_db.get_user.return_value = {"id": 1, "name": "Alice"}

        result = fetch_user_name(mock_db, 1)
        self.assertEqual(result, "Alice")

    def test_fetch_user_name_with_unknown_user(self):
        mock_db = MagicMock()
        mock_db.get_user.return_value = {"id": 2}

        result = fetch_user_name(mock_db, 2)
        self.assertEqual(result, "Unknown")

    def test_fetch_user_name_calls_get_user_once(self):
        mock_db = MagicMock()
        mock_db.get_user.return_value = {"id": 3, "name": "Bob"}

        fetch_user_name(mock_db, 3)
        mock_db.get_user.assert_called_once_with(3)

    def test_fetch_user_name_with_no_return_value(self):
        mock_db = MagicMock()
        mock_db.get_user.return_value = None

        result = fetch_user_name(mock_db, 4)
        self.assertEqual(result, "Unknown")

    def test_fetch_user_name_with_empty_name(self):
        mock_db = MagicMock()
        mock_db.get_user.return_value = {"id": 5, "name": ""}

        result = fetch_user_name(mock_db, 5)
        self.assertEqual(result, "Unknown")

    def test_fetch_user_name_with_exception(self):
        mock_db = MagicMock()
        mock_db.get_user.side_effect = Exception("Database error")

        result = fetch_user_name(mock_db, 6)
        self.assertEqual(result, "Unknown")


if __name__ == "__main__":
    unittest.main()
