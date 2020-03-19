#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
# import os

# 実際にはraspberryPiのフォルダを指定する
# DEF_DBNAME = '/var/lib/sqlite3/log.db'
DEF_DBNAME = '/home/pi/django_app/db.sqlite3'

class SQLController(object):
	def __init__(self):
		self.__prepareDb()

	def __prepareDb(self):
		pass
		#isExistsFile = os.path.exists(DEF_DBNAME)
		#if isExistsFile == False:
		#	self.mDb = sqlite3.connect(DEF_DBNAME)
		#	conect = self.mDb.cursor()
		#	conect.execute('''CREATE TABLE wateringLogs(id INTEGER, history TEXT)''')
		#	conect.execute('''CREATE TABLE temperatureLogs(id INTEGER, history TEXT, temperature REAL)''')
		#	conect.execute('''CREATE TABLE humidityLogs(id INTEGER, history TEXT, humidity REAL)''')
		#	self.mDb.commit()
		#	conect.close()

	def execute(self, sql, data):
		try:
			self.mDb = sqlite3.connect(DEF_DBNAME)
			conect = self.mDb.cursor()
			conect.execute(sql, data)
			self.mDb.commit()
			fet = conect.fetchone()
			conect.close()
		except:
			print("[Error] sql wite error.[", sql, "]")
			return False, None
		
		return True, fet