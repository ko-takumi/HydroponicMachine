#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import Builder
from ..src import LampCmd as Cmd

class LampAPI(object):
	def __init__(self):
		builder = Builder.Builder()
		self.__mMain = builder.getLampMain()

	def __del__(self):
		pass

	def on(self):
		self.__mMain.notifyCommand(Cmd.LAMP_CMD_ON, None)

	def off(self, offTime):
		self.__mMain.notifyCommand(Cmd.LAMP_CMD_OFF, [offTime])

	def threadEnd(self):
		print("--> LampAPI Stop.")
		self.__mMain.notifyCommand(Cmd.LAMP_CMD_QUIT, None)
