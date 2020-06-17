#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
from . import LampIO
from . import LampCmd as Cmd
import LogPrint as LOG
import Semaphore

DEF_PIN = 15
DEF_MYNAME = "Lamp"

class LampMain(threading.Thread):
	__mCommand	= []
	__mParam	= []
	__mIo		= None
	__mSem	= None

	def __init__(self):
		threading.Thread.__init__(self)
		self.__mIo = LampIO.LampIO(DEF_PIN)
		self.__mSem = Semaphore.Semaphore(DEF_MYNAME)

	def run(self):
		LOG.INFO(__name__, "Thread start. [{}]".format(hex(id(self))))

		while True:
			self.__executeCommand()
			time.sleep(1)

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

		if cmd == Cmd.LAMP_CMD_QUIT:
			LOG.INFO(__name__, "--> LampMain QUIT.[", param, "]")
			quit()

		elif cmd == Cmd.LAMP_CMD_ON:
			self.__mIo.on()

		elif cmd == Cmd.LAMP_CMD_OFF:
			self.__mIo.off(param[0])

		else:
			print("Cmd Error.")
			