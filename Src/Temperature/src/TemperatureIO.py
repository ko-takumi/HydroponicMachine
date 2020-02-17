#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from . import dht11
import RPi.GPIO as GPIO
import LogPrint as LOG
# 暫定
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

TEMP_PIN = 14

class TemperatureIO(object):
	def __init__(self):
		self.__mTempSensor = dht11.DHT11(pin = TEMP_PIN)
		
	def get(self):
		result = self.__mTempSensor.read()
		success = result.is_valid()
		if success == True:
			temperature = result.temperature
			humidity = result.humidity
			return True, temperature, humidity

		LOG.ERROR(__name__, "self.__mTempSensor.read() is Error.")
		return False, 0.0, 0.0
