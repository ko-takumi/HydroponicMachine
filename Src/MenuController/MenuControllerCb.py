#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from . import MenuControllerCmd as Cmd

class MenuControllerCb(object):
	__mMain = None
	def __init__(self, mainObj):
		self.__mMain = mainObj

	def getTemperatureCb(self, value):
		self.__mMain.notifyCommand(Cmd.MENU_CMD_GET_TEMP, [value])

	def getHumidityCb(self, value):
		self.__mMain.notifyCommand(Cmd.MENU_CMD_GET_HUMID, [value])

	def notifyPushSWCb(self):
		self.__mMain.notifyCommand(Cmd.MENU_CMD_PUSH_SW, [None])
