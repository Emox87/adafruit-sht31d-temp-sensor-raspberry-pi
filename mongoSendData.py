#!/usr/bin/python3
import RPi.GPIO as GPIO
import pymongo
from pymongo import MongoClient
import board
import busio
import adafruit_sht31d
import datetime
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_sht31d.SHT31D(i2c)
h = float("{0:.2f}".format(sensor.relative_humidity))
t = float("{0:.2f}".format(sensor.temperature))
url = 'mongodb://192.168.0.10:27017'
client = MongoClient(url)
db = client.room1
collection = db.env
query_data = {
    'time': datetime.datetime.now(),
    'temperature': t,
    'humidity': h
}
result = collection.insert_one(query_data)