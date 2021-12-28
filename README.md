# SQLAlchemy climate analysis - Surfs Up!



![surfs-up.png](Images/surfs-up.png)

This project is about climate analysis on Hawaii. The following outlines what you need to do.

## Step 1 - Climate Analysis and Exploration

Used Python and SQLAlchemy to do basic climate analysis and data exploration of my climate database. All of the following analysis were completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

* Sart and end date chose for my trip (analysis). 

* Used SQLAlchemy `create_engine` to connect to my sqlite database.

* Used SQLAlchemy `automap_base()` to reflect my tables into classes and save a reference to those classes called `Station` and `Measurement`.

### Precipitation Analysis

* Designed a query to retrieve the last 12 months of precipitation data.

* Loaded the query results into a Pandas DataFrame and set the index to the date column.

* Sort the DataFrame values by `date`.

* Plotted the results using the DataFrame `plot` method.

  ![precipitation](Images/precipitation.png)

* Used Pandas to print the summary statistics for the precipitation data.

### Station Analysis

* Designed a query to calculate the total number of stations.

* Designed a query to find the most active stations.

* Listed the stations and observation counts in descending order.

* Found out the station has the highest number of observations with function such as `func.min`, `func.max`, `func.avg`, and `func.count` in my queries

* Designed a query to retrieve the last 12 months of temperature observation data (TOBS).

* Filtered by the station with the highest number of observations.

* Plotted the results as a histogram with `bins=12`.

    ![station-histogram](Images/station-histogram.png)

- - -

## Step 2 - Climate App

Designed a Flask API based on the queries that you have just developed.

the station and measurement tables were joined.

### Routes

* `/`

  * Home page.

  * All routes that are available.

* `/api/v1.0/precipitation`

  * Converted the query results to a dictionary using `date` as the key and `prcp` as the value.

  * Returned the JSON representation of my dictionary.

* `/api/v1.0/stations`

  * Returned a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * Queried the dates and temperature observations of the most active station for the last year of data.
  
  * Returned a JSON list of temperature observations (TOBS) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Returned a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

- - -

### Temperature Analysis I - difference between the temperature in different seasons

* Identified the average temperature in June at all stations across all available years in the dataset. Same for December temperature.

* Used the t-test to determine whether the difference in the means, if any, is statistically significant. 



### Copyright

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
