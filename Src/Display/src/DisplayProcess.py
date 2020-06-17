#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import LogPrint as LOG
from . import DisplayIO

BUS_NUMBER = 1
ADDR = 0x27
REGISTER_SETTING = 0x00
REGISTER_DISPLAY = 0x80

MODEID_TEMP_IP = 0
MODEID_MAX = 1

class DisplayProcess(object):
	__mModeID = MODEID_TEMP_IP	# TODO: 現在固定
	__mTemp = 0.0
	__mHumid = 0.0
	__mIPAddr = "0.0.0.0"
	__mIsDisp = False

	def __init__(self, dataObj):
		self.__mDataApi = dataObj
		self.__mDisplay = DisplayIO.DisplayIO(BUS_NUMBER, ADDR, REGISTER_SETTING, REGISTER_DISPLAY)
		self.__mModeID = MODEID_TEMP_IP

	def execute(self):
		if self.__mIsDisp == False:
			return

		# modeによって出力を変化させる
		if self.__mModeID == MODEID_TEMP_IP:
			str1st = "{}'C({}%)".format(self.__mTemp, self.__mHumid)
			self.__mDisplay.writeStr1st(str1st)
			self.__mDisplay.writeStr2nd(self.__mIPAddr)

		self.__mIsDisp = False

	def notifyTemperature(self, value):
		LOG.INFO(__name__, "TEMP[{}]".format(value))
		self.__mIsDisp = True
		self.__mTemp = value

	def notifyHumidity(self, value):
		LOG.INFO(__name__, "HUMID[{}]".format(value))
		self.__mIsDisp = True
		self.__mHumid = value

	def notifyIPAddress(self, ip):
		LOG.INFO(__name__, "IP-ADDRESS[{}]".format(ip))
		self.__mIsDisp = True
		self.__mIPAddr = ip

	def notifyChangeMode(self):
		# TODO
		# MODEID_TEMP_IP → MODEID_XXXXX → MODEID_TEMP_IP　→ MODEID_XXXXX
		# とやりたい
		oldMode = self.__mModeID
		self.__mModeID += 1
		if self.__mModeID >= MODEID_MAX:
			self.__mModeID = MODEID_TEMP_IP

		LOG.INFO(__name__, "Mode[{} >> {}]".format(oldMode, self.__mModeID))
		