#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import LogPrint as LOG

class Semaphore(object):
	__mIsLock = False
	__mClientName = ""

	def __init__(self, clientName):
		self.__mClientName = clientName

	def __del__(self):
		pass

	def lock(self):
		while(self.__mIsLock != False):
			LOG.INFO(__name__, "[{}] wait...".format(self.__mClientName))
			time.sleep(0.01)

		LOG.INFO(__name__, "lock.[{}]".format(self.__mClientName))
		self.__mIsLock = True

	def unlock(self):
		LOG.INFO(__name__, "unlock.[{}]".format(self.__mClientName))
		self.__mIsLock = False