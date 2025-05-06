import unittest
from io import StringIO
import sys
import os
import Weather

class TestForecastIntegration(unittest.TestCase):

    def setUp(self):
        self.api_key = Weather.api_key
        self.valid_zip = "10001"  # New York
        self.invalid_zip = "00000"
        self.country_code = "us"
        self.stdout_backup = sys.stdout
        sys.stdout = StringIO()  # capture print output

    def tearDown(self):
        sys.stdout = self.stdout_backup
        for f in ["forecast1.txt", "forecast2.txt", "forecast3.txt"]:
            if os.path.exists(f):
                os.remove(f)

    def test_valid_forecast_output(self):
        Weather.get_3_day_forecast(self.valid_zip, self.country_code, self.api_key)
        output = sys.stdout.getvalue()
        self.assertIn("Day 1", output)
        self.assertTrue(os.path.exists("forecast1.txt"))

    def test_invalid_zip_error(self):
        Weather.get_3_day_forecast(self.invalid_zip, self.country_code, self.api_key)
        output = sys.stdout.getvalue()
        self.assertIn("Sorry, invalid API response", output)

    def test_expected_data_structure_from_extract(self):
        response = Weather.requests.get(
            f"http://api.openweathermap.org/data/2.5/forecast?zip={self.valid_zip},{self.country_code}&units=imperial&cnt=24&appid={self.api_key}"
        )
        data = response.json()
        result = Weather.extract_3_day_forecast(data)
        self.assertEqual(len(result), 3)
        self.assertEqual(len(result[0]), 3)  # date, temp, description
        self.assertTrue(response.status_code == 200)

    def test_handling_of_bad_api_key(self):
        bad_key = "INVALIDKEY123"
        Weather.get_3_day_forecast(self.valid_zip, self.country_code, bad_key)
        output = sys.stdout.getvalue()
        self.assertIn("Sorry, invalid API response", output)

if __name__ == "__main__":
    unittest.main()
