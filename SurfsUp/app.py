# Import the dependencies.
from flask import Flask, jsonify
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
M = Base.classes.measurement
S = Base.classes.station

#################################################
# Flask Setup
#################################################
app= Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route('/')
def home():
    return '''
        <h2>Available routes:</h2>
            <ul>
                <li>/api/v1.0/precipitation</li>
                <li>/api/v1.0/stations</li>
                <li>/api/v1.0/tobs</li>
                <li>/api/v1.0/<start></li> 
                <li>/api/v1.0/<start>/<end></li> 
            </ul>
                '''

@app.route('/api/v1.0/precipitation')
def precipitation():
    session = Session(bind=engine)
    results = session.query(M.date, M.prcp).filter(M.date >= '2016-08-23').all()
    
    return [ {d:p} for d,p in results ]



@app.route('/api/v1.0/stations')
def stations():
    session = Session(bind=engine)
    stations = session.query(S.station).distinct().all()
    station_list = [station[0] for station in stations]
    
    return jsonify({'stations': station_list})


@app.route('/api/v1.0/tobs')
def tobs():
    session = Session(bind=engine)
    most_active_station = 'USC00519281'
    
    lastdate = session.query(func.max(M.date)).first()[0]
    lastdate = dt.datetime.strptime(lastdate, '%Y-%m-%d').date()
    preyear = lastdate - dt.timedelta(days=365)
   
    temperature_data = session.query(M.date, M.tobs) \
                              .filter(M.station == most_active_station) \
                              .filter(M.date >= preyear) \
                              .all()
    temperature_list = [{'date': date, 'tobs': tobs} for date, tobs in temperature_data]
    
    return jsonify(temperature_list)

@app.route('/api/v1.0/<start>')
def temp_start(start):
    with Session(engine) as session:
        results = session.query(func.min(M.tobs), func.max(M.tobs), func.avg(M.tobs)) \
                 .filter(M.date >= start) \
                 .all()

    start_list = [{'TMIN': results[0][0], 'TAVG': results[0][1], 'TMAX': results[0][2]}]
    return jsonify(start_list)
    

@app.route("/api/v1.0/<start>/<end>")
def temp_range(start, end):
    
    with Session(engine) as session:
       
        results = session.query(func.min(M.tobs), func.avg(M.tobs), func.max(M.tobs)).\
            filter(M.date >= start, M.date <= end).all()
    
    date_list = [{'TMIN': results[0][0], 'TAVG': results[0][1], 'TMAX': results[0][2]}]
    return jsonify(date_list)


if __name__ == '__main__':
    app.run(debug=True)



    
