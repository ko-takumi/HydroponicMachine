#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import LogPrint as LOG
import RPi.GPIO as GPIO

class PumpIO(object):
	__mPin = 0
	def __init__(self, pin):
		self.__mPin = pin
		GPIO.setup(self.__mPin, GPIO.OUT)

		# wakeup
		for t in [1, 0.5, 0.5]:
			GPIO.output(self.__mPin, GPIO.HIGH)
			time.sleep(t)
			GPIO.output(self.__mPin, GPIO.LOW)
			time.sleep(t)

	def __del__(self):
		pass

	def on(self):
		LOG.INFO(__name__, "ON.")
		GPIO.output(self.__mPin, GPIO.HIGH)

	def off(self):
		LOG.INFO(__name__, "OFF.")
		GPIO.output(self.__mPin, GPIO.LOW)
		