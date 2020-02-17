#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
from . import TemperatureCmd as Cmd
from . import TemperatureIO
import LogPrint as LOG

class TemperatureMain(threading.Thread):
	__mCommand	= []
	__mParam	= []
	__mDataCtr	= None

	def __init__(self, dataObj):
		threading.Thread.__init__(self)
		self.__mDataApi = dataObj
		self.__mSensor = TemperatureIO.TemperatureIO()

	def run(self):
		LOG.INFO(__name__, "Thread start. [{}]".format(hex(id(self))))

		while True:			
			self.__executeCommand()

			# 温度取得/格納
			result, temperature, humidity = self.__mSensor.get()
			if result == True:
				self.__mDataApi.setTemperature(temperature)
				self.__mDataApi.setHumidity(humidity)
			else:
				LOG.ERROR(__name__, "self.__mSensor.get() is Error.")

			time.sleep(10)

	def notifyCommand(self, cmd, param):
		self.__mCommand.append(cmd)
		self.__mParam.append(param)

	def __executeCommand(self):
		if len(self.__mCommand) == 0:
			return

		cmd = self.__mCommand.pop(0)
		param = self.__mParam.pop(0)
		if cmd == Cmd.TEMP_CMD_QUIT:
			LOG.INFO(__name__, "Thread QUIT. [{}]".format(hex(id(self))))
			quit()

		else:
			LOG.ERROR(__name__, "{} {}".format(cmd, param))
