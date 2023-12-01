from tools.fetch import submit, pullProblem

def answer(data):
    return sum([answerLine(l) for l in data])

def answerLine(line):
    filteredLine = [c for c in line if c.isdigit()]
    return int(filteredLine[0] + filteredLine[-1])

submit(1,1,answer)

def answer2(data):
    return sum([answerLine2(l) for l in data])

numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def isDigit(line):
    if line[0].isdigit():
        return line[0]
    for w in numbers.keys():
        if line.startswith(w):
            return numbers[w]
    return False

def answerLine2(line):
    filteredLine = [isDigit(line[i:]) for i in range(len(line)) if isDigit(line[i:])]
    return int(filteredLine[0] + filteredLine[-1])

submit(1,2,answer2)