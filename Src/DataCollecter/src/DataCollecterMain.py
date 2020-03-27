#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
from . import DataCollecterProcess
from . import DataCollecterCmd as Cmd
import LogPrint as LOG
import Semaphore

DEF_MYNAME = "DataCollecter"

class DataCollecterMain(threading.Thread):
	__mCommand	= []
	__mParam	= []
	__mRegGetTempCb = []
	__mRegGetHumidityCb = []
	__mSem	= None

	def __init__(self):
		threading.Thread.__init__(self)
		self.__mProc = DataCollecterProcess.DataCollecterProcess()
		self.__mSem = Semaphore.Semaphore(DEF_MYNAME)

	def run(self):
		LOG.INFO(__name__, "Thread start. [{}]".format(hex(id(self))))

		while True:
			self.__executeCommand()
			time.sleep(0.1)

	def notifyCommand(self, cmd, param):
		self.__mSem.lock()
		self.__mCommand.append(cmd)
		self.__mParam.append(param)
		self.__mSem.unlock()

	def __executeCommand(self):
		if len(self.__mCommand) == 0:
			return

		self.__mSem.lock()
		cmd = self.__mCommand.pop(0)
		param = self.__mParam.pop(0)
		self.__mSem.unlock()

		if cmd == Cmd.DATA_CMD_QUIT:
			LOG.INFO(__name__, "Thread QUIT. [{}]".format(hex(id(self))))
			quit()

		elif cmd == Cmd.DATA_CMD_SET_TEMP:	# 温度格納
			isSave = param[1]
			if isSave == True:
				self.__mProc.setTemperature(param[0])

			for cbFunc in self.__mRegGetTempCb:
				cbFunc(param[0])

		elif cmd == Cmd.DATA_CMD_GET_TEMP:	# 温度取得
			value = self.__mProc.getTemperature()
			param[0](value)

		elif cmd == Cmd.DATA_CMD_SET_HUMID:	# 湿度格納
			isSave = param[1]
			if isSave == True:
				self.__mProc.setHumidity(param[0])
				
			for cbFunc in self.__mRegGetHumidityCb:
				cbFunc(param[0])

		elif cmd == Cmd.DATA_CMD_GET_HUMID:	# 湿度取得
			value = self.__mProc.getHumidity()
			param[0](value)

		elif cmd == Cmd.DATA_CMD_REG_CHANGETEMP:
			self.__mRegGetTempCb.append(param[0])

		elif cmd == Cmd.DATA_CMD_REG_CHANGEHUMID:
			self.__mRegGetHumidityCb.append(param[0])

		else:
			LOG.ERROR(__name__, "{} {}".format(cmd, param))
			