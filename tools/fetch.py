import requests
from pathlib import Path
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
    article = html.tostring(pageTree.xpath("//main/article")[level-1])
    return int(html.fromstring(article).xpath("//code/em")[-1].text)


def sendAnswer(day, level, answer):
    resp = requests.post(f"https://adventofcode.com/2023/day/{day}/answer", headers=COOKIE_HEADERS,
                          data={"answer":answer, "level": level})
    tree =  html.fromstring(resp.content)
    return html.tostring(tree.xpath("//main/article")[0])

def submit(day, level,function):
    pageTree = html.fromstring(getPage(day))
    exampleAnswer = function(getExemple(pageTree, level))
    expectedAnswer = getExampleAnswer(pageTree,level)
    if (exampleAnswer != expectedAnswer):
        print(f"Wrong answer: {exampleAnswer}, expected: {expectedAnswer}")
        return
    print(sendAnswer(day, level, function(getInput(day))))
    pullProblem(day)

def pullProblem(day):
    pageTree = html.fromstring(getPage(day))
    articles = [ html.tostring(article) for article in pageTree.xpath("//main/article")]
    Path(f"day{day:02d}").mkdir(parents=True, exist_ok=True)
    for i in range(len(articles)):
        with open(f"day{day:02d}/level{i+1}.md", "wb") as f:
            f.write(articles[i])