#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
from . import TemperatureCmd as Cmd
from . import TemperatureIO

class TemperatureMain(threading.Thread):
	__mCommand	= []
	__mParam	= []
	__mDataCtr	= None

	def __init__(self, dataObj):
		threading.Thread.__init__(self)
		self.__mDataApi = dataObj
		self.__mSensor = TemperatureIO.TemperatureIO()

	def run(self):
		print("TemperatureMain start. [", id(self), "]")

		while True:
			print("---> TemperatureMain")
			
			self.__executeCommand()

			# 温度取得/格納
			value = self.__mSensor.get()
			self.__mDataApi.setTemperature(value)

			self.__mDataApi.getTemperature(None)
			time.sleep(1)
			

	def notifyCommand(self, cmd, param):
		self.__mCommand.append(cmd)
		self.__mParam.append(param)

	def __executeCommand(self):
		if len(self.__mCommand) == 0:
			return

		cmd = self.__mCommand.pop(0)
		param = self.__mParam.pop(0)
		if cmd == Cmd.TEMP_CMD_QUIT:
			print("--> TemperatureMain QUIT.[", param, "]")
			quit()

		else:
			print("Cmd Error.")
