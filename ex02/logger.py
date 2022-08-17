from datetime import datetime as dt
from time import time

def temperatureLogger(data):
    time=dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{}; temperature;{}'.format(time.data))

def pressureLogger(data):
    time=dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{}; pressure;{}'.format(time.data))

def windSpeedLogger(data):
    time=dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{}; windSpeed;{}'.format(time.data))