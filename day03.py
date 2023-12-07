from tools.fetch import submit
from functools import reduce

GAME_SET= {"blue":14,"red":12,"green":13}

def answer(data):
    data = [parseRow(row )for row in data]
    symbolAdjacentPos = getSymbolAdjacentPos(data)
    numbers = getNumbersAndPos(data)
    return sum([n["number"] for n in numbers if hasAdjacentSymbol(n,symbolAdjacentPos)])

def parseRow(row):
    return [c for c in row]

def getSymbolAdjacentPos(data):
    pos = set()
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] != '.' and not data[i][j].isdigit():
                pos = pos.union(getAdjacentPos(i,j,len(data),len(data[0])))
    return pos

def getAdjacentPos(i,j,m,n):
    pos = set()
    pos.add((i,j))
    if j > 0:
        pos.add((i,j-1))
    if j < n - 1:
        pos.add((i,j+1))
    if i>0:
        pos.add((i-1,j))
        if j > 0:
            pos.add((i-1,j-1))
        if j < n - 1:
            pos.add((i-1,j+1))
    if i < m - 1:
        pos.add((i+1,j))
        if j > 0:
            pos.add((i+1,j-1))
        if j < n - 1:
            pos.add((i+1,j+1))
    return pos

def getNumbersAndPos(data):
    numbers = []
    current = None
    currentPos = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            c = data[i][j]
            if c.isdigit():
                currentPos.append((i,j))
                current = c if current is None else current + c
            else:
                if current is not None:
                    numbers.append({"number":int(current),"pos":currentPos})
                current = None
                currentPos = []
    return numbers

def hasAdjacentSymbol(number,adjacentSymbols):
    for pos in number["pos"]:
        if pos in adjacentSymbols:
            return True
    return False

submit(3,1,answer)

def getAdjacentNumber(i,j,numbers,n,m):
    symbolPos = getAdjacentPos(i,j,n,m)
    return [n for n in numbers if hasAdjacentSymbol(n,symbolPos)]

def findGears(data, numbers):
    gears=[]
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '*':
                adjacentNumbers = getAdjacentNumber(i,j,numbers,len(data),len(data[i]))
                if len(adjacentNumbers) == 2:
                    gears.append(adjacentNumbers[0]["number"]*adjacentNumbers[1]["number"])
    return gears

def answer2(data):
    data = [parseRow(row )for row in data]
    numbers = getNumbersAndPos(data)
    return sum(findGears(data,numbers))

submit(3,2,answer2)
