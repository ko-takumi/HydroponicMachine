#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from . import SQLController
import LogPrint as LOG

class DataCollecterProcess(object):
	__mTempIdMax = 0
	__mHumidIdMax = 0

	def __init__(self):
		self.__mSqlCtr = SQLController.SQLController()
		result, fet = self.__mSqlCtr.execute("SELECT count(*) FROM temperatureLogs", ())
		if fet == None:
			self.__mTempIdMax = 0
		else:
			self.__mTempIdMax = fet[0]

		result, fet = self.__mSqlCtr.execute("SELECT count(*) FROM humidityLogs", ())
		if fet == None:
			self.__mHumidIdMax = 0
		else:
			self.__mHumidIdMax = fet[0]

	def setTemperature(self, value):
		LOG.INFO(__name__, "temperature[{}].".format(value))

		history = time.time()
		sql = "INSERT INTO temperatureLogs (id, history, temperature) VALUES (?, ?, ?)"
		history = '{}'.format(history)
		data = (self.__mTempIdMax + 1, history, value)
		result, dummy = self.__mSqlCtr.execute(sql, data)
		if result == False:
			LOG.ERROR(__name__, "__mSqlCtr.execute() error.")
			return False

		self.__mTempIdMax += 1
		return True

	def getTemperature(self):
		sql = "SELECT * FROM temperatureLogs WHERE id = {}".format(self.__mTempIdMax)
		data = ()
		result, item = self.__mSqlCtr.execute(sql, data)
		if (result == False) or (item == None):
			LOG.ERROR(__name__, "__mSqlCtr.execute() error.")
			return 0.0
			
		return item[2]

	def setHumidity(self, value):
		LOG.INFO(__name__, "humidity[{}].".format(value))

		history = time.time()
		sql = "INSERT INTO humidityLogs (id, history, humidity) VALUES (?, ?, ?)"
		history = '{}'.format(history)
		data = (self.__mHumidIdMax + 1, history, value)
		result, dummy = self.__mSqlCtr.execute(sql, data)
		if result == False:
			LOG.ERROR(__name__, "__mSqlCtr.execute() error.")
			return False

		self.__mHumidIdMax += 1
		return True

	def getHumidity(self):
		sql = "SELECT * FROM humidityLogs WHERE id = {}".format(self.__mHumidIdMax)
		data = ()
		result, item = self.__mSqlCtr.execute(sql, data)
		if (result == False) or (item == None):
			LOG.ERROR(__name__, "__mSqlCtr.execute() error.")
			return 0.0
			
		return item[2]
