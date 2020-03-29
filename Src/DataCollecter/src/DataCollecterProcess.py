#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import time
import datetime
from . import SQLController
import LogPrint as LOG

class DataCollecterProcess(object):
	__mTempIdMax = 0
	__mHumidIdMax = 0
	__mPictureIdMax = 0

	def __init__(self):
		self.__mSqlCtr = SQLController.SQLController()
		result, fet = self.__mSqlCtr.execute("SELECT count(*) FROM Hydroponic_temperatureLog", ())
		if fet == None:
			self.__mTempIdMax = 0
		else:
			self.__mTempIdMax = fet[0]

		result, fet = self.__mSqlCtr.execute("SELECT count(*) FROM Hydroponic_humidityLog", ())
		if fet == None:
			self.__mHumidIdMax = 0
		else:
			self.__mHumidIdMax = fet[0]

		result, fet = self.__mSqlCtr.execute("SELECT count(*) FROM Hydroponic_pictureLog", ())
		if fet == None:
			self.__mPictureIdMax = 0
		else:
			self.__mPictureIdMax = fet[0]

	def setTemperature(self, value):
		LOG.INFO(__name__, "temperature[{}].".format(value))

		history = datetime.datetime.now()
		sql = "INSERT INTO Hydroponic_temperatureLog (id, history, temperature) VALUES (?, ?, ?)"
		#history = '{}'.format(history)
		data = (self.__mTempIdMax + 1, history, value)
		result, dummy = self.__mSqlCtr.execute(sql, data)
		if result == False:
			LOG.ERROR(__name__, "__mSqlCtr.execute() error.")
			return False

		self.__mTempIdMax += 1
		return True

	def getTemperature(self):
		sql = "SELECT * FROM Hydroponic_temperatureLog WHERE id = {}".format(self.__mTempIdMax)
		data = ()
		result, item = self.__mSqlCtr.execute(sql, data)
		if (result == False) or (item == None):
			LOG.ERROR(__name__, "__mSqlCtr.execute() error.")
			return 0.0
			
		return item[2]

	def setHumidity(self, value):
		LOG.INFO(__name__, "humidity[{}].".format(value))

		history = datetime.datetime.now()
		sql = "INSERT INTO Hydroponic_humidityLog (id, history, humidity) VALUES (?, ?, ?)"
		#history = '{}'.format(history)
		data = (self.__mHumidIdMax + 1, history, value)
		result, dummy = self.__mSqlCtr.execute(sql, data)
		if result == False:
			LOG.ERROR(__name__, "__mSqlCtr.execute() error.")
			return False

		self.__mHumidIdMax += 1
		return True

	def getHumidity(self):
		sql = "SELECT * FROM Hydroponic_humidityLog WHERE id = {}".format(self.__mHumidIdMax)
		data = ()
		result, item = self.__mSqlCtr.execute(sql, data)
		if (result == False) or (item == None):
			LOG.ERROR(__name__, "__mSqlCtr.execute() error.")
			return 0.0
			
		return item[2]

	def setPicture(self, fileName):
		LOG.INFO(__name__, "fileName[{}].".format(fileName))

		history = datetime.datetime.now()
		sql = "INSERT INTO Hydroponic_pictureLog (id, history, fileName) VALUES (?, ?, ?)"
		data = (self.__mPictureIdMax + 1, history, fileName)
		result, dummy = self.__mSqlCtr.execute(sql, data)
		if result == False:
			LOG.ERROR(__name__, "__mSqlCtr.execute() error.")
			return False

		self.__mPictureIdMax += 1
		return True