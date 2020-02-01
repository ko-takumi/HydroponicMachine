#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
from Pump.api import PumpAPI
from Camera.api import CameraAPI
from Lamp.api import LampAPI
import LogPrint as LOG

DEF_LAMP_OFF_TIME = 3.0

class MainController(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.__mApiPump		= PumpAPI.PumpAPI()
		self.__mApiCamera	= CameraAPI.CameraAPI()
		self.__mApiLamp		= LampAPI.LampAPI()

	def run(self):
		LOG.INFO(__name__, "Thread start. [{}]".format(hex(id(self))))

		# 暫定
		while True:
			self.__mApiPump.execute(3)
			self.__takePhoto()
			time.sleep(10)	# 暫定(1h)
			

	def __takePhoto(self):
		self.__mApiLamp.on()
		time.sleep(0.1)
		self.__mApiCamera.execute()
		self.__mApiLamp.off(DEF_LAMP_OFF_TIME)
