#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
from . import DataCollecterProcess
from . import DataCollecterCmd as Cmd
import LogPrint as LOG

class DataCollecterMain(threading.Thread):
	__mCommand	= []
	__mParam	= []
	__mRegGetTempCb = []

	def __init__(self):
		threading.Thread.__init__(self)
		self.__mProc = DataCollecterProcess.DataCollecterProcess()

	def run(self):
		LOG.INFO(__name__, "Thread start. [{}]".format(hex(id(self))))

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
			LOG.INFO(__name__, "Thread QUIT. [{}]".format(hex(id(self))))
			quit()

		elif cmd == Cmd.DATA_CMD_SET_TEMP:	# 温度格納
			self.__mProc.setTemperature(param[0])
			for cbFunc in self.__mRegGetTempCb:
				cbFunc(param[0])

		elif cmd == Cmd.DATA_CMD_GET_TEMP:	# 温度取得
			value = self.__mProc.getTemperature()
			param[0](value)

		elif cmd == Cmd.DATA_CMD_REG_CHANGETEMP:
			self.__mRegGetTempCb.append(param[0])

		else:
			LOG.ERROR(__name__, "{} {}".format(cmd, param))
			