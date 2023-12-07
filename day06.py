from tools.fetch import submit
import re
import math
from functools import reduce

def answer(data):
    data = parseData(data)
    possibilities = [countPossibilities(race) for race in data]
    return reduce(lambda x,y: x*y, possibilities)

def parseData(data):
    data = [re.split("\s+", row.split(":")[1].strip()) for row in data]
    return [ {
        "time": int(data[0][i]),
        "distance": int(data[1][i])
    } for i in range(len(data[0]))]

def distanceDelta(time, recordDistance, startTime):
    return (time - startTime) * startTime - recordDistance

def countPossibilities(race):
    delta = race["time"] ** 2 - 4 * race["distance"]
    root1 = math.floor((race["time"] - math.sqrt(delta))/2) + 1
    root2 = math.ceil((race["time"] + math.sqrt(delta))/2) - 1
    return root2 - root1 + 1

def answer2(data):
    data = parseData2(data)
    possibilities = [countPossibilities(race) for race in data]
    return reduce(lambda x,y: x*y, possibilities)

def parseData2(data):
    data = [re.sub("\s+","", row.split(":")[1].strip()) for row in data]
    return [{
        "time": int(data[0]),
        "distance": int(data[1])
    }]
submit(6,1,answer)
submit(6,2,answer2)

