import math


def firstrun():
    return "success"


def radiusToArea(radius):
    return math.pi * math.pow(radius, 2)


def firstLast(listIn):
    if len(listIn) <= 0:
        return listIn
    else:
        newList = listIn.copy()
        del newList[1:len(newList)-1]
        return newList


def timeSpan(dateA, dateB):
    delta = abs(dateA-dateB).days
    return delta
