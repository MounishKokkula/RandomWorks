"""
The below test cases are implemented for weather.oy

Author: Mounish Kokkula
Edit: version #1
Date: Feb 15th 2021
"""
import unittest
from weather import WeatherAnalysis


class MyTestCase(unittest.TestCase):
    def test_min_temp(self):
        weather = WeatherAnalysis('data_copy.csv')
        min_temp = weather.min_temp()
        self.assertEqual(min_temp['station_id'], 68)

    def test_fluctuation(self):
        weather = WeatherAnalysis('data_copy.csv')
        fluctuations = weather.fluctuations_dates()
        self.assertEqual(fluctuations, 198)

    def test_fluctuation_params(self):
        weather = WeatherAnalysis('data_copy.csv')
        fluctuations_dates = weather.fluctuations_dates(2012.208, 2013.408)
        self.assertEqual(fluctuations_dates, 198)

    def test_fluctuation_large_params(self):
        weather = WeatherAnalysis('data_copy.csv')
        # large input after decimal is being truncated - should return the same response as previous test case
        fluctuations_dates = weather.fluctuations_dates(2012.20821341352512321, 2013.408342354213526567)
        self.assertEqual(fluctuations_dates, 198)

    def test_fluctuation_string_params(self):
        weather = WeatherAnalysis('data_copy.csv')
        fluctuations_dates = weather.fluctuations_dates('2012.208', '2013.408')
        self.assertEqual(fluctuations_dates, "Exception Caught! Input params should be of float type & Format=> 'YYYY.###' ")

    def test_fluctuation_random_params(self):
        weather = WeatherAnalysis('data_copy.csv')
        fluctuations_dates = weather.fluctuations_dates(20121324.208, 2013324.408)
        self.assertEqual(fluctuations_dates, "Exception Caught! Input params should be of float type & Format=> 'YYYY.###' ")


if __name__ == '__main__':
    unittest.main()
