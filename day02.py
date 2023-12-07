from tools.fetch import submit
from functools import reduce

GAME_SET= {"blue":14,"red":12,"green":13}

def answer(data):
    data = [parseRow(row )for row in data]
    return sum([game["id"] for game in data if isGameOk(game)])

def parseRow(row):
    splitted_row = row.split(': ')
    id = int(splitted_row[0].split(' ')[1])
    sets = [ parseSet(setStr) for setStr in splitted_row[1].split("; ")]
    return {"id": id, "sets": sets}

def parseSet(setStr):
    items = setStr.split(', ')
    items = [item.split(" ") for item in items]
    return { color: int(count) for [count,color] in  items }

def isGameOk(game):
    notOkSets = [gameSet for gameSet in game["sets"] if not isSetOk(gameSet)]
    return len(notOkSets) == 0

def isSetOk(gameSet):
    notOkKeys = [ color for color,count in gameSet.items() if GAME_SET[color]<count]
    return len(notOkKeys) == 0

submit(2,1,answer)

def answer2(data):
    data = [parseRow(row )for row in data]
    return sum([powerMinSet(game) for game in data])

def powerMinSet(game):
    minSet = {}
    for gameSet in game["sets"]:
        minSet = getMinSet(minSet,gameSet)
    return reduce(lambda x,y: x*y,minSet.values())

def getMinSet(gameSet1,gameSet2):
    keys = set(gameSet1.keys()).union(set(gameSet2.keys()))
    minSet = {}
    for key in keys:
        if key not in gameSet1:
            minSet[key] = gameSet2[key]
        elif key not in gameSet2:
            minSet[key] = gameSet1[key]
        else: minSet[key] = max(gameSet1[key], gameSet2[key])
    return minSet


submit(2,2,answer2)

