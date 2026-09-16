import unittest

from finance import get_month_statistics, get_category_statistics


class TestStatistics(unittest.TestCase):

    def test_month_statistics(self):
        data = {
            "transactions": [
                {
                    "type": "income",
                    "amount": 50000,
                    "category": "Зарплата",
                    "date": "10.09.2026"
                },
                {
                    "type": "expense",
                    "amount": 1500,
                    "category": "Еда",
                    "date": "11.09.2026"
                },
                {
                    "type": "expense",
                    "amount": 500,
                    "category": "Такси",
                    "date": "12.09.2026"
                }
            ]
        }

        result = get_month_statistics(data, "09.2026")

        self.assertEqual(result["income"], 50000)
        self.assertEqual(result["expense"], 2000)
        self.assertEqual(result["balance"], 48000)

    def test_category_statistics(self):
        data = {
            "transactions": [
                {
                    "type": "expense",
                    "amount": 1000,
                    "category": "Еда",
                    "date": "10.09.2026"
                },
                {
                    "type": "expense",
                    "amount": 500,
                    "category": "Еда",
                    "date": "11.09.2026"
                },
                {
                    "type": "expense",
                    "amount": 300,
                    "category": "Такси",
                    "date": "12.09.2026"
                }
            ]
        }

        result = get_category_statistics(data, "09.2026")

        self.assertEqual(result["Еда"], 1500)
        self.assertEqual(result["Такси"], 300)