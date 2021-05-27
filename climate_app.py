import numpy as np
import os

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
from datetime import datetime as dt
from datetime import timedelta 


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurements = Base.classes.measurement
Stations = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")
def prcp():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """ 1. Convert the query results to a dictionary using date 
        as the key and prcp as the value.
        
        2. Return the JSON representation of your dictionary."""
    
    # Query all precipiation measurements and group by date with avg
    results = session.query(Measurements.date, func.avg(Measurements.prcp)).\
    filter(Measurements.date > '2016-08-23').\
    group_by(Measurements.date).order_by(Measurements.date).all()

    session.close()

    # Convert list of tuples into dictionary
    prcp = dict(results)

    return jsonify(prcp)


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a JSON list of stations from the dataset."""
    # Query all stations
    results = session.query(Stations.station).all()

    session.close()

    # Create a JSON list of stations
    stations = list(np.ravel(results))

    return jsonify(stations)


@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """ 1. Query the dates and temperature observations of the most active 
        station for the last year of data.

        2. Return a JSON list of temperature observations (TOBS) for the previous year."""

    # Query most active station
    most_active_station = session.query(Stations.id, Stations.station).\
        filter(Measurements.station == Stations.station).\
        group_by(Measurements.station).order_by(func.count(Measurements.station).\
        desc()).first()
    
    # Query most recent date    
    most_recent_date = session.query(Measurements).\
        filter(Measurements.station == Stations.station).\
        filter(Stations.id == most_active_station.id).\
        order_by(Measurements.date.desc()).first()

    # Calculate date for 12 months prior         
    most_recent_date_dt_object = dt.strptime(most_recent_date.date, '%Y-%m-%d')

    one_year_before_most_recent = most_recent_date_dt_object.date() - timedelta(days=365)

    # Query temperature data for last 12 months at most active station
    most_active_station_12months = session.query(Measurements.date, Measurements.tobs).\
        filter(Measurements.station == Stations.station).\
        filter(Stations.id == most_active_station.id).\
        filter(Measurements.date <= most_recent_date.date, 
           Measurements.date > one_year_before_most_recent.strftime("%Y-%m-%d")).all() 
    
    
    session.close()

    # Create a JSON list of tobs data

    return jsonify(dict(most_active_station_12months))

@app.route("/api/v1.0/<start>")
def temps_start(start):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """ 1. Return a JSON list of the minimum temperature, the average temperature, 
        and the max temperature for a given start or start-end range. 
        
        2. When given the start only, calculate TMIN, TAVG, and TMAX for all dates 
        greater than and equal to the start date."""
 
   # Query most active station
    most_active_station = session.query(Stations.id, Stations.station).\
        filter(Measurements.station == Stations.station).\
        group_by(Measurements.station).order_by(func.count(Measurements.station).\
        desc()).first()
    
    # Query most recent date (the end date for this query)  
    most_recent_date = session.query(Measurements).\
        filter(Measurements.station == Stations.station).\
        filter(Stations.id == most_active_station.id).\
        order_by(Measurements.date.desc()).first()

    # Query temperature data beginning at start date
    min_temp, max_temp, avg_temp  = session.query(func.min(Measurements.tobs), 
            func.max(Measurements.tobs), 
            func.round(func.avg(Measurements.tobs), 1)).\
        filter(Measurements.station == Stations.station).\
        filter(Stations.id == most_active_station.id).\
        filter(Measurements.date >= start).all()[0]
    
    session.close()

    # Convert data into dictionary
    most_active_station_data = \
        {'Station ID' : most_active_station.id, 
        'Station Name' : most_active_station.station, 
        'Start Date' : start, 
        'End Date' : most_recent_date.date,
        'Min Temp' : min_temp, 
        'Avg Temp': avg_temp,
        'Max Temp': max_temp 
        }   
    
    return jsonify(most_active_station_data)

@app.route("/api/v1.0/<start>/<end>")
def temps_start_end(start, end):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """ 1. Return a JSON list of the minimum temperature, the average temperature, 
        and the max temperature for a given start or start-end range.
        
        2. When given the start and the end date, calculate the TMIN, TAVG, and TMAX 
        for dates between the start and end date inclusive."""

    # Query most active station
    most_active_station = session.query(Stations.id, Stations.station).\
        filter(Measurements.station == Stations.station).\
        group_by(Measurements.station).order_by(func.count(Measurements.station).\
        desc()).first()

    # Query temperature data beginning at start date
    min_temp, max_temp, avg_temp  = session.query(func.min(Measurements.tobs), 
            func.max(Measurements.tobs), 
            func.round(func.avg(Measurements.tobs), 1)).\
        filter(Measurements.station == Stations.station).\
        filter(Stations.id == most_active_station.id).\
        filter(Measurements.date >= start, Measurements.date >= end).all()[0]
    
    session.close()

    # Convert data into dictionary
    most_active_station_data = \
        {'Station ID' : most_active_station.id, 
        'Station Name' : most_active_station.station, 
        'Start Date' : start, 
        'End Date' : end,
        'Min Temp' : min_temp, 
        'Avg Temp': avg_temp,
        'Max Temp': max_temp 
        }     
    
    return jsonify(most_active_station_data)

if __name__ == '__main__':
    app.run(debug=True)
