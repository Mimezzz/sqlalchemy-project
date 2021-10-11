from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine,func
from flask import Flask,jsonify
import datetime as dt

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

session = Session(engine)
station = Base.classes.station
measurement = Base.classes.measurement

app = Flask(__name__)

@app.route('/')
def home():
    return (
        f"Welcome to the Home Page!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"Query dates:<br/>"
        f"/api/v1.0/startdate<br/>"
        f"/api/v1.0/startdate/enddate<br/>"
        f"For example:/api/v1.0/2016-08-08/2016-12-21<br/><br/> "
        f"NOTICE:<br/>"
        f"Please input the start/end date in (YYYY-MM-DD)format,<br/>"
        f"and the start date should not be later than 2017-08-23."
    )



@app.route('/api/v1.0/precipitation')
def prcp():
    result=session.query(measurement.date,measurement.prcp).all()
    print(result)
    prcp = []
    for date, prcp in result:
        prcp_dict = {}
        prcp_dict[date] = prcp
        prcp.append(prcp_dict)

    return jsonify(prcp)

@app.route('/api/v1.0/stations')
def sta():
    station_list=[]
    result=session.query(station.station).distinct().all()
    i=0
    for x in result:
        station_dict = {}
        i=i+1
        station_dict[i]=x[0]
        station_list.append(station_dict)
    return jsonify(station_list)

@app.route('/api/v1.0/tobs')
def tobs():
    latest_date = session.query(measurement.date).order_by(measurement.date.desc()).first()
    latest_date = dt.date(2017, 8, 23)
    one_year_ago = latest_date - dt.timedelta(days=365)
    active_sta = session.query(measurement.station, func.count(measurement.station)).\
        group_by(measurement.station).order_by(func.count(measurement.station).desc()).first()
    sel = [measurement.date,
           measurement.tobs]
    station_temp = session.query(*sel). \
        filter(measurement.station == active_sta[0]). \
        filter(measurement.date >= one_year_ago).all()
    tob_list=[]
    for x in station_temp:
        tob_dict={}
        tob_dict['date']=x[0]
        tob_dict['tem']=x[1]
        tob_list.append(tob_dict)
    return jsonify(tob_list)

@app.route('/api/v1.0/<startdate>')
def start(startdate):
    latest_date = session.query(measurement.date).order_by(measurement.date.desc()).first()
    start_date=dt.datetime.strptime(startdate, '%Y-%m-%d').date()
    result=session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).\
        filter(measurement.date >= start_date).all()

    return (
        f'From {startdate} to {latest_date[0]}<br/>'
        f'the minimum temperature is {result[0][0]}<br/>'
        f'the average temperature is {result[0][1]}<br/>'
        f'the maximum temperature is {result[0][2]}'
)


@app.route('/api/v1.0/<startdate>/<enddate>')
def start_end(startdate,enddate):
    start_date=dt.datetime.strptime(startdate,'%Y-%m-%d').date()
    end_date=dt.datetime.strptime(enddate,'%Y-%m-%d').date()
    result = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)). \
        filter(measurement.date >= start_date).filter(measurement.date<=end_date).all()
    return (
            f'From {startdate} to {enddate}<br/>'
            f'the minimum temperature is {result[0][0]}<br/>'
            f'the average temperature is {result[0][1]}<br/>'
            f'the maximum temperature is {result[0][2]}'
    )



if __name__ == "__main__":
    app.run(debug=True)