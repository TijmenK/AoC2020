with open("day03_input.txt") as textFile:
        lines = textFile.readlines()
# lines = [[1 if char == '#' else 0 for char in line.rstrip()] for line in open("day03_input.txt")]
linelength = len(lines[0]) - 1
steppedlines = []

#part1
xCounter = 0;
treeCounter = 0;

for step in lines:
    if step[xCounter%linelength] == '#':
        treeCounter = treeCounter + 1
        curline = list(step)
        curline[xCounter%linelength] = "X"
        steppedlines.append("".join(curline))
    else:
        curline = list(step)
        curline[xCounter%linelength] = "O"
        steppedlines.append("".join(curline))
    xCounter = xCounter + 3
    
print(steppedlines)
print(treeCounter)
print("End part 1")

#part2
slopeArray = [[1,1],[3,1],[5,1],[7,1],[1,2]]

def slopeChecker (slope):
    horizontalStep = slope[0]
    verticalStep = slope[1]
    xCounter = 0;
    treeCounter = 0;
    
    for index, step in enumerate(lines):
        print(step)
        if index % verticalStep == 0:
            if step[xCounter%linelength] == '#':
                treeCounter = treeCounter + 1
            xCounter = xCounter + horizontalStep
    return(treeCounter)

slopeResults = []

for slope in slopeArray:
    slopeResults.append(slopeChecker(slope))

import math
print(slopeResults)
print(math.prod(slopeResults))