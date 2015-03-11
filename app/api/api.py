#coding=utf-8

import web
from threading import Thread
from config import *
from squid import Squid_PURGE, SERVER_LIST_HOST
from json import dumps
from Queue import Queue
import re

class default:
	def GET(self):
		return Return('Error', 1001)
	def POST(self):
		return Return('Error', 1002)

class cache:
	def GET(self):
		return Return('Error', 1003)
	def POST(self):
		data = web.input()
		Type = data.type.upper()
		URL  = data.url
		if len(data) != 2: return Return('Error', 1006)
		if not re.findall('^PURGE$',  Type): return Return('Error', 1004)
		if not re.findall('^http://',  URL): return Return('Error', 1005)
		
		#SQUID_HOST = SERVER_LIST_HOST()
		SQUID_HOST = ['192.168.3.100', '192.168.4.100']
		threadings = []
		Queuedings = []
		Success    = 0
		Failure    = 0

		for h in SQUID_HOST:
			Q = Queue()
			Queuedings.append(Q)
			threadings.append(Thread(target=Squid_PURGE, args=(h, Type, URL, Q)))

		for t in threadings:
			t.setDaemon(True)
			t.start()

		for t in threadings:
			t.join()

		for q in Queuedings:
			if q.get()['message'] == 'True':
				Success = Success + 1
			else:
				Failure = Failure + 1

		result = {
			'total'   : len(Queuedings),
			'Success' : Success,
			'Failure' : Failure,
		}

		return dumps(result)

