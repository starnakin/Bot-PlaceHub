import json
import os

def getData(file, key):
    with open('./utilities/'+file+".json") as f:
        return json.load(f)[key]

def setData(file, key, value):
    with open('./utilities/'+file+".json", "w") as f:
        json.dumps(key, value)

def getPrefix():
    return getData("config", "prefix")

def setPrefix(prefix):
    setData("config", "prefix", prefix)

def getActivity():
    return getData("config", "activity")

def setActivity(activity):
    setData("config", "activity", activity)

def getToken():
    return getData("config", "token")

def getChannel(arg1):
    return getData("channels", arg1)

def getMessage(arg1):
    return getData("messages", arg1)

def getRole(arg1):
    return getData("roles", arg1)