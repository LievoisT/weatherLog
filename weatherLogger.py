import requests
import datetime
from datetime import date
from time import sleep
import csv
from os import path


while True:
    today_filename = f'./{date.today().month}-{date.today().day}-{date.today().year}.csv'

    if not path.isfile(today_filename):
        with open(today_filename, 'w') as newfile:
            header_writer = csv.writer(newfile, quoting=csv.QUOTE_MINIMAL)
            header_writer.writerow(['dt', 'wind_speed', 'wind_direction'])

    try:
        r = requests.get('http://192.168.4.1/get_livedata_info').json()

        wind_speed = r['common_list'][6]['val']
        wind_dir = r['common_list'][11]['val']

        with open(today_filename, 'a') as csvfile:
            weather_writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
            weather_writer.writerow([datetime.datetime.now(), wind_speed, wind_dir])

    except ValueError:
        pass

    sleep(60)
