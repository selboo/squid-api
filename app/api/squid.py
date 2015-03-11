#!/usr/bin/env python
#coding=utf8

from httplib import HTTPConnection
from glob import glob
from re import findall
from config import *


def Squid_PURGE(Squid, Type, URL, Q):
	try:
		Conn = HTTPConnection(host=Squid, port='80', timeout=timeout)
		Conn.request(Type, URL)
	except:
		message = 'Timeout'
		Status  = 408
		logclass[0].Log_Info(Squid, URL, Status, message)
	else:
		try:
			message = 'True'
			Status = Conn.getresponse().status
		except:
			message = 'Error'
			Status  = 409
			logclass[0].Log_Info(Squid, URL, Status, message)
		else:
			if Status == 403: message = 'Failure'
			logclass[0].Log_Info(Squid, URL, Status, message)
	finally:
		if Status not in [200, 404]: message = 'Failure'
		Conn.close()
	Q.put({'Squid' : Squid, 'message' : message})
	return True

def SERVER_LIST_HOST():
	Squid_List = []
	Squid_Host = []
	
	for host in squidfile:
		Squid_List.append(serverlis + host)

	for host in Squid_List:
		Squid_Host.extend(Read_File(host))

	return Squid_Host

def Read_File(file):
	result = []
	try:
		oFile = open(file, 'r')
		oHost = oFile.readlines()
	except:
		result = 'Null'
	else:
		for i in oHost:
			Host = i.split('#')[0]
			if Host != "": result.append(Host.split(',')[0])
	finally:
		oFile.close()
	return result

