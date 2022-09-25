import time
import datetime

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
