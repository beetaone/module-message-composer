import time
import datetime
from os import getenv

def getTimestamp():
    return time.time()

def getTime():
    e = datetime.datetime.now()
    return f"{e.hour}:{e.minute}:{e.second}.{e.microsecond}"

def getDate():
    e = datetime.datetime.now()
    return f"{e.year}-{e.month}-{e.day}"

def getDateAndTime():
    return str(datetime.datetime.now())

def getNodeID():
    return getenv("NODE_ID", "")

def getNodeName():
    return getenv("NODE_NAME", "")
