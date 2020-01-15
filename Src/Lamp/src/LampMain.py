#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
from . import LampIO
from . import LampCmd as Cmd
import LogPrint as LOG

class LampMain(threading.Thread):
	__mCommand	= []
	__mParam	= []
	__mIo		= None

	def __init__(self):
		threading.Thread.__init__(self)
		self.__mIo = LampIO.LampIO()

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
		if cmd == Cmd.LAMP_CMD_QUIT:
			LOG.INFO(__name__, "--> LampMain QUIT.[", param, "]")
			quit()

		elif cmd == Cmd.LAMP_CMD_ON:
			self.__mIo.on()

		elif cmd == Cmd.LAMP_CMD_OFF:
			self.__mIo.off(param[0])

		else:
			print("Cmd Error.")
			