#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
from . import SwitchCmd as Cmd
import LogPrint as LOG

class SwitchMain(threading.Thread):
	__mCommand	= []
	__mParam	= []
	__mRegPushSwCb = []

	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		LOG.INFO(__name__, "Thread start. [{}]".format(hex(id(self))))

		while True:
			# お試し
			'''
			for cbFunc in self.__mRegPushSwCb:
				cbFunc()
			'''
				
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
		if cmd == Cmd.SWITCH_CMD_QUIT:
			print("--> SwitchMain QUIT.[", param, "]")
			quit()

		elif cmd == Cmd.SWITCH_CMD_REG_PUSHSW:
			self.__mRegPushSwCb.append(param[0])

		else:
			print("Cmd Error.")
			