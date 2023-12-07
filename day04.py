from tools.fetch import submit
import re
from functools import reduce

def answer(data):
    data = [parseRow(row )for row in data]
    return sum([rowPower(row) for row in data])

def parseRow(row):
    card, cards = re.split(":\s+",row)
    cardNumber = re.split("\s+", card)[1]
    winnings, all = re.split("\s+\|\s+",cards)
    return {
        "number": int(cardNumber),
        "winnings": set(re.split("\s+",winnings)),
        "all": re.split("\s+",all)
        }

def rowPower(row):
    cards = [card for card in row["all"] if card in row["winnings"]]
    return 0 if len(cards) == 0 else 2 ** (len(cards) - 1)

def playOneCard(cardCounts, card):
    n = card["number"]
    cardCounts[n] = cardCounts[n] + 1 if n in cardCounts else 1
    cardScore = len([c for c in card["all"] if c in card["winnings"]])
    for i in range(1,cardScore+1):
        currentCount = cardCounts[n+i] if n+i in cardCounts else 0
        cardCounts[n+i] = currentCount + cardCounts[n]
    return cardCounts

def answer2(data):
    data = [parseRow(row )for row in data]
    cardCounts = reduce(playOneCard, data, {})
    return sum(cardCounts.values())

submit(4,1,answer)

submit(4,2,answer2)
