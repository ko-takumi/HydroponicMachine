#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import Builder
from ..src import DisplayCmd as Cmd

class DisplayAPI(object):
	def __init__(self):
		builder = Builder.Builder()
		self.__mMain = builder.getDisplayMain()

	def __del__(self):
		pass

	def notifyTemperature(self, value):
		self.__mMain.notifyCommand(Cmd.DISPLAY_CMD_NOTIFY_TEMP, value)

	def notifyIPAddress(self, ip):
		self.__mMain.notifyCommand(Cmd.DISPLAY_CMD_NOTIFY_IPADDRESS, ip)

	def threadEnd(self):
		self.__mMain.notifyCommand(Cmd.DISPLAY_CMD_QUIT, None)
