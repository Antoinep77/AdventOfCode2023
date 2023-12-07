from tools.fetch import submit

def answer(input):
    seeds,maps = input
    state = "seed"
    while state != "location":
        map = [m for m in maps if m["source"] == state][0]
        state = map["dest"]
        seeds = [convert(s, map) for s in seeds]
    return min(seeds)

def parseData(data):
    groups = data.split("\n\n")
    seeds = [int(s) for s in groups[0].split(": ")[1].split(" ")]
    maps = [ parseMap(m) for m in groups[1:]]
    return seeds,maps

def parseMap(map):
    lines = map.strip().split("\n")
    source, dest = lines[0].split(" ")[0].split("-to-")
    mapValues = [l.split(" ") for l in lines[1:]]
    values = [{"destStart": int(l[0]) , "sourceStart":int(l[1]), "length": int(l[2]) } for l in mapValues]
    return {"source": source, "dest": dest, "values": values}

def convert(val,map):
    for mapValue in map["values"]:
        if 0 <= val - mapValue["sourceStart"] < mapValue["length"]:
            return val - mapValue["sourceStart"] + mapValue["destStart"]
    return val

def parseData2(data):
    groups = data.split("\n\n")
    seeds = [int(s) for s in groups[0].split(": ")[1].split(" ")]
    seeds = parseSeed(seeds)
    maps = [ parseMap(m) for m in groups[1:]]
    return seeds,maps

def parseSeed(seedRanges):
    seeds = []
    for i in range(0,len(seedRanges),2):
        seeds.append({ "start":seedRanges[i], "end":seedRanges[i] + seedRanges[i+1] - 1})
    return seeds

def convert2(seed,map):
    if seed["start"] > seed["end"]:
        return []
    for mapValue in map["values"]:
        if  mapValue["sourceStart"] <= seed["start"] < mapValue["sourceStart"] + mapValue["length"] or mapValue["sourceStart"] <= seed["end"] < mapValue["sourceStart"] + mapValue["length"] :
            beforeSeeds = {"start": seed["start"], "end": mapValue["sourceStart"] - 1 }
            afterSeeds = {"start": mapValue["sourceStart"] + mapValue["length"], "end": seed["end"] }
            beforeResult = convert2(beforeSeeds,map)
            afterResult = convert2(afterSeeds,map)
            convertedSeed = { "start": max([seed["start"],mapValue["sourceStart"]]) - mapValue["sourceStart"] + mapValue["destStart"],
                             "end": min([seed["end"],mapValue["sourceStart"] + mapValue["length"] - 1]) - mapValue["sourceStart"] + mapValue["destStart"]}
            return [convertedSeed] + beforeResult + afterResult
    return [seed]

def answer2(input):
    seeds,maps = input
    state = "seed"
    while state != "location":
        map = [m for m in maps if m["source"] == state][0]
        state = map["dest"]
        seeds = [convert2(s, map) for s in seeds]
        seeds = [s for sList in seeds for s in sList]
    return min([s["start"] for s in seeds])

submit(5,1,answer,parseData)
submit(5,2,answer2,parseData2, skipVerification=True)

