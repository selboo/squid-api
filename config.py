#!/usr/bin/env python
#coding=utf8
from json import dumps
from os.path import abspath

global logclass
logclass  = []
logfile   = '/data/log/api_squid.log'
logmax    = 50 * 1024 * 1024
backlog   = 100
timeout   = 3
formatlog = '%(asctime)s - %(levelname)s - %(message)s'  
squidfile = ['BJ_serverlist.txt', 'SZ_serverlist.txt', 'TJ_serverlist.txt']
squidpath = '/squid/'
serverlis = abspath('.') + squidpath

def Return(Error, Code):
	result = {
		'Status' : Error,
		'Code'   : Code
	}
	return dumps(result)
