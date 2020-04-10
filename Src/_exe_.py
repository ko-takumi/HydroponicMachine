#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import Builder
import LogPrint as LOG

def main():
	LOG.INFO(__name__, "HydroponicMachine start.")

	builder = Builder.Builder()
	threadList = builder.getThreads()
	for thread in threadList:
		thread.start()

if __name__ == "__main__":
	main()