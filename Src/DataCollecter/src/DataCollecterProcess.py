#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from . import SQLController

class DataCollecterProcess(object):
	__mWateringIdMax = 0
	def __init__(self):
		self.__mSqlCtr = SQLController.SQLController()

	def setTemperature(self, value):
		print("--> setTemperature[", value, "]")

		history = time.time()
		sql = "INSERT INTO temperatureLogs (id, history, temperature) VALUES (?, ?, ?)"
		history = '{}'.format(history)
		data = (self.__mWateringIdMax + 1, history, value)
		result, dummy = self.__mSqlCtr.execute(sql, data)
		if result == False:
			print("[Error] __execSQL error.")
			return False

		self.__mWateringIdMax += 1
		return True

	def getTemperature(self):
		sql = "SELECT * FROM temperatureLogs WHERE id = {}".format(self.__mWateringIdMax)
		data = ()
		result, item = self.__mSqlCtr.execute(sql, data)
		if result == False:
			print("Error. getTemperature()")
			return 0.0
			
		return item[2]
