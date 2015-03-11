#!/usr/bin/env python
#coding=utf8

import logging
from logging.handlers import RotatingFileHandler
from config import *

class cLogs():
	def __init__(self):
		handler = RotatingFileHandler(logfile, maxBytes = logmax, backupCount = backlog)
		formatter = logging.Formatter(formatlog)
		handler.setFormatter(formatter)
		
		self.logger = logging.getLogger()
		self.logger.addHandler(handler)
		self.logger.setLevel(logging.DEBUG)
	
	def Log_Info(self, server, url, status, message):
		return self.logger.info('%s %s %s %s' %(server, url, status, message))

	def Log_Warning(self, server, url, status, message):
		return self.logger.warning('%s %s %s %s' %(server, url, status, message))

	def Log_Debug(self, server, url, status, message):
		return self.logger.debug('%s %s %s %s' %(server, url, status, message))



