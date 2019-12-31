#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import Builder
from ..src import DataCollecterCmd as Cmd

class DataCollecterAPI(object):
	def __init__(self):
		builder = Builder.Builder()
		self.__mMain = builder.getDataCollecterMain()

	def __del__(self):
		pass

	def setTemperature(self, value):
		print("setTemperature--> ", value)
		print(self.__mMain)
		self.__mMain.notifyCommand(Cmd.DATA_CMD_SET_TEMP, [value])

	def getTemperature(self, cb):
		print("getTemperature--> ", cb)
		print(self.__mMain)
		self.__mMain.notifyCommand(Cmd.DATA_CMD_GET_TEMP, [None])

	def threadEnd(self):
		print("--> DisplayAPI Stop.")
		self.__mMain.notifyCommand(Cmd.DISPLAY_CMD_QUIT, None)
