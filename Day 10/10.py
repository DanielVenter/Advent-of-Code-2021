from collections import deque

def illegalChar(lines : list) -> str or None:
    opens = []
    for char in lines:
        if char in openChar:
            opens.append(char)
        else: 
            if char != close[opens.pop()]:
                return char
    return None

def part1(lines: list) -> int:
    score = 0
    for line in lines: 
        char = illegalChar(line)
        if char:
            score += scores1[char]
    return score


def complete(lines: list) -> int:
    opens = []
    for char in lines:
        if char in openChar:
            opens.append(char)
        else: 
            opens.pop()
        
    score = 0
    closes = ""
    while opens:
        closes += close[opens.pop()]
        score = score*5 + scores2[closes[-1]]

    return score

def part2(lines):
    scores = []
    for line in lines:
        if illegalChar(line):
            continue
        scores.append(complete(line))
    return sorted(scores)[len(scores)//2]


with open("input.txt", "r") as f:
    lines = [line.strip("\n") for line in f]

openChar = ["(", "{", "[", "<"]
close = {"(" : ")", "{" : "}" , "[" : "]", "<" : ">"}
scores1 = {")" : 3, "}" : 1197, "]" : 57, ">" : 25137}
scores2 = {")" : 1, "}" : 3, "]" : 2, ">" : 4}


print(part2(lines))



