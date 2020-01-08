#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import smbus
import time
import LogPrint as LOG

class DisplayIO(object):
	def __init__(self, busNumber, addr, registerSetting, registerDisplay):
		self.__mBusNumber = busNumber
		self.__mAddr = addr
		self.__mRegSetting = registerSetting
		self.__mRegDisplay = registerDisplay
		self.__mBus = smbus.SMBus(self.__mBusNumber)
		try:
			self.__mBus.write_byte_data(self.__mAddr, self.__mRegSetting, 0x01)
			time.sleep(0.02)
			self.__mBus.write_byte_data(self.__mAddr, self.__mRegSetting, 0x38)
			time.sleep(0.02)
			self.__mBus.write_byte_data(self.__mAddr, self.__mRegSetting, 0x0f)
			time.sleep(0.02)
			self.__mBus.write_byte_data(self.__mAddr, self.__mRegSetting, 0x06)
			time.sleep(0.02)
		except:
			LOG.ERROR(__name__, "Display init error.")

	def __del__(self):
		pass

	def writeStr1st(self, dispStr):
		LOG.INFO(__name__, "1stDisp[{}]".format(dispStr))
		try:
			self.__mBus.write_byte_data(self.__mAddr, self.__mRegSetting, 0x80)
			self.__writeStr(dispStr)
		except:
			LOG.ERROR(__name__, "write_byte_data error.")

	def writeStr2nd(self, dispStr):
		LOG.INFO(__name__, "2ndDisp[{}]".format(dispStr))
		try:
			self.__mBus.write_byte_data(self.__mAddr, self.__mRegSetting, 0xc0)
			self.__writeStr(dispStr)
		except:
			LOG.ERROR(__name__, "write_byte_data error.")

	def __writeStr(self, dispStr):
		for c in list(dispStr):
			self.__mBus.write_byte_data(self.__mAddr, self.__mRegDisplay, ord(c))
			time.sleep(0.1)
