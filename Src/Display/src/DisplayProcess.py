#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import LogPrint as LOG

class DisplayProcess(object):
	def __init__(self, dataObj):
		self.__mDataApi = dataObj

	def execute(self):
		pass

	def notifyTemperature(self, value):
		LOG.INFO(__name__, "TEMP[{}]".format(value))
