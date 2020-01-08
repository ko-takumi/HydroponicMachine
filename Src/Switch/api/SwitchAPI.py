#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import Builder
from ..src import SwitchCmd as Cmd
import LogPrint as LOG

class SwitchAPI(object):
	def __init__(self):
		builder = Builder.Builder()
		self.__mMain = builder.getSwitchMain()

	def __del__(self):
		pass

	def registerPushSw(self, cb):
		LOG.INFO(__name__, "SWITCH_CMD_REG_PUSHSW.")
		self.__mMain.notifyCommand(Cmd.SWITCH_CMD_REG_PUSHSW, [cb])

	def threadEnd(self):
		print("--> SwitchAPI Stop.")
		self.__mMain.notifyCommand(Cmd.SWITCH_CMD_QUIT, None)