#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import LogPrint as LOG
import cv2
import os

class ImageRecognition(object):
	def __init__(self):
		pass

	def __del__(self):
		pass

	def execute(self, fileName):
		# 対象画像読み込み
		img = cv2.imread(fileName, cv2.IMREAD_COLOR)

		# RGB平均値を出力
		# flattenで一次元化しmeanで平均を取得 
		b = img.T[0].flatten().mean()
		g = img.T[1].flatten().mean()
		r = img.T[2].flatten().mean()

		# RGB平均値を取得
		LOG.INFO(__name__, "R: %.2f" % (r))
		LOG.INFO(__name__, "G: %.2f" % (g))
		LOG.INFO(__name__, "B: %.2f" % (b))
		
		return r, g, b
		