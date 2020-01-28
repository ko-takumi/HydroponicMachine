#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import smbus
import time
import LogPrint as LOG

LCD_LINE_1		= 0x80
LCD_LINE_2		= 0xC0
LCD_BACKLIGHT	= 0x08  # back light on
E_DELAY			= 0.0005
E_PULSE			= 0.0005
ENABLE 			= 0b00000100 # Enable bit
LCD_CHR			= 1 # Mode - Sending data
LCD_CMD 		= 0 # Mode - Sending command
LCD_WIDTH 		= 16   # Maximum characters per line

class DisplayIO(object):
	def __init__(self, busNumber, addr, registerSetting, registerDisplay):
		self.__mBusNumber = busNumber
		self.__mAddr = addr
		self.__mRegSetting = registerSetting
		self.__mRegDisplay = registerDisplay
		self.__mBus = smbus.SMBus(self.__mBusNumber)
		try:
			self.__lcdByte(0x33, LCD_CMD) # 110011 Initialise
			self.__lcdByte(0x32, LCD_CMD) # 110010 Initialise
			self.__lcdByte(0x06, LCD_CMD) # 000110 Cursor move direction
			self.__lcdByte(0x0C, LCD_CMD) # 001100 Display On,Cursor Off, Blink Off 
			self.__lcdByte(0x28, LCD_CMD) # 101000 Data length, number of lines, font size
			self.__lcdByte(0x01, LCD_CMD) # 000001 Clear display
			time.sleep(E_DELAY)
		except:
			LOG.ERROR(__name__, "Display init error.")

	def __del__(self):
		pass

	def writeStr1st(self, dispStr):
		LOG.INFO(__name__, "1stDisp[{}]".format(dispStr))
		dispStr = str(dispStr)
		dispStr = dispStr.ljust(LCD_WIDTH, " ")

		self.__lcdByte(LCD_LINE_1, LCD_CMD)
		for i in range(LCD_WIDTH):
			self.__lcdByte(ord(dispStr[i]),LCD_CHR)

		return

	def writeStr2nd(self, dispStr):
		LOG.INFO(__name__, "2ndDisp[{}]".format(dispStr))
		dispStr = str(dispStr)
		dispStr = dispStr.ljust(LCD_WIDTH, " ")

		self.__lcdByte(LCD_LINE_2, LCD_CMD)
		for i in range(LCD_WIDTH):
			self.__lcdByte(ord(dispStr[i]),LCD_CHR)

		return

	def __lcdByte(self, bits, mode):
		# Send byte to data pins
		# bits = the data
		# mode = 1 for data
		#        0 for command
		bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
		bits_low = mode | ((bits<<4) & 0xF0) | LCD_BACKLIGHT

		# High bits
		self.__mBus.write_byte(self.__mAddr, bits_high)
		self.__lcdToggleEnable(bits_high)

		# Low bits
		self.__mBus.write_byte(self.__mAddr, bits_low)
		self.__lcdToggleEnable(bits_low)

		return

	def __lcdToggleEnable(self, bits):
		# Toggle enable
		time.sleep(E_DELAY)
		self.__mBus.write_byte(self.__mAddr, (bits | ENABLE))
		time.sleep(E_PULSE)
		self.__mBus.write_byte(self.__mAddr,(bits & ~ENABLE))
		time.sleep(E_DELAY)

		return
