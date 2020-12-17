import copy

def printGrid(array2D):
    for row in array2D:
        print(row)

def printCube(array3D):
    for idx, plane in enumerate(array3D):
        print("Z is: " + str(int(idx +0.5 - len(array3D)/2)))
        printGrid(plane)

startCube = [[[1 if char == '#' else 0 for char in line.rstrip()] for line in open("day17_input.txt")] for k in range(1)]

def checkAdjacent(z, y, x, shiftCube):
    w = len(shiftCube[0][0])
    h = len(shiftCube[0])
    d = len(shiftCube)
    state = shiftCube[z][y][x] == 1
    activeCount = 0
    for i in range(-1,2):
        for j in range(-1,2):
            for k in range(-1,2):
                if not(i == j == k == 0):
                    if 0 <=i+z < d and 0 <= j+y < h and 0 <= k+x < w:
                        activeCount += shiftCube[i+z][j+y][k+x]
    if state and activeCount in (2, 3):
        return(1)                
    elif state == False and activeCount == 3:
        return(1)                
    else:
        return(0)

def tick(Cube):
    w = len(Cube[0]) + 2
    h = len(Cube[0]) + 2
    d = len(Cube) + 2
    shiftCube = [[[0 for i in range(w)] for j in range(h)] for k in range(d)]
    for zIDX, Z in enumerate(Cube):
        for yIDX, Y in enumerate(Z):
            for xIDX, X in enumerate(Y):
                shiftCube[zIDX+1][yIDX+1][xIDX+1] = X
    newCube = [[[0 for i in range(w)] for j in range(h)] for k in range(d)]
    for zIDX, Z in enumerate(newCube):
        for yIDX, Y in enumerate(Z):
            for xIDX, X in enumerate(Y):
                newCube[zIDX][yIDX][xIDX] = checkAdjacent(zIDX, yIDX, xIDX,shiftCube)
    return(newCube)

for i in range(6):
    startCube = copy.deepcopy(tick(startCube))
print("Part 1 answer is: "+ str(str(startCube).count('1')))


startCube2 = [[[[1 if char == '#' else 0 for char in line.rstrip()] for line in open("day17_input.txt")] for k in range(1)] for l in range(1)]

def checkAdjacent2(w, z, y, x, shiftCube):
    wi = len(shiftCube[0][0][0])
    h = len(shiftCube[0][0])
    d = len(shiftCube[0])
    e = len(shiftCube)
    state = shiftCube[w][z][y][x] == 1
    activeCount = 0
    for l in range(-1,2):
        for i in range(-1,2):
            for j in range(-1,2):
                for k in range(-1,2):
                    if not(l == i == j == k == 0):
                        if 0 <=i+z < d and 0 <= j+y < h and 0 <= k+x < wi and 0 <= l+w < e:
                            activeCount += shiftCube[l+w][i+z][j+y][k+x]
    if state and activeCount in (2, 3):
        return(1)                
    elif state == False and activeCount == 3:
        return(1)                
    else:
        return(0)

def tick2(Cube):
    w = len(Cube[0][0][0]) + 2
    h = len(Cube[0][0]) + 2
    d = len(Cube[0]) + 2
    e = len(Cube) + 2
    shiftCube = [[[[0 for i in range(w)] for j in range(h)] for k in range(d)] for l in range(e)]
    for wIDX, W in enumerate(Cube):
        for zIDX, Z in enumerate(W):
            for yIDX, Y in enumerate(Z):
                for xIDX, X in enumerate(Y):
                    shiftCube[wIDX+1][zIDX+1][yIDX+1][xIDX+1] = X
    newCube = [[[[0 for i in range(w)] for j in range(h)] for k in range(d)] for l in range(e)]
    for wIDX, W in enumerate(newCube):
        for zIDX, Z in enumerate(W):
            for yIDX, Y in enumerate(Z):
                for xIDX, X in enumerate(Y):
                    newCube[wIDX][zIDX][yIDX][xIDX] = checkAdjacent2(wIDX, zIDX, yIDX, xIDX, shiftCube)
    return(newCube)

for i in range(6):
    startCube2 = copy.deepcopy(tick2(startCube2))
    print(str(startCube2).count('1'))
          
print("Part 2 answer is: "+ str(str(startCube2).count('1')))