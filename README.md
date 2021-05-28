## Hawaii Weather Analysis and API Query Service

 <table style="width:100%">
  <tr valign="top">
    <th><img height="300" alt="Average Daily Rainfall" src="https://github.com/kennethcandersen/sqlalchemy-challenge/blob/main/output_charts/average_rainfall.png"></th>
    <th><img height="300" alt="Average Salaries by Position" src="https://github.com/kennethcandersen/sqlalchemy-challenge/blob/main/output_charts/temps_during_trip_date_range.png"></th>
  </tr>
</table> 

**EXECUTIVE SUMMARY**

This project provides analysis of Hawaii weather and makes available queries via API.

**REPOSITORY NAVIGATION**

* [*Climate Analysis*](https://github.com/kennethcandersen/sqlalchemy-challenge/commit/4c2e4c0c2f734589b0003d0ae3305864ff982e66) is a Jypyter Notebook that calculates and visualizes average rainfall in a bar chart and average temperature in a histogram.
* [*The Climate App*](https://github.com/kennethcandersen/sqlalchemy-challenge/blob/main/climate_app.py) is a Flask API application that provides climate data for 5 database queries. More detail for using the API is below. 
* [*Additional Temperature Analysis 1*](https://github.com/kennethcandersen/sqlalchemy-challenge/blob/main/temp_analysis_bonus_1_starter.ipynb) runs a t-test to compare June and December average temperatures. 
* [*Additional Temperature Analysis 2*](https://github.com/kennethcandersen/sqlalchemy-challenge/blob/main/temp_analysis_bonus_2_starter.ipynb) calculates and visualizes the minmum, average and maximum temperatures during a specified vacation date range with a [bar chart](https://github.com/kennethcandersen/sqlalchemy-challenge/blob/main/output_charts/average_trip_temperature.png) and an [area chart](https://github.com/kennethcandersen/sqlalchemy-challenge/blob/main/output_charts/temps_during_trip_date_range.png).

**OBJECTIVE**

Analyze compensation data for over 300,000 employees:
- Create code to set up a database using Postgre SQL, import data from csv files, and run queries
- Import data into a Jupyter Notebook
- Create code to analyze and plot compensation data
- Provide recommendations to the corporate compensation committee

**API DOCUMENTATION**
- Dowload the [Climate App API starter code](https://github.com/kennethcandersen/sqlalchemy-challenge/blob/main/climate_app.py) and the Hawaii weather [sqlite database](https://github.com/kennethcandersen/sqlalchemy-challenge/blob/main/hawaii.sqlite) into the same folder on your drive. 
- Run the python app on your computer.
- In your navigator enter this address: http://127.0.0.1:5000/
- You will have a menu of five API route options:
-   /api/v1.0/precipitation provides average daily rainfall for the past year. 
-   /api/v1.0/stations provides a list of the stations with their coordinates, elevation and measurement activity levels. 
-   /api/v1.0/tobs provides average daily temperatures for the past year.
-   /api/v1.0/<start> provides the minimum, average, and maximum temperature from a start date to present. Start dates should be in the following format: yyyy-mm-dd. Example: '/api/v1.0/2014-01-01'
-   /api/v1.0/<start>/<end> provides the minimum, average, and maximum temperature from a start date to and end date. Start and end dates should be in the following format: yyyy-mm-dd. Example: '/api/v1.0/2014-01-01/2016-12-31'

**DATA** 

- [sqlite database] (https://github.com/kennethcandersen/sqlalchemy-challenge/blob/main/hawaii.sqlite) with data from 9 weather stations on the islands of Hawaii


**DEPENDENCIES**

- from sqlalchemy import create_engine
- from sqlalchemy.dialects import postgresql
- from config import pgadmin_pw
- import pandas as pd
- import matplotlib.pyplot as plt      
- from matplotlib import style
- style.use('fivethirtyeight')
- import math
- import numpy as np
- import pandas as pd
- import datetime as dt
- from scipy import stats
- from datetime import datetime as dt
- from datetime import timedelta                
       
**PANDAS ANALYSIS**

 <table style="width:100%">
  <tr valign="top">
    <th><img height="200" alt="Average Daily Rainfall" src="https://github.com/kennethcandersen/sqlalchemy-challenge/blob/main/output_charts/average_rainfall.png"></th>
    <th><img height="200" alt="Average Salaries by Position" src="https://github.com/kennethcandersen/sqlalchemy-challenge/blob/main/output_charts/temps_during_trip_date_range.png"></th>
    <th><img height="200" alt="Average Historical Temperatures During Trip Dates" src="https://github.com/kennethcandersen/sqlalchemy-challenge/blob/main/output_charts/temps_during_trip_date_range.png"></th>
       <th><img height="200" alt="Average Historical Temperatures During Trip Dates" src="https://github.com/kennethcandersen/sqlalchemy-challenge/blob/main/output_charts/temps_during_trip_date_range.png"></th>
  </tr>
</table> 

**CONCLUSIONS**

- Hawaii has amazing weather. 
=======

