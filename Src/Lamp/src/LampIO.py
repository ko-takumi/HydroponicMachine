#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import LogPrint as LOG

class LampIO(object):
	def __init__(self):
		pass

	def __del__(self):
		pass

	def on(self):
		LOG.INFO(__name__, "ON.")
		# LED-ON

	def off(self, offTime):
		LOG.INFO(__name__, "OFF---->.")
		time.sleep(offTime)
		# LED-OFF
		LOG.INFO(__name__, "<----OFF.")