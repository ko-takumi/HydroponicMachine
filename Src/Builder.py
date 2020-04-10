#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Temperature.src import TemperatureMain
from DataCollecter.src import DataCollecterMain
from DataCollecter.api import DataCollecterAPI
from Switch.src import SwitchMain
from Display.src import DisplayMain, DisplayCb
from Pump.src import PumpMain
from Camera.src import CameraMain
from Lamp.src import LampMain

from MainController import MainController
from MenuController import MenuController

class Builder(object):
	__mInstance				= None
	__mTemperatureThread	= None
	__mDataCollecterThread	= None
	__mSwitchThread			= None
	__mDisplayThread		= None
	__mPumpThread			= None
	__mCameraThread			= None
	__mLampThread			= None
	__mMainThread			= None
	__mMenuThread			= None

	__mDataCollecterAPI		= None

	__mDisplayCb			= None

	def __new__(self):
		if self.__mInstance == None:
			self.__mInstance = super(Builder, self).__new__(self)
			self.__mInstance.__create()
		return self.__mInstance

	def __create(self):
		# 順番性あり
		# DataCollectoreTread -> DataCollecterAPIとすること
		self.__mDataCollecterThread	= DataCollecterMain.DataCollecterMain()
		self.__mDataCollecterAPI	= DataCollecterAPI.DataCollecterAPI()
		param = self.__mDataCollecterAPI.getMachineValue()

		self.__mTemperatureThread	= TemperatureMain.TemperatureMain(self.__mDataCollecterAPI, param['temperatureSaveTime'])
		self.__mSwitchThread		= SwitchMain.SwitchMain()
		self.__mDisplayThread		= DisplayMain.DisplayMain(self.__mDataCollecterAPI)
		self.__mPumpThread			= PumpMain.PumpMain()
		self.__mCameraThread		= CameraMain.CameraMain(self.__mDataCollecterAPI)
		self.__mLampThread			= LampMain.LampMain()

		# CBクラス作成
		self.__mDisplayCb	= DisplayCb.DisplayCb(self.__mDisplayThread)

		# main, menu作成
		self.__mMainThread = MainController.MainController(param['photoTime'], param['plantManagemntTime'], param['notifyTime'], param['warteringTime'], param['lineToken'])
		self.__mMenuThread = MenuController.MenuController()

	def getThreads(self):
		threadList =	[self.__mTemperatureThread, self.__mDataCollecterThread, self.__mSwitchThread, 
						 self.__mDisplayThread, self.__mPumpThread, self.__mCameraThread, self.__mLampThread, self.__mMainThread, self.__mMenuThread]
		if None in threadList:
			print("[ERROR]thread is None.")
			return None
		return threadList

	def getSwitchMain(self):
		return self.__mSwitchThread

	def getDisplayMain(self):
		return self.__mDisplayThread

	def getDisplayCb(self):
		return self.__mDisplayCb

	def getPumpMain(self):
		return self.__mPumpThread

	def getDataCollecterMain(self):
		return self.__mDataCollecterThread

	def getDataCollecterAPI(self):
		return self.__mDataCollecterAPI

	def getCameraMain(self):
		return self.__mCameraThread

	def getLampMain(self):
		return self.__mLampThread

Builder()