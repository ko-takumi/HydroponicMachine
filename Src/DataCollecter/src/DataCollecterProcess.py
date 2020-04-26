#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import time
import datetime
from . import SQLController
import LogPrint as LOG

class DataCollecterProcess(object):
	__mColorIdMax = 0

	def __init__(self):
		self.__mSqlCtr = SQLController.SQLController()

		result, fet = self.__mSqlCtr.execute("SELECT count(*) FROM Hydroponic_colorLog", ())
		if fet == None:
			self.__mColorIdMax = 0
		else:
			self.__mColorIdMax = fet[0]

	def __getTempId(self):
		idIndex = 0
		result, fet = self.__mSqlCtr.execute("SELECT count(*) FROM Hydroponic_temperatureLog", ())
		if fet == None:
			idIndex = 0
		else:
			idIndex = fet[0]
		return idIndex

	def __getHumidId(self):
		idIndex = 0
		result, fet = self.__mSqlCtr.execute("SELECT count(*) FROM Hydroponic_humidityLog", ())
		if fet == None:
			idIndex = 0
		else:
			idIndex = fet[0]
		return idIndex

	def __getPictureId(self):
		idIndex = 0
		result, fet = self.__mSqlCtr.execute("SELECT count(*) FROM Hydroponic_pictureLog", ())
		if fet == None:
			idIndex = 0
		else:
			idIndex = fet[0]
		return idIndex

	def __getColorIdToAdd(self):
		idIndex = 0
		result, fet = self.__mSqlCtr.execute("SELECT count(*) FROM Hydroponic_colorLog", ())
		if fet == None:
			idIndex = 0
		else:
			idIndex = fet[0]
		return idIndex

	def setTemperature(self, value):
		LOG.INFO(__name__, "temperature[{}].".format(value))
		addId = self.__getTempId()
		addId += 1

		history = datetime.datetime.now()
		sql = "INSERT INTO Hydroponic_temperatureLog (id, history, temperature) VALUES (?, ?, ?)"
		data = (addId, history, value)
		result, dummy = self.__mSqlCtr.execute(sql, data)
		if result == False:
			LOG.ERROR(__name__, "__mSqlCtr.execute() error.")
			return False

		return True

	def getTemperature(self):
		idIndex = self.__getTempId()

		sql = "SELECT * FROM Hydroponic_temperatureLog WHERE id = {}".format(idIndex)
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
		addId = self.__getHumidId()
		addId += 1

		history = datetime.datetime.now()
		sql = "INSERT INTO Hydroponic_humidityLog (id, history, humidity) VALUES (?, ?, ?)"
		#history = '{}'.format(history)
		data = (addId, history, value)
		result, dummy = self.__mSqlCtr.execute(sql, data)
		if result == False:
			LOG.ERROR(__name__, "__mSqlCtr.execute() error.")
			return False

		return True

	def getHumidity(self):
		addMax = self.__getHumidId()

		sql = "SELECT * FROM Hydroponic_humidityLog WHERE id = {}".format(addMax)
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
		addId = self.__getPictureId()
		addId += 1

		history = datetime.datetime.now()
		sql = "INSERT INTO Hydroponic_pictureLog (id, history, fileName) VALUES (?, ?, ?)"
		data = (addId, history, fileName)
		result, dummy = self.__mSqlCtr.execute(sql, data)
		if result == False:
			LOG.ERROR(__name__, "__mSqlCtr.execute() error.")
			return False

		return True

	def setColor(self, r, g, b):
		LOG.INFO(__name__, "r[{}] g[{}] b[{}].".format(r, g, b))
		addId = self.__getColorIdToAdd()
		addId += 1

		history = datetime.datetime.now()
		sql = "INSERT INTO Hydroponic_colorLog (id, history, red, green, blue) VALUES (?, ?, ?, ?, ?)"
		r = '{:.5g}'.format(r)
		g = '{:.5g}'.format(g)
		b = '{:.5g}'.format(b)
		data = (addId, history, r, g, b)
		result, dummy = self.__mSqlCtr.execute(sql, data)
		if result == False:
			LOG.ERROR(__name__, "__mSqlCtr.execute() error.")
			return False

		return True
	
	def updateGrowth(self, r, g, b):
		sql = "UPDATE Hydroponic_growth SET value={:.5g} WHERE id=1;".format(g)
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