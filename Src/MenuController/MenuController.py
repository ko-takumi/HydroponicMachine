#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
import Builder
from Switch.api import SwitchAPI
from . import MenuControllerCb
from . import MenuControllerCmd as Cmd
from . import MenuControllerProcess
import LogPrint as LOG
import Semaphore

DEF_MYNAME = "MenuController"

class MenuController(threading.Thread):
	__mCommand	= []
	__mParam	= []
	__mProcess	= None
	__mSem		= None
	
	def __init__(self):
		threading.Thread.__init__(self)
		self.__mProcess		= MenuControllerProcess.MenuControllerProcess()
		self.__mSem = Semaphore.Semaphore(DEF_MYNAME)

	def run(self):
		LOG.INFO(__name__, "Thread start. [{}]".format(hex(id(self))))
		cb = MenuControllerCb.MenuControllerCb(self)

		# 温度変更通知を登録
		builder = Builder.Builder()
		dataApi = builder.getDataCollecterAPI()
		dataApi.registerChangeTemprature(cb.getTemperatureCb)
		dataApi.registerChangeHumidity(cb.getHumidityCb)

		# スイッチ押下通知を登録
		self.__mApiSwitch	= SwitchAPI.SwitchAPI()
		self.__mApiSwitch.registerPushSw(cb.notifyPushSWCb)

		while True:
			# コマンド実行
			self.__executeCommand()

			# 周期実行
			self.__mProcess.execute()

			time.sleep(0.5)

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

		if cmd == Cmd.MENU_CMD_QUIT:
			LOG.INFO(__name__, "Thread QUIT. [{}]".format(hex(id(self))))
			quit()

		elif cmd == Cmd.MENU_CMD_GET_TEMP:
			self.__mProcess.updataTemperature(param[0])

		elif cmd == Cmd.MENU_CMD_GET_HUMID:
			self.__mProcess.updataHumidity(param[0])

		elif cmd == Cmd.MENU_CMD_PUSH_SW:
			self.__mProcess.notifyPushSW()

		else:
			LOG.ERROR(__name__, "{} {}".format(cmd, param))
