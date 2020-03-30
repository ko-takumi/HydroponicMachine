#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import LogPrint as LOG
import subprocess
import datetime

DEF_IMAGE_PATH = "/home/pi/django_app/Hydroponic/static/Hydroponic/images/"	# 暫定

class CameraIO(object):
	def __init__(self):
		pass

	def __del__(self):
		pass

	def execute(self):
		LOG.INFO(__name__, "Take Photo.")
		now = datetime.datetime.now()
		fileName = "{0}{1:%Y%m%d%H%S%f}.jpg".format(DEF_IMAGE_PATH, now)
		cmd = "/usr/bin/fswebcam -r 1920x1080 " + fileName
		print(cmd)
		subprocess.call(cmd.split())
		return True, fileName