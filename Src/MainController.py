#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
from Pump.api import PumpAPI

class MainController(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.__mApiPump	= PumpAPI.PumpAPI()

	def run(self):
		print("MainController start. [", id(self), "]")

		while True:
			print("---> MainController")
			time.sleep(1)

			#self.__mApiPump.threadEnd()