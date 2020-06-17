#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from . import DisplayCmd as Cmd

class DisplayCb(object):
	__mMain = None
	def __init__(self, mainObj):
		self.__mMain = mainObj

	def getTemperatureCb(self, value):
		self.__mMain.notifyCommand(Cmd.DISPLAY_CMD_GET_TEMP, [value])
