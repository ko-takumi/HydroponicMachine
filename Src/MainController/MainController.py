#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
import Builder
from Pump.api import PumpAPI
from Camera.api import CameraAPI
from Lamp.api import LampAPI
import LogPrint as LOG
from Notify.src import LineNotify

DEF_LAMP_OFF_TIME = 3.0
DEF_WARTERING_TIME = 1.0

class MainController(threading.Thread, LineNotify.LineNotify):
	__mSubThreadFlag = True

	# 時間設定
	# TODO: 外部から設定できるようにしたい
	__mPhotoTime = 60 * 60			# 1h
	__mPlantManagemntTime = 30 * 60 # 0.5h
	__mNotifyTime = (3 * 60) * 60	# 3.0h

	# スレッド
	__mPhotoThread = None
	__mPompThread = None
	__mNotifyThread = None

	# 実施有無
	__mIsPhotoStart = False
	__mIsPlantManagemnt = False

	# 通知内容
	__mTempValue = 0.0
	__mHumidValue = 0.0
	__mImageFile = ""

	def __init__(self):
		threading.Thread.__init__(self)
		LineNotify.LineNotify.__init__(self)
		self.__mApiPump		= PumpAPI.PumpAPI()
		self.__mApiCamera	= CameraAPI.CameraAPI()
		self.__mApiLamp		= LampAPI.LampAPI()

		builder = Builder.Builder()
		self.__mData = builder.getDataCollecterAPI()

		self.__mData.getTemperature(self.getTemperatureCB)
		self.__mData.getHumidity(self.getHumidityCB)
		self.sentMessage("INFO", "起動した")

		# photoスレッド生成
		self.__mPhotoThread = threading.Thread(target=self.__executePhotoThread)
		self.__mPhotoThread.start()

		# pompスレッド生成
		self.__mPompThread = threading.Thread(target=self.__executePlantManagerThread)
		self.__mPompThread.start()

		# 通知スレッド生成
		self.__mNotifyThread = threading.Thread(target=self.__executeNotifyThread)
		self.__mNotifyThread.start()

	def __executePhotoThread(self):
		while self.__mSubThreadFlag:
			self.__mIsPhotoStart = True
			time.sleep(self.__mPhotoTime)

	def __executePlantManagerThread(self):
		while self.__mSubThreadFlag:
			self.__mIsPlantManagemnt = True
			time.sleep(self.__mPlantManagemntTime)

	def __executeNotifyThread(self):
		while self.__mSubThreadFlag:
			self.__mIsNotify = True
			time.sleep(self.__mNotifyTime)

	def run(self):
		LOG.INFO(__name__, "Thread start. [{}]".format(hex(id(self))))

		while True:
			# 写真撮影実施
			if self.__mIsPhotoStart == True:
				self.__mIsPhotoStart = False
				self.__takePhoto()
			
			# 水やり実施
			if self.__mIsPlantManagemnt == True:
				self.__mIsPlantManagemnt = False
				self.__mApiPump.execute(DEF_WARTERING_TIME)
				self.__mData.getTemperature(self.getTemperatureCB)
				self.__mData.getHumidity(self.getHumidityCB)

			# Line通知実施
			if self.__mIsNotify == True:
				self.__mIsNotify = False
				self.__NotifyInfo()

			time.sleep(1)
		return

	def __takePhoto(self):
		self.__mApiLamp.on()
		time.sleep(0.1)
		self.__mApiCamera.execute(self.getImageCB)
		self.__mApiLamp.off(DEF_LAMP_OFF_TIME)

	def __NotifyInfo(self):
		msg = "{}度 {}%".format(self.__mTempValue, self.__mHumidValue)
		self.sentMessage("温度/湿度", msg)
		if self.__mImageFile != "":
			self.sendImage(self.__mImageFile)

	def getTemperatureCB(self, value):
		self.__mTempValue = value

	def getHumidityCB(self, value):
		self.__mHumidValue = value

	def getImageCB(self, fileName):
		self.__mImageFile = fileName
