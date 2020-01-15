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

		while True:
			time.sleep(1)
			# self.__takePhoto()

	def __takePhoto(self):
		self.__mApiLamp.on()
		time.sleep(0.1)
		self.__mApiCamera.execute()
		self.__mApiLamp.off(DEF_LAMP_OFF_TIME)
