#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
import Builder
from Pump.api import PumpAPI
from Camera.api import CameraAPI
from Lamp.api import LampAPI
import LogPrint as LOG
from Notify.src import LineNotify

DEF_LAMP_OFF_TIME = 3.0

class MainController(threading.Thread, LineNotify.LineNotify):
	def __init__(self):
		threading.Thread.__init__(self)
		LineNotify.LineNotify.__init__(self)
		self.__mApiPump		= PumpAPI.PumpAPI()
		self.__mApiCamera	= CameraAPI.CameraAPI()
		self.__mApiLamp		= LampAPI.LampAPI()

		builder = Builder.Builder()
		self.__mData = builder.getDataCollecterAPI()

		self.__mData.getTemperature(self.getTemperatureCB)
		self.sentMessage("START", "起動した")

	def run(self):
		LOG.INFO(__name__, "Thread start. [{}]".format(hex(id(self))))

		# 暫定
		while True:

			self.__mApiPump.execute(1)
			self.__takePhoto()

			self.__mData.getTemperature(self.getTemperatureCB)

			time.sleep(30*60)	# 暫定(0.5h)
			

	def __takePhoto(self):
		self.__mApiLamp.on()
		time.sleep(0.1)
		self.__mApiCamera.execute(self.getImageCB)
		self.__mApiLamp.off(DEF_LAMP_OFF_TIME)

	def getTemperatureCB(self, value):
		self.sentMessage("温度", str(value))

	def getImageCB(self, fileName):
		self.sendImage(fileName)
