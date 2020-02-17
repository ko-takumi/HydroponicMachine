#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
from . import DisplayCmd as Cmd
from . import DisplayProcess
import LogPrint as LOG

class DisplayMain(threading.Thread):
	__mCommand	= []
	__mParam	= []
	__mProcess	= None

	def __init__(self, dataObj):
		threading.Thread.__init__(self)
		self.__mDataApi = dataObj
		self.__mProcess = DisplayProcess.DisplayProcess(self.__mDataApi)

	def run(self):
		LOG.INFO(__name__, "Thread start. [{}]".format(hex(id(self))))

		while True:
			# コマンド実行
			self.__executeCommand()

			# 周期実行
			self.__mProcess.execute()

			time.sleep(0.5)

	def notifyCommand(self, cmd, param):
		self.__mCommand.append(cmd)
		self.__mParam.append(param)

	def __executeCommand(self):
		if len(self.__mCommand) == 0:
			return

		cmd = self.__mCommand.pop(0)
		param = self.__mParam.pop(0)
		if cmd == Cmd.DISPLAY_CMD_QUIT:
			LOG.INFO(__name__, "Thread QUIT. [{}]".format(hex(id(self))))
			quit()

		elif cmd == Cmd.DISPLAY_CMD_NOTIFY_TEMP:
			LOG.INFO(__name__, "{}: {}".format(cmd, param))
			self.__mProcess.notifyTemperature(param[0])

		elif cmd == Cmd.DISPLAY_CMD_NOTIFY_HUMID:
			LOG.INFO(__name__, "{}: {}".format(cmd, param))
			self.__mProcess.notifyHumidity(param[0])

		elif cmd == Cmd.DISPLAY_CMD_NOTIFY_IPADDRESS:
			LOG.INFO(__name__, "{}: {}".format(cmd, param))
			self.__mProcess.notifyIPAddress(param[0])

		elif cmd == Cmd.DISPLAY_CMD_NOTIFY_CHANGEMODE:
			LOG.INFO(__name__, "{}: {}".format(cmd, param))
			self.__mProcess.notifyChangeMode()

		else:
			LOG.ERROR(__name__, "{} {}".format(cmd, param))
			