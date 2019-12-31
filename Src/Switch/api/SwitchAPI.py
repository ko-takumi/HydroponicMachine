#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import Builder
from ..src import SwitchCmd as Cmd

class SwitchAPI(object):
	def __init__(self):
		builder = Builder.Builder()
		self.__mMain = builder.getSwitchMain()

	def __del__(self):
		pass

	def threadEnd(self):
		print("--> SwitchAPI Stop.")
		self.__mMain.notifyCommand(Cmd.SWITCH_CMD_QUIT, None)