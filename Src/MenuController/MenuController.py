#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
import Builder
from . import MenuControllerCb
from . import MenuControllerCmd as Cmd
from . import MenuControllerProcess
import LogPrint as LOG

class MenuController(threading.Thread):
	__mCommand	= []
	__mParam	= []
	__mProcess	= None
	
	def __init__(self):
		threading.Thread.__init__(self)
		self.__mProcess		= MenuControllerProcess.MenuControllerProcess()

	def run(self):
		LOG.INFO(__name__, "Thread start. [{}]".format(hex(id(self))))
		cb = MenuControllerCb.MenuControllerCb(self)

		# 温度変更通知を登録
		builder = Builder.Builder()
		dataApi = builder.getDataCollecterAPI()
		dataApi.registerChangeTemprature(cb.getTemperatureCb)

		while True:
			# コマンド実行
			self.__executeCommand()

			# 周期実行
			self.__mProcess.execute()

			time.sleep(1)

	def notifyCommand(self, cmd, param):
		self.__mCommand.append(cmd)
		self.__mParam.append(param)

	def __executeCommand(self):
		if len(self.__mCommand) == 0:
			return

		cmd = self.__mCommand.pop(0)
		param = self.__mParam.pop(0)
		if cmd == Cmd.MENU_CMD_QUIT:
			LOG.INFO(__name__, "Thread QUIT. [{}]".format(hex(id(self))))
			quit()

		elif cmd == Cmd.MENU_CMD_GET_TEMP:
			self.__mProcess.updataTemperature(param[0])

		else:
			LOG.ERROR(__name__, "{} {}".format(cmd, param))
