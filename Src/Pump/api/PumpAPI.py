#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import Builder
from ..src import PumpCmd as Cmd

class PumpAPI(object):
	def __init__(self):
		builder = Builder.Builder()
		self.__mMain = builder.getPumpMain()

	def __del__(self):
		pass

	def threadEnd(self):
		print("--> PumpAPI Stop.")
		self.__mMain.notifyCommand(Cmd.PUMP_CMD_QUIT, None)
