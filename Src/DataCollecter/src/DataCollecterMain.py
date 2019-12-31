#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
from . import DataCollecterProcess
from . import DataCollecterCmd as Cmd

class DataCollecterMain(threading.Thread):
	__mCommand	= []
	__mParam	= []

	def __init__(self):
		threading.Thread.__init__(self)
		self.__mProc = DataCollecterProcess.DataCollecterProcess()

	def run(self):
		print("DataCollecterMain start. [", id(self), "]")

		while True:
			self.__executeCommand()
			time.sleep(0.1)

	def notifyCommand(self, cmd, param):
		self.__mCommand.append(cmd)
		self.__mParam.append(param)

	def __executeCommand(self):
		if len(self.__mCommand) == 0:
			return

		cmd = self.__mCommand.pop(0)
		param = self.__mParam.pop(0)
		if cmd == Cmd.DATA_CMD_QUIT:
			print("--> DataCollecterMain QUIT.[", param, "]")
			quit()
		elif cmd == Cmd.DATA_CMD_SET_TEMP:	# 温度格納
			self.__mProc.setTemperature(param[0])

		elif cmd == Cmd.DATA_CMD_GET_TEMP:	# 温度取得
			self.__mProc.getTemperature()

		else:
			print("Cmd Error.")
			