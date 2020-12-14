rawInstructions = [line.rstrip() for line in open("day12_input.txt")]
instructions=[]
for line in rawInstructions:
    instructions.append([line[0], int(line[1:])])

orientations = [[0,1], [1,0], [0,-1], [-1,0]]
position = [0, 0, 1]

def makeMove1(position, instruction):
    x = position[0]
    y = position[1]
    orientation = position[2]
    if instruction[0] == "L":
        orientation = int((position[2] - instruction[1] / 90) % 4)
    if instruction[0] == "R":
        orientation = int((position[2] + instruction[1] / 90) % 4)
    if instruction[0] == "F":
        x += instruction[1] * orientations[orientation][0]
        y += instruction[1] * orientations[orientation][1]
    if instruction[0] == "N":
        y += instruction[1]
    if instruction[0] == "E":
        x += instruction[1]
    if instruction[0] == "S":
        y -= instruction[1]
    if instruction[0] == "W":
        x -= instruction[1]
    return([x,y, orientation])

for line in instructions:
    print(line)
    position = makeMove1(position, line)
    
position2 = [0,0,1,10,1]

ccw_rotate = {1: lambda x, y: (-y, x),
              2: lambda x, y: (-x, -y),
              3: lambda x, y: (y, -x)}

cw_rotate = {1: lambda x, y: (y, -x),
             2: lambda x, y: (-x, -y),
             3: lambda x, y: (-y, x)}

def makeMove2(position, instruction):
    x = position2[0]
    y = position2[1]
    orientation = position2[2]
    neworientation = orientation
    x1 = position2[3]
    y1 = position2[4]
    if instruction[0] == "L":
        x1, y1 = ccw_rotate.get(int(instruction[1] / 90))(x1,y1)
    if instruction[0] == "R":
        x1, y1 = cw_rotate.get(int(instruction[1] / 90))(x1,y1)
    if instruction[0] == "F":
        x += instruction[1] * x1
        y += instruction[1] * y1
    if instruction[0] == "N":
        y1 += instruction[1]
    if instruction[0] == "E":
        x1 += instruction[1]
    if instruction[0] == "S":
        y1 -= instruction[1]
    if instruction[0] == "W":
        x1 -= instruction[1]
    return([x,y, neworientation, x1, y1])

for line in instructions:
    print(line)
    position2 = makeMove2(position2, line)
    
print("Manhattan position 1 is: "+ str(abs(position[0])+abs(position[1])))
print("Manhattan position 2 is: "+ str(abs(position2[0])+abs(position2[1])))