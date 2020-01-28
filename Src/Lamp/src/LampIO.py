#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import LogPrint as LOG
import RPi.GPIO as GPIO

DEF_PIN = 15

class LampIO(object):
	__mPin = DEF_PIN
	def __init__(self):
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

	def off(self, offTime):
		LOG.INFO(__name__, "OFF---->.")
		time.sleep(offTime)
		GPIO.output(self.__mPin, GPIO.LOW)
		LOG.INFO(__name__, "<----OFF.")