#!/usr/bin/env python
#coding=utf-8

import web
from urls import urls
from config import *
from app.api.log import *

app = web.application(urls, globals())

if __name__ == "__main__":
	logclass.append(cLogs())
	app.run()
