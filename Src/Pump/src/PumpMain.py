#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
from . import PumpCmd as Cmd
from . import PumpIO
import LogPrint as LOG
import Semaphore

DEF_PIN = 18
DEF_MYNAME = "Pump"

class PumpMain(threading.Thread):
	__mCommand	= []
	__mParam	= []
	__mIo		= None
	__mSem		= None

	def __init__(self):
		threading.Thread.__init__(self)
		self.__mIo = PumpIO.PumpIO(DEF_PIN)
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
		
		if cmd == Cmd.PUMP_CMD_QUIT:
			print("--> PumpMain QUIT.[", param, "]")
			quit()

		elif cmd == Cmd.PUMP_CMD_EXECUTE:
			self.__executePump(int(param[0]))

		else:
			print("Cmd Error.")
		
	def __executePump(self, waitTime):
		self.__mIo.on()
		time.sleep(waitTime)
		self.__mIo.off()
