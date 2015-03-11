#!/usr/bin/env python
#coding=utf-8

import web
from urls import urls
from config import *
from app.api.log import *

logclass.append(cLogs())
app = web.application(urls, globals())
application = app.wsgifunc()
