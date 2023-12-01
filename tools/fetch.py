import requests
from lxml import html
from tools.cookie import COOKIE

COOKIE_HEADERS = {"cookie": COOKIE }

def getPage(day):
    return requests.get(f"https://adventofcode.com/2023/day/{day}", headers=COOKIE_HEADERS).content

def getExemple(pageTree, level):
    rawInput = pageTree.xpath("//pre/code")[level-1].text
    return prepareInput(rawInput)

def getInput(day):
    rawInput = requests.get(f"https://adventofcode.com/2023/day/{day}/input", headers=COOKIE_HEADERS).text
    return prepareInput(rawInput)

def prepareInput(rawInput):
    return rawInput.split("\n")[:-1]

def getExampleAnswer(pageTree, level):
    return int(pageTree.xpath("//code/em")[level-1].text)


def sendAnswer(day, level, answer):
    resp = requests.post(f"https://adventofcode.com/2023/day/{day}/answer", headers=COOKIE_HEADERS,
                          data={"answer":answer, "level": level})
    return html.fromstring(resp.content).xpath("//main/article/p")[0].text

def submit(day, level,function):
    pageTree = html.fromstring(getPage(day))
    exampleAnswer = function(getExemple(pageTree, level))
    if (exampleAnswer != getExampleAnswer(pageTree,level)):
        print(f"Wrong answer: ")
        return
    print(sendAnswer(day, level, function(getInput(day))))

