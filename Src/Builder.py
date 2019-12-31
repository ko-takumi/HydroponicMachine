#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Temperature.src import TemperatureMain
from DataCollecter.src import DataCollecterMain
from DataCollecter.api import DataCollecterAPI
from Switch.src import SwitchMain
from Display.src import DisplayMain
from Pump.src import PumpMain

class Builder(object):
	__mInstance				= None
	__mTemperatureThread	= None
	__mDataCollecterThread	= None
	__mSwitchThread			= None
	__mDisplayThread		= None
	__mPumpThread			= None

	__mDataCollecterAPI		= None

	def __new__(self):
		if self.__mInstance == None:
			self.__mInstance = super(Builder, self).__new__(self)
			self.__mInstance.__create()
		return self.__mInstance

	def __create(self):
		self.__mDataCollecterThread	= DataCollecterMain.DataCollecterMain()
		self.__mDataCollecterAPI	= DataCollecterAPI.DataCollecterAPI()

		self.__mTemperatureThread	= TemperatureMain.TemperatureMain(self.__mDataCollecterAPI)
		self.__mSwitchThread		= SwitchMain.SwitchMain()
		self.__mDisplayThread		= DisplayMain.DisplayMain()
		self.__mPumpThread			= PumpMain.PumpMain()

	def getThreads(self):
		threadList = [self.__mTemperatureThread, self.__mDataCollecterThread, self.__mSwitchThread, self.__mDisplayThread, self.__mPumpThread]
		if None in threadList:
			print("[ERROR]thread is None.")
			return None
		return threadList

	def getSwitchMain(self):
		return self.__mSwitchThread

	def getDisplayMain(self):
		return self.__mDisplayThread

	def getPumpMain(self):
		return self.__mPumpThread

	def getDataCollecterMain(self):
		return self.__mDataCollecterThread

Builder()