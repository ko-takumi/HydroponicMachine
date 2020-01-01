#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import LogPrint as LOG
from Switch.api import SwitchAPI
from Display.api import DisplayAPI

class MenuControllerProcess(object):
	def __init__(self):
		self.__mApiSwitch	= SwitchAPI.SwitchAPI()
		self.__mApiDisplay	= DisplayAPI.DisplayAPI()

	def execute(self):
		pass

	def updataTemperature(self, value):
		LOG.INFO(__name__, "UPDATA[{}].".format(value))
		self.__mApiDisplay.notifyTemperature([value])