from tools.fetch import submit
CARD_VALUE = {
    "A":"14", "K":"13","Q":"12","J":"11","T":"10",
    **{(str(i)):f"0{i}" for i in range(2,10)}
}

CARD_VALUE_2 = {
    "A":"14", "K":"13","Q":"12","J":"01","T":"10",
    **{(str(i)):f"0{i}" for i in range(2,10)}
}

def answer(data):
    data = [parseRow(row) for row in data]
    sortedHands = sorted(data,key=getHandValue)
    return sum([(i+1)*hand["bid"] for i, hand in enumerate(sortedHands)])

def parseRow(row):
    hand, bid = row.split(" ")
    return {"hand":hand, "bid":int(bid)}

def countHand(hand):
    counts = {}
    for card in hand:
        counts[card] = counts[card] + 1 if card in counts else 1
    return counts

def getHandValue(hand):
    parsedHand = countHand(hand["hand"])
    sortedCounts = sorted([str(count) for count in parsedHand.values()], reverse=True)
    return "".join(sortedCounts) + "".join([ CARD_VALUE[card] for card in hand["hand"]])

submit(7,1,answer)

def countHand2(hand):
    counts = {}
    for card in hand:
        counts[card] = counts[card] + 1 if card in counts else 1
    if "J" in counts and len(counts) > 1:
        jokers =  counts["J"]
        del counts["J"]
        maxKey = max(counts,key=counts.get)
        counts[maxKey] = counts[maxKey] + jokers
    return counts

def getHandValue2(hand):
    parsedHand = countHand2(hand["hand"])
    sortedCounts = sorted([str(count) for count in parsedHand.values()], reverse=True)
    return "".join(sortedCounts) + "".join([ CARD_VALUE_2[card] for card in hand["hand"]])

def answer2(data):
    data = [parseRow(row) for row in data]
    sortedHands = sorted(data,key=getHandValue2)
    return sum([(i+1)*hand["bid"] for i, hand in enumerate(sortedHands)])

submit(7,2,answer2)
