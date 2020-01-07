#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import LogPrint as LOG
from Switch.api import SwitchAPI
from Display.api import DisplayAPI
import ipget

class MenuControllerProcess(object):
	__mIPAdder = ""
	def __init__(self):
		self.__mApiSwitch	= SwitchAPI.SwitchAPI()
		self.__mApiDisplay	= DisplayAPI.DisplayAPI()

		# ipアドレス取得
		self.__mIPAdder = self.__getIPAddress()
		self.__mApiDisplay.notifyIPAddress([self.__mIPAdder])

	def execute(self):
		# ipアドレスの変更確認
		ip = self.__getIPAddress()
		if self.__mIPAdder != ip:
			self.__mIPAdder = ip
			self.__mApiDisplay.notifyIPAddress([self.__mIPAdder])

	def updataTemperature(self, value):
		LOG.INFO(__name__, "UPDATA-TEMP[{}].".format(value))
		self.__mApiDisplay.notifyTemperature([value])

	def __getIPAddress(self):
		try:
			instance = ipget.ipget()
			ip = instance.ipaddr("eth0")
		except:
			# 切替り中のタイミングによってはエラーとなる
			ip = self.__mIPAdder
		return ip
	