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
	__mSetValue = None

	def __init__(self):
		threading.Thread.__init__(self)
		self.__mProc = DataCollecterProcess.DataCollecterProcess()
		self.__mSem = Semaphore.Semaphore(DEF_MYNAME)

		# 各設定値を取得する
		self.__mSetValue = self.__mProc.getSettingData()

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

	def getParameter(self):
		if self.__mSetValue == None:
			LOG.ERROR(__name__, "__mSetValue is Error.")

		return self.__mSetValue

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
			self.__mProc.updateTemperature(param[0])
			
			isSave = param[1]
			if isSave == True:
				self.__mProc.setTemperature(param[0])

			for cbFunc in self.__mRegGetTempCb:
				cbFunc(param[0])

		elif cmd == Cmd.DATA_CMD_GET_TEMP:	# 温度取得
			value = self.__mProc.getTemperature()
			param[0](value)

		elif cmd == Cmd.DATA_CMD_SET_HUMID:	# 湿度格納
			self.__mProc.updateHumidity(param[0])

			isSave = param[1]
			if isSave == True:
				self.__mProc.setHumidity(param[0])

			for cbFunc in self.__mRegGetHumidityCb:
				cbFunc(param[0])

		elif cmd == Cmd.DATA_CMD_GET_HUMID:	# 湿度取得
			value = self.__mProc.getHumidity()
			param[0](value)

		elif cmd == Cmd.DATA_CMD_SET_PICTURE: # 画像格納
			fileName = param[0]
			self.__mProc.setPicture(fileName)

		elif cmd == Cmd.DATA_CMD_SET_COLOR:	# 色格納
			self.__mProc.setColor(param[0], param[1], param[2])
			self.__mProc.updateGrowth(param[0], param[1], param[2])

		elif cmd == Cmd.DATA_CMD_REG_CHANGETEMP:
			self.__mRegGetTempCb.append(param[0])

		elif cmd == Cmd.DATA_CMD_REG_CHANGEHUMID:
			self.__mRegGetHumidityCb.append(param[0])

		else:
			LOG.ERROR(__name__, "{} {}".format(cmd, param))
			