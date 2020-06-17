#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
from . import TemperatureCmd as Cmd
from . import TemperatureIO
import LogPrint as LOG
import Semaphore

DEF_MYNAME = "Temperature"

class TemperatureMain(threading.Thread):
	__mCommand	= []
	__mParam	= []
	__mDataCtr	= None
	__mSubThreadFlag = True
	__mIsSave = False
	__mJudgeSaveThread = None
	__mSaveTime = 0

	def __init__(self, dataObj, saveTime):
		threading.Thread.__init__(self)
		self.__mDataApi = dataObj
		self.__mSensor = TemperatureIO.TemperatureIO()
		self.__mSem = Semaphore.Semaphore(DEF_MYNAME)
		self.__mSaveTime = saveTime
		LOG.INFO(__name__, "save time[{}]".format(self.__mSaveTime))

		# save判定スレッド生成
		self.__mJudgeSaveThread = threading.Thread(target=self.__executeJudgeSave)
		self.__mJudgeSaveThread.start()

	def __executeJudgeSave(self):
		while self.__mSubThreadFlag:
			self.__mIsSave = True
			time.sleep(self.__mSaveTime)

	def run(self):
		LOG.INFO(__name__, "Thread start. [{}]".format(hex(id(self))))

		while True:			
			self.__executeCommand()

			# 温度取得/格納
			result, temperature, humidity = self.__mSensor.get()
			if result == True:
				if self.__mIsSave == True:
					self.__mDataApi.setTemperature(temperature, True)
					self.__mDataApi.setHumidity(humidity, True)
					self.__mIsSave = False
				else:
					self.__mDataApi.setTemperature(temperature, False)
					self.__mDataApi.setHumidity(humidity, False)
			else:
				LOG.ERROR(__name__, "self.__mSensor.get() is Error.")

			time.sleep(10)

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

		if cmd == Cmd.TEMP_CMD_QUIT:
			LOG.INFO(__name__, "Thread QUIT. [{}]".format(hex(id(self))))
			quit()

		else:
			LOG.ERROR(__name__, "{} {}".format(cmd, param))
