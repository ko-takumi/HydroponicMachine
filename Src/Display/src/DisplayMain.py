#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
from . import DisplayCmd as Cmd

class DisplayMain(threading.Thread):
	__mCommand	= []
	__mParam	= []

	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		print("DisplayMain start. [", id(self), "]")

		while True:
			print("---> DisplayMain")
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
		if cmd == Cmd.DISPLAY_CMD_QUIT:
			print("--> DisplayMain QUIT.[", param, "]")
			quit()

		else:
			print("Cmd Error.")
			