#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
from Switch.api import SwitchAPI
from Display.api import DisplayAPI

class MenuController(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.__mApiSwitch	= SwitchAPI.SwitchAPI()
		self.__mApiDisplay	= DisplayAPI.DisplayAPI()

	def run(self):
		print("MenuController start. [", id(self), "]")

		while True:
			print("---> MenuController")
			time.sleep(1)

			#self.__mApiSwitch.threadEnd()
			#self.__mApiDisplay.threadEnd()