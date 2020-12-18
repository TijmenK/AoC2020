import re

def evaluateString(string):
    startVal = int(string[0])
    for i in range(1,len(string)-1):
        if string[i] == '*': startVal *= int(string[i+1])
        if string[i] == '+': startVal += int(string[i+1])
    return(startVal)

def processLine(line):
    line = list(re.sub(' ', '', line))
    while '(' in line:
        indicesOpen = [i for i,x in enumerate(line) if x == "("]
        indicesClose = [i for i,x in enumerate(line) if x == ")"]
        distanceDict = {}
        for indexO in indicesOpen:
            for indexC in indicesClose:
                if indexC - indexO > 0: distanceDict[(indexO, indexC)] = indexC - indexO
        firstPair = min(distanceDict, key = distanceDict.get)
        subLine = line[firstPair[0]+1:firstPair[1]]
        line[firstPair[0]] = str(evaluateString(subLine))
        del line[firstPair[0]+1:firstPair[1]+1]
    return(evaluateString(line))

part1 = sum([processLine(line.strip()) for line in open("day18_input.txt")])
print('Part 1 answer: ' + str(part1))

def evaluateString2(string):
    while '+' in string:
        indexA = string.index('+')
        string[indexA-1] = int(string[indexA-1]) +int(string[indexA+1])
        del string[indexA:indexA+2]
    startVal = int(string[0])
    for i in range(1,len(string)-1):
        if string[i] == '*': startVal *= int(string[i+1])
        if string[i] == '+': startVal += int(string[i+1])
    return(startVal)

def processLine2(line):
    line = list(re.sub(' ', '', line))
    while '(' in line:
        indicesOpen = [i for i,x in enumerate(line) if x == "("]
        indicesClose = [i for i,x in enumerate(line) if x == ")"]
        distanceDict = {}
        for indexO in indicesOpen:
            for indexC in indicesClose:
                if indexC - indexO > 0: distanceDict[(indexO, indexC)] = indexC - indexO
        firstPair = min(distanceDict, key = distanceDict.get)
        subLine = line[firstPair[0]+1:firstPair[1]]
        line[firstPair[0]] = str(evaluateString2(subLine))
        del line[firstPair[0]+1:firstPair[1]+1]
    return(evaluateString2(line))

part2 = sum([processLine2(line.strip()) for line in open("day18_input.txt")])
print('Part 2 answer: ' + str(part2))