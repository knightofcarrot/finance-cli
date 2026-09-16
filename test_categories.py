import unittest

from finance import add_category, remove_category


class TestCategories(unittest.TestCase):

    def test_add_category(self):
        data = {
            "categories": ["Еда", "Такси"],
            "transactions": []
        }

        result = add_category(data, "Кино")

        self.assertTrue(result)
        self.assertIn("Кино", data["categories"])

    def test_add_existing_category(self):
        data = {
            "categories": ["Еда", "Такси"],
            "transactions": []
        }

        result = add_category(data, "Еда")

        self.assertFalse(result)
        self.assertEqual(data["categories"], ["Еда", "Такси"])

    def test_remove_category(self):
        data = {
            "categories": ["Еда", "Такси", "Кино"],
            "transactions": []
        }

        result = remove_category(data, "Кино")

        self.assertTrue(result)
        self.assertNotIn("Кино", data["categories"])

    def test_remove_missing_category(self):
        data = {
            "categories": ["Еда", "Такси"],
            "transactions": []
        }

        result = remove_category(data, "Кино")

        self.assertFalse(result)
        self.assertEqual(data["categories"], ["Еда", "Такси"])