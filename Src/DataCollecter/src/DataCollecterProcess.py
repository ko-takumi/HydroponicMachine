#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from . import SQLController
import LogPrint as LOG

class DataCollecterProcess(object):
	__mWateringIdMax = 0
	def __init__(self):
		self.__mSqlCtr = SQLController.SQLController()
		result, fet = self.__mSqlCtr.execute("SELECT count(*) FROM temperatureLogs", ())
		if fet == None:
			self.__mWateringIdMax = 0
		else:
			self.__mWateringIdMax = fet[0]

	def setTemperature(self, value):
		LOG.INFO(__name__, "temperature[{}].".format(value))

		history = time.time()
		sql = "INSERT INTO temperatureLogs (id, history, temperature) VALUES (?, ?, ?)"
		history = '{}'.format(history)
		data = (self.__mWateringIdMax + 1, history, value)
		result, dummy = self.__mSqlCtr.execute(sql, data)
		if result == False:
			LOG.ERROR(__name__, "__mSqlCtr.execute() error.")
			return False

		self.__mWateringIdMax += 1
		return True

	def getTemperature(self):
		sql = "SELECT * FROM temperatureLogs WHERE id = {}".format(self.__mWateringIdMax)
		data = ()
		result, item = self.__mSqlCtr.execute(sql, data)
		if (result == False) or (item == None):
			LOG.ERROR(__name__, "__mSqlCtr.execute() error.")
			return 0.0
			
		return item[2]
