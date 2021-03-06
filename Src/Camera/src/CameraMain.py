#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
from . import CameraIO
from . import ImageRecognition
from . import CameraCmd as Cmd
import LogPrint as LOG
import Semaphore

DEF_MYNAME = "Camera"

class CameraMain(threading.Thread):
	__mCommand	= []
	__mParam	= []
	__mDataCtr	= None
	__mIo		= None
	__mSem		= None
	__mRecog	= None

	def __init__(self, dataObj):
		threading.Thread.__init__(self)
		self.__mDataApi = dataObj
		self.__mIo = CameraIO.CameraIO()
		self.__mSem = Semaphore.Semaphore(DEF_MYNAME)
		self.__mRecog = ImageRecognition.ImageRecognition()

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

		if cmd == Cmd.CAMERA_CMD_QUIT:
			LOG.INFO(__name__, "--> CameraMain QUIT.[", param, "]")
			quit()

		elif cmd == Cmd.CAMERA_CMD_EXECUTE:
			result, fileName = self.__mIo.execute()
			if result == True:
				param[0](fileName)

				# 画像の色を判別
				r, g, b = self.__mRecog.execute(fileName)
				self.__mDataApi.setColor(r, g, b)
				self.__mDataApi.setPicture(fileName[fileName.rfind('/') + 1:])
				
		else:
			print("Cmd Error.")
			