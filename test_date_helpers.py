import unittest, sys
from datetime import datetime, timedelta, date
from pappardelle import *

sys.path.append('pappardelle')  # Include the subdir in the PythonPath

class TestDateHelpers(unittest.TestCase):

    def test_yesterday(self):
        self.assertEqual(yesterday(), date.today() - timedelta(days=1))

    def test_tomorrow(self):
        self.assertEqual(tomorrow(), date.today() + timedelta(days=1))

    def test_days_before(self):
        self.assertEqual(days_before(5), date.today() - timedelta(days=5))

    def test_days_after(self):
        self.assertEqual(days_after(3), date.today() + timedelta(days=3))

    def test_hours_before(self):
        self.assertAlmostEqual(hours_before(5), datetime.now() - timedelta(hours=5), delta=timedelta(seconds=1))

    def test_hours_after(self):
        self.assertAlmostEqual(hours_after(2), datetime.now() + timedelta(hours=2), delta=timedelta(seconds=1))

    def test_weeks_before(self):
        self.assertEqual(weeks_before(2), date.today() - timedelta(weeks=2))

    def test_weeks_after(self):
        self.assertEqual(weeks_after(3), date.today() + timedelta(weeks=3))

    def test_months_before(self):
        # Assuming current date is simple enough to handle month subtraction
        # This test might need adjustment depending on exact date and handling of end-of-month cases
        ref_date = date(2024, 10, 15)
        expected_date = date(2024, 8, 15)
        self.assertEqual(months_before(2, ref_date), expected_date)

    def test_months_after(self):
        ref_date = date(2024, 10, 15)
        expected_date = date(2025, 2, 15)
        self.assertEqual(months_after(4, ref_date), expected_date)

    def test_years_before(self):
        ref_date = date(2024, 10, 15)
        expected_date = date(2022, 10, 15)
        self.assertEqual(years_before(2, ref_date), expected_date)

    def test_years_after(self):
        ref_date = date(2024, 10, 15)
        expected_date = date(2026, 10, 15)
        self.assertEqual(years_after(2, ref_date), expected_date)

if __name__ == '__main__':
    unittest.main()
