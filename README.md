# RandomWorks
This repository includes the following programs/projects  

### Bar chart using turtle(python)
A Bar chart program using turtle (“Turtle” is a Python feature like a drawing board, which lets us command a turtle to draw) and pandas library for reading csv - python 3.6.4


### ArrayOperations (python, unnittest)
The directory contains a program that could be used as a utility library for array operations.

#### program:flatten_array.py
Methods:
1. Flatten an array/list (words array & list are being interchangeably in the code below)

#### program:test_flatten_array.py
The file contains test cases for flatten_array.py


### Weather(python, pandas, numpy, csv, unnittest)
The directory contains a program to analyze weather data from csv file.

#### program:weather.py
Methods:
1. min_temp: Find the station_id having the minimum temperature across all the rows
2. fluctuations_dates: Find the station_id having the most amount of temperature fluctuation

    i) across all dates that it reported temperatures for

    ii) across the supplied input dates

#### program:test_weather.py
The file contains test cases for flatten_array.py


### Campaign Scheduling (python 3.6, pandas, Unittest, Test Driven Developement[TDD])

A "Campaign" is the top-level advertising unit. Among other things, a campaign
will have a unique name, a start date, and end date.
"CampaignScheduler" service class can be used to store a set of campaigns. 
Each campaign being scheduled should have a unique name, a start date, and an end date.

Class: CampaignScheduler

Methods: 
1. schedule_campaign(campaign) This function adds a new campaign to the scheduler.
2. find_gaps() This function returns a list of date ranges that are not covered by the
current set of scheduled campaigns.

Unittest:
TDD approach is followed in this program
