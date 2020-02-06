#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime

def INFO(funcName, logStr):
	_DATA_ = datetime.datetime.now()
	print(_DATA_, funcName, ":[INFO]", logStr)

def ERROR(funcName, logStr):
	_DATA_ = datetime.datetime.now()
	print(_DATA_, funcName, ":[ERROR]:",logStr)

def WARRING(funcName, logStr):
	_DATA_ = datetime.datetime.now()
	print(_DATA_, funcName, ":[WARRING]:", logStr)
