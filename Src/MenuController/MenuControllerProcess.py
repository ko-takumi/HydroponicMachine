#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import LogPrint as LOG
from Display.api import DisplayAPI
import ipget

class MenuControllerProcess(object):
	__mIPAdder = ""
	def __init__(self):
		self.__mApiDisplay	= DisplayAPI.DisplayAPI()	# TODO: Mainに移管したい

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

	def updataHumidity(self, value):
		LOG.INFO(__name__, "UPDATA-HUMID[{}].".format(value))
		self.__mApiDisplay.notifyHumidity([value])

	def notifyPushSW(self):
		LOG.INFO(__name__, "PUSH SW.")
		self.__mApiDisplay.notifyChangeMode()

	def __getIPAddress(self):
		try:
			instance = ipget.ipget()
			ip = instance.ipaddr("eth0")
		except:
			# 切替り中のタイミングによってはエラーとなる
			ip = self.__mIPAdder
		return ip
	