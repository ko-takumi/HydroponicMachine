#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
from Pump.api import PumpAPI
import LogPrint as LOG

class MainController(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.__mApiPump	= PumpAPI.PumpAPI()

	def run(self):
		LOG.INFO(__name__, "Thread start. [{}]".format(hex(id(self))))

		while True:
			time.sleep(1)

			#self.__mApiPump.threadEnd()