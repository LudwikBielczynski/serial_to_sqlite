import json
import sys
import time
from typing import Dict, Optional
import warnings

from flask import Flask, jsonify, make_response
from flask_httpauth import HTTPBasicAuth
import pandas as pd
from werkzeug.security import generate_password_hash, check_password_hash

from common.shares import LOCAL_DATABASES_PATH, AUTH_PATH

from repositories.database import WateringSchedule
from repositories.database.sqlite import DatabaseSqlite

from watering_controller.relay import load_channel_section_name_map

warnings.simplefilter(action='ignore', category=FutureWarning)

app = Flask(__name__)
auth = HTTPBasicAuth()

with open(AUTH_PATH, 'r') as json_data:
    users = json.load(json_data)

DEFAULT_APP_PORT = 5000

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

def check_inputs(channel: int,
                 weekday: Optional[int] = None,
                 start_time_utc: Optional[str] = None,
                 end_time_utc: Optional[str] = None,
                ):
    channel_section_name_map = load_channel_section_name_map()
    if channel not in channel_section_name_map.keys():
        raise AttributeError('The channel was not set in the configuration')

    if weekday:
        if weekday not in range(0,8):
            raise AttributeError('For weekdays only values from 0-7 are acceptable')

    if (not start_time_utc is None) & (not end_time_utc is None):
        def check_time(time):
            '''Checks if the string representing time is well formed'''
            hours = int(time.split(':')[0])
            if (hours >= 24) | (hours < 0):
               raise AttributeError('Hours should be between 0 and 24')

            minutes = int(time.split(':')[1])
            if (minutes >= 60) | (minutes < 0):
               raise AttributeError('Minutes should be between 0 and 60')

        check_time(start_time_utc)
        check_time(end_time_utc)

        if int(start_time_utc.split(':')[0]) > int(end_time_utc.split(':')[0]):
            raise AttributeError('The end time should be later than the start time')
        elif int(start_time_utc.split(':')[0]) == int(end_time_utc.split(':')[0]):
            if int(start_time_utc.split(':')[1]) > int(end_time_utc.split(':')[1]):
                raise AttributeError('The end time should be later than the start time')

@app.route('/health/ready', methods=['GET'])
def check_readiness() -> str:
    '''
    This method is used to check the readiness of the API.

    Example:
    curl -i -H "Content-Type: application/json" -X GET http://localhost:5000/health/ready
    '''
    return jsonify({'status': 'ready'})

@app.route('/get_schedule', methods=['GET'])
@auth.login_required
def get_schedule_route():
    '''
    This method is used to get the full watering scheduls

    Example:
    curl -i -H "Content-Type: application/json" -X GET http://localhost:5000/get_schedule
    '''

    # Delete the local database a new schedule
    database_sqlite = DatabaseSqlite(LOCAL_DATABASES_PATH, 'watering_schedule.db')
    watering_schedule = WateringSchedule(database_sqlite)
    schedule = watering_schedule.get_all_schedule()

    return jsonify(schedule.T.to_dict())

@app.route('/get_relay_configuration', methods=['GET'])
@auth.login_required
def get_relay_configuration_route():
    '''
    This method is used to get relay configuration

    Example:
    curl -i -H "Content-Type: application/json" -X GET http://localhost:5000/get_relay_configuration
    '''
    return jsonify(load_channel_section_name_map())

@app.route('/schedule_watering/<int:channel>_<start_time_utc>-<end_time_utc>_<int:weekday>', methods=['PUT'])
@auth.login_required
def schedule_watering_route(channel: int,
                            start_time_utc: str,
                            end_time_utc: str,
                            weekday: int,
                           ):
    '''
    This method is used to schedule watering for a selected weekday channel combination, and for
    selected time range.

    Example:
    curl -i -H "Content-Type: application/json" -X PUT http://localhost:5000/schedule_watering/1_10:00-20:00_1
    '''
    # Perform checks of all attributes
    check_inputs(channel, weekday, start_time_utc, end_time_utc)

    # Try to insert to the local database a new schedule
    LOCAL_DATABASES_PATH.mkdir(parents=True, exist_ok=True)

    database_sqlite = DatabaseSqlite(LOCAL_DATABASES_PATH, 'watering_schedule.db')
    watering_schedule = WateringSchedule(database_sqlite)

    now = pd.Timestamp.utcnow()
    scheduled_watering = {'insert_datetime_utc': now.to_pydatetime(),
                          'channel': channel,
                          'start_time_utc': start_time_utc,
                          'end_time_utc': end_time_utc,
                          'weekday': weekday,
                         }

    # Check if there is something scheduled for that channel and weekday combination
    is_already_scheduled = watering_schedule.check_if_already_scheduled(channel, weekday)
    if is_already_scheduled:
        raise Exception(f'For channel {channel} and weekday {weekday} there was already watering scheduled')
    else:
        watering_schedule.schedule_watering(scheduled_watering)

    return jsonify({'status': 'data added to local database'})

@app.route('/delete_for_channel_weekday_watering_schedule/<int:channel>_<int:weekday>', methods=['PUT'])
@auth.login_required
def delete_for_channel_weekday_watering_schedule_route(channel: int, weekday: int):
    '''
    This method is used to clear watering schedule for a selected weekday channel combination.

    Example:
    curl -i -H "Content-Type: application/json" -X PUT http://localhost:5000/delete_for_channel_weekday_watering_schedule/1_1
    '''
    # Perform checks of all attributes
    check_inputs(channel, weekday)

    # Delete the local database a new schedule
    database_sqlite = DatabaseSqlite(LOCAL_DATABASES_PATH, 'watering_schedule.db')
    watering_schedule = WateringSchedule(database_sqlite)
    watering_schedule.delete_for_channel_weekday_schedule(channel, weekday)

    return jsonify({'status': f'data for channel {channel} and weekday {weekday} was deleted'})

@app.route('/delete_for_channel_watering_schedule/<int:channel>', methods=['PUT'])
@auth.login_required
def delete_for_channel_watering_schedule_route(channel: int):
    '''
    This method is used to clear watering schedule for a selected weekday channel combination.

    Example:
    curl -i -H "Content-Type: application/json" -X PUT http://localhost:5000/delete_for_channel_watering_schedule/1
    '''
    # Perform checks of all attributes
    check_inputs(channel)

    # Delete the local database a new schedule
    database_sqlite = DatabaseSqlite(LOCAL_DATABASES_PATH, 'watering_schedule.db')
    watering_schedule = WateringSchedule(database_sqlite)
    watering_schedule.delete_for_channel_schedule(channel)

    return jsonify({'status': f'data for channel {channel} was deleted'})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'URL not found'}), 404)

if __name__ == '__main__':
    port = DEFAULT_APP_PORT
    if len(sys.argv) > 1:
        port = int(sys.argv[1])

    app.run(debug=False,
            host='0.0.0.0',
            # processes=3,
            port=port,
            threaded=True)
