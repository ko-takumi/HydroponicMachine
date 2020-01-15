#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import Builder
from ..src import CameraCmd as Cmd

class CameraAPI(object):
	def __init__(self):
		builder = Builder.Builder()
		self.__mMain = builder.getCameraMain()

	def __del__(self):
		pass

	def execute(self):
		self.__mMain.notifyCommand(Cmd.CAMERA_CMD_EXECUTE, None)

	def threadEnd(self):
		print("--> CameraAPI Stop.")
		self.__mMain.notifyCommand(Cmd.CAMERA_CMD_QUIT, None)
