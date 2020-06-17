#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import LogPrint as LOG
SUCCESS_NUM = "<Response [200]>"
DEF_API = 'https://notify-api.line.me/api/notify'

class LineNotify(object):
	__mToken = ""
	__mApi = ""

	def __init__(self, token):
		self.__mToken = token
		self.__mApi = DEF_API
		LOG.INFO(__name__, "token[{}]".format(self.__mToken))

	def sentMessage(self, subject, text):
		LOG.INFO(__name__, "send[{}]".format(text))

		message = subject + " : " + text
		payload = {'message': message}
		headers = {'Authorization': 'Bearer ' + self.__mToken}

		try:
			result = str(requests.post(self.__mApi, data=payload, headers=headers))
			if result == SUCCESS_NUM:
				LOG.ERROR(__name__, "success[{}]".format(result))
			else:
				LOG.ERROR(__name__, "error[{}]".format(result))
		except:
			LOG.ERROR(__name__, "except[{}]".format(result))

	def sendImage(self, img):
		LOG.INFO(__name__, "send[{}]".format(img))
		
		message = "image[{}]".format(img)
		payload = {'message': message}

		f = open(img, "rb")
		files = {"imageFile": f}
		headers = {'Authorization': 'Bearer ' + self.__mToken}

		try:
			result = str(requests.post(self.__mApi, data=payload, headers=headers, files=files))
			if result == SUCCESS_NUM:
				LOG.ERROR(__name__, "success[{}]".format(result))
			else:
				LOG.ERROR(__name__, "error[{}]".format(result))
		except:
			LOG.ERROR(__name__, "except.")
