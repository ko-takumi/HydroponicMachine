#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import LogPrint as LOG
import subprocess
import datetime

class CameraIO(object):
	def __init__(self):
		pass

	def __del__(self):
		pass

	def execute(self):
		LOG.INFO(__name__, "Take Photo.")
		now = datetime.datetime.now()
		cmd = "/usr/bin/fswebcam -r 1920x1080 ../{0:%Y%m%d%H%S%f}.jpg".format(now)
		subprocess.call(cmd.split())
		return