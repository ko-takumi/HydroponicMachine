#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
from . import PumpCmd as Cmd
import LogPrint as LOG

class PumpMain(threading.Thread):
	__mCommand	= []
	__mParam	= []

	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		LOG.INFO(__name__, "Thread start. [{}]".format(hex(id(self))))

		while True:
			self.__executeCommand()
			time.sleep(1)

	def notifyCommand(self, cmd, param):
		self.__mCommand.append(cmd)
		self.__mParam.append(param)

	def __executeCommand(self):
		if len(self.__mCommand) == 0:
			return

		cmd = self.__mCommand.pop(0)
		param = self.__mParam.pop(0)
		if cmd == Cmd.PUMP_CMD_QUIT:
			print("--> PumpMain QUIT.[", param, "]")
			quit()

		else:
			print("Cmd Error.")
			