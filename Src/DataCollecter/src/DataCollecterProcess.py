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
	__mColorIdMax = 0

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

		result, fet = self.__mSqlCtr.execute("SELECT count(*) FROM Hydroponic_colorLog", ())
		if fet == None:
			self.__mColorIdMax = 0
		else:
			self.__mColorIdMax = fet[0]

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

	# 現在温度を更新する
	# setTemperatureとは目的が異なる
	def updateTemperature(self, value):
		sql = "UPDATE Hydroponic_temperature SET value ={} WHERE id=1;".format(value)
		data = ''
		result, dummy = self.__mSqlCtr.execute(sql, data)
		if result == False:
			LOG.ERROR(__name__, "__mSqlCtr.execute() error.")
			return False
		
		return True

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

	# 現在温度を更新する
	# setHumidityとは目的が異なる
	def updateHumidity(self, value):
		sql = "UPDATE Hydroponic_humidity SET value={} WHERE id=1;".format(value)
		data = ''
		result, dummy = self.__mSqlCtr.execute(sql, data)
		if result == False:
			LOG.ERROR(__name__, "__mSqlCtr.execute() error.")
			return False
		
		return True

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

	def setColor(self, r, g, b):
		LOG.INFO(__name__, "r[{}] g[{}] b[{}].".format(r, g, b))

		history = datetime.datetime.now()
		sql = "INSERT INTO Hydroponic_colorLog (id, history, red, green, blue) VALUES (?, ?, ?, ?, ?)"
		r = '{:.2g}'.format(r)
		g = '{:.2g}'.format(g)
		b = '{:.2g}'.format(b)
		data = (self.__mColorIdMax + 1, history, r, g, b)
		result, dummy = self.__mSqlCtr.execute(sql, data)
		if result == False:
			LOG.ERROR(__name__, "__mSqlCtr.execute() error.")
			return False

		self.__mPictureIdMax += 1
		return True
	
	def updateGrowth(self, r, g, b):
		sql = "UPDATE Hydroponic_growth SET value={:.2g} WHERE id=1;".format(g)
		data = ''
		result, dummy = self.__mSqlCtr.execute(sql, data)
		if result == False:
			LOG.ERROR(__name__, "__mSqlCtr.execute() error.")
			return False
		
		return True

	def getSettingData(self):
		param = \
		{
			'photoTime': 0,
			'plantManagemntTime': 0,
			'notifyTime': 0,
			'temperatureSaveTime': 0,
			'warteringTime': 0.0,
			'lineToken': "",
		}

		# photoTimeを取得
		sql = "SELECT * FROM Hydroponic_timesetting WHERE name=\"photoTime\""
		data = ()
		result, item = self.__mSqlCtr.execute(sql, data)
		if (result == False) or (item == None):
			LOG.ERROR(__name__, "__mSqlCtr.execute() error.")
			LOG.ERROR(__name__, "photoTime default value[3600]")
			param['photoTime'] = 3600
		param['photoTime'] = int(item[2])

		# plantManagemntTimeを取得
		sql = "SELECT * FROM Hydroponic_timesetting WHERE name=\"plantManagemntTime\""
		data = ()
		result, item = self.__mSqlCtr.execute(sql, data)
		if (result == False) or (item == None):
			LOG.ERROR(__name__, "__mSqlCtr.execute() error.")
			LOG.ERROR(__name__, "plantManagemntTime default value[1800]")
			param['plantManagemntTime'] = 1800
		param['plantManagemntTime'] = int(item[2])

		# notifyTimeを取得
		sql = "SELECT * FROM Hydroponic_timesetting WHERE name=\"notifyTime\""
		data = ()
		result, item = self.__mSqlCtr.execute(sql, data)
		if (result == False) or (item == None):
			LOG.ERROR(__name__, "__mSqlCtr.execute() error.")
			LOG.ERROR(__name__, "notifyTime default value[10800]")
			param['notifyTime'] = 10800
		param['notifyTime'] = int(item[2])

		# temperatureSaveTimeを取得
		sql = "SELECT * FROM Hydroponic_timesetting WHERE name=\"temperatureSaveTime\""
		data = ()
		result, item = self.__mSqlCtr.execute(sql, data)
		if (result == False) or (item == None):
			LOG.ERROR(__name__, "__mSqlCtr.execute() error.")
			LOG.ERROR(__name__, "temperatureSaveTime default value[1800]")
			param['temperatureSaveTime'] = 1800
		param['temperatureSaveTime'] = int(item[2])

		# warteringTimeを取得
		sql = "SELECT * FROM Hydroponic_watersetting WHERE name=\"warteringTime\""
		data = ()
		result, item = self.__mSqlCtr.execute(sql, data)
		if (result == False) or (item == None):
			LOG.ERROR(__name__, "__mSqlCtr.execute() error.")
			LOG.ERROR(__name__, "warteringTime default value[1800]")
			param['warteringTime'] = 1.0
		param['warteringTime'] = float(item[1])

		# lineTokenを取得
		sql = "SELECT * FROM Hydroponic_linesetting WHERE name=\"lineToken\""
		data = ()
		result, item = self.__mSqlCtr.execute(sql, data)
		if (result == False) or (item == None):
			LOG.ERROR(__name__, "__mSqlCtr.execute() error.")
			LOG.ERROR(__name__, "lineToken default value[none]")
			param['lineToken'] = "none"
		param['lineToken'] = str(item[2])		
		
		return param