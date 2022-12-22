from datetime import datetime
import json
import requests
import unittest
import urllib.request
from datetime import datetime
from unittest.mock import patch, MagicMock
from what_is_year_now import what_is_year_now, API_URL


class MyTestCase(unittest.TestCase):

    @staticmethod
    def prepare_mock_urlopen(mock_urlopen, current_date_time):
        fake_json = {
            '$id': '1',
            'currentDateTime': current_date_time,
            'utcOffset': '00:00:00',
            'isDayLightSavingsTime': False,
            'dayOfTheWeek': 'Friday',
            'timeZoneName': 'UTC',
            'currentFileTime': 133150579589475527,
            'ordinalDate': '2022-343',
            'serviceResponse': None
        }

        cm = MagicMock()
        cm.read.return_value = json.dumps(fake_json)
        cm.__enter__.return_value = cm
        mock_urlopen.return_value = cm

    def test_what_year_is_now_ymd_type(self):
        test_year = 2001
        current_date_time_with_dashes = str(test_year) + '-12-09T11:12Z'

        with patch('urllib.request.urlopen') as mock_urlopen:
            self.prepare_mock_urlopen(mock_urlopen, current_date_time_with_dashes)
            self.assertEqual(what_is_year_now(), test_year)

    def test_what_year_is_now_dmy_type(self):
        test_year = 2015
        current_date_time_with_dots = '01.03.' + str(test_year)

        with patch('urllib.request.urlopen') as mock_urlopen:
            self.prepare_mock_urlopen(mock_urlopen, current_date_time_with_dots)
            self.assertEqual(what_is_year_now(), test_year)

    def test_what_is_the_year_now_wrong_type(self):
        test_year = 'TWENTY_TWENTYTWO'
        invalid_date_time = test_year

        with patch('urllib.request.urlopen') as mock_urlopen:
            self.prepare_mock_urlopen(mock_urlopen, invalid_date_time)

            with self.assertRaises(ValueError):
                what_is_year_now()


if __name__ == '__main__':
    unittest.main()
