#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import Builder
import MainController
import MenuController

def main():
	builder = Builder.Builder()
	threadList = builder.getThreads()
	for thread in threadList:
		thread.start()

	mainCtr = MainController.MainController()
	menuCtr = MenuController.MenuController()

	mainCtr.start()
	menuCtr.start()

	'''
	threadList[0].notifyCommand("TEMP_CMD_QUIT", None)
	threadList[1].notifyCommand("DATA_CMD_QUIT", None)
	threadList[2].notifyCommand("SWITCH_CMD_QUIT", None)
	threadList[3].notifyCommand("DISPLAY_CMD_QUIT", None)
	threadList[4].notifyCommand("PUMP_CMD_QUIT", None)
	'''

if __name__ == "__main__":
	main()