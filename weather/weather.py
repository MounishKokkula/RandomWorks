"""
The below program contains a set of methods to analyze weather data from csv file.

Methods:
1. min_temp: Find the station_id having the minimum temperature across all the rows
2. fluctuations_dates: Find the station_id having the most amount of temperature fluctuation
                        i) across all dates that it reported temperatures for
                        ii) across the supplied input dates

Author: Mounish Kokkula
Edit: version #1
Date: Feb 15th 2021
"""

import time
import pandas
import numpy as np


class WeatherAnalysis:
    def __init__(self, csv_file):
        """
        constructor processes the input file and returns a datafram
        :param csv_file: csv_file
        """
        self.csv_file = csv_file
        self.df = pandas.read_csv(self.csv_file)

        # data cleaning - removing a row if any column value is empty
        self.df = self.df.dropna(axis=0, how='any')

    def min_temp(self):
        # Time complexity
        # O(N), i.e. O(N) where n is number of rows in input csv
        min_row = self.df[self.df.temperature_c == self.df.temperature_c.min()].values.tolist()
        date = float(f"{min_row[0][1]:.3f}")
        return {"station_id": int(min_row[0][0]), "date": date}

    def fluctuations_dates(self, date1=None, date2=None):
        # Time complexity
        # O(d), i.e. O(d) where d is number of elements in the date range supplied
        """
        :param date1: initial date in the sequence (float)
        :param date2: last date in the sequence (float)
        :return: max fluctuation station_id (dictionary)
        """
        try:
            df_new = self.df
            if date1 and date2:
                date1 = float(f"{date1:.3f}")
                date2 = float(f"{date2:.3f}")
                df_new = self.df[(self.df['date'] >= date1) & (self.df['date'] <= date2)]
            grouped = df_new.groupby("station_id", as_index=False, group_keys=False)
            max_fluctuation = {"station_id": 0, "fluct": 0}
            for station_id, group in grouped:
                temp = abs(group['temperature_c'].values - group['temperature_c'].shift(-1).values)
                temp = temp[~np.isnan(temp)].sum()

                if max_fluctuation["fluct"] < temp:
                    max_fluctuation["station_id"] = station_id
                    max_fluctuation["fluct"] = temp

            if max_fluctuation["station_id"] == 0:
                raise ValueError
            return max_fluctuation["station_id"]

        except ValueError:
            return "Exception Caught! Input params should be of float type & Format=> 'YYYY.###' "

        except Exception as e:
            return str(e)


if __name__ == '__main__':
    startTime = time.time()
    # pass the csv file frame to class
    weather = WeatherAnalysis('data_copy.csv')

    """
    # Part 1
    Create a function that when called returns the station_id, and date pair that reported the lowest temperature. 
    If a tie occurs simply return one pair at random.
    """
    print('Part 1: Reported lowest temperature')
    min_temp = weather.min_temp()
    print("station_id: {} , date: {:.3f} ".format(min_temp['station_id'], min_temp['date']))
    print('Execution time in seconds: {:.3f}'.format(time.time() - startTime))
    print("\n")

    startTime = time.time()
    """
    # Part 2
    Create a function that returns the station_id that experienced the most amount of temperature fluctuation 
    across all dates that it reported temperatures for.
    """
    print('Part 2: The most amount of temperature fluctuation across all dates')
    fluctuations = weather.fluctuations_dates()
    print("station_id: {} ".format(fluctuations))
    print('Execution time in seconds: {:.3f}'.format(time.time() - startTime))
    print("\n")

    """
    # Part 3
    Create a function that will return the station_id that experienced the most amount of temperature fluctuation for 
    any given range of dates. I.e to get the result of 10 degrees from part 2 above, we would expect the input dates to 
    be 2000.001 and 2000.456.
    """
    startTime = time.time()
    print('Part 3: The most amount of temperature fluctuation for any given range of dates')
    fluctuations_dates = weather.fluctuations_dates(2012.208, 2013.408)
    print("station_id: {} ".format(fluctuations_dates))
    print('Execution time in seconds: {:.3f}'.format(time.time() - startTime))
    print("\n")

    print("Checking with string input params")
    fluctuations_dates = weather.fluctuations_dates('2000.208', '2005.408')
    print("station_id: {} ".format(fluctuations_dates))
    print("\n")

    print("Checking with large input params")
    fluctuations_dates = weather.fluctuations_dates(20121324.208, 2013324.408)
    print("station_id: {} ".format(fluctuations_dates))
    print("\n")
