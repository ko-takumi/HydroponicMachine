#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import Builder
from ..src import DataCollecterCmd as Cmd
import LogPrint as LOG

class DataCollecterAPI(object):
	def __init__(self):
		builder = Builder.Builder()
		self.__mMain = builder.getDataCollecterMain()

	def __del__(self):
		pass

	# 同期API
	def getMachineValue(self):
		value = self.__mMain.getParameter()
		return value

	def setTemperature(self, value, isSave):
		LOG.INFO(__name__, "DATA_CMD_SET_TEMP.")
		self.__mMain.notifyCommand(Cmd.DATA_CMD_SET_TEMP, [value, isSave])

	def getTemperature(self, cb):
		LOG.INFO(__name__, "DATA_CMD_GET_TEMP.")
		self.__mMain.notifyCommand(Cmd.DATA_CMD_GET_TEMP, [cb])

	def setHumidity(self, value, isSave):
		LOG.INFO(__name__, "DATA_CMD_SET_HUMID.")
		self.__mMain.notifyCommand(Cmd.DATA_CMD_SET_HUMID, [value, isSave])

	def getHumidity(self, cb):
		LOG.INFO(__name__, "DATA_CMD_GET_HUMID.")
		self.__mMain.notifyCommand(Cmd.DATA_CMD_GET_HUMID, [cb])

	def setPicture(self, fileName):
		LOG.INFO(__name__, "DATA_CMD_SET_PICTURE.")
		self.__mMain.notifyCommand(Cmd.DATA_CMD_SET_PICTURE, [fileName])

	def setColor(self, r, g, b):
		LOG.INFO(__name__, "DATA_CMD_SET_COLOR.")
		self.__mMain.notifyCommand(Cmd.DATA_CMD_SET_COLOR, [r, g, b])

	def registerChangeTemprature(self, cb):
		LOG.INFO(__name__, "DATA_CMD_REG_CHANGETEMP.")
		self.__mMain.notifyCommand(Cmd.DATA_CMD_REG_CHANGETEMP, [cb])

	def registerChangeHumidity(self, cb):
		LOG.INFO(__name__, "DATA_CMD_REG_CHANGEHUMID.")
		self.__mMain.notifyCommand(Cmd.DATA_CMD_REG_CHANGEHUMID, [cb])

	def threadEnd(self):
		LOG.INFO(__name__, "DISPLAY_CMD_QUIT.")
		self.__mMain.notifyCommand(Cmd.DISPLAY_CMD_QUIT, None)
