#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Builder(object):
	__mInstance = None

	def __new__(self):
		if self.__mInstance == None:
			self.__mInstance = super(Builder, self).__new__(self)
		return self.__mInstance

Builder()