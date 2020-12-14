seatGrid = [[3 if char == '.' else 0 for char in line.rstrip()] for line in open("day11_input.txt")]

h = len(seatGrid)
w= len(seatGrid[0])

def printGrid(array):
    for row in array:
        print(row)

def checkAdjacent(row, chair):
    if seatGrid[row][chair] == 3:
        return 3
    adjacentArray = [[0 for i in range(3)] for j in range(3)]
    itRow = 0
    itChair = 0
    for i in range(row-1,row+2):
        for j in range(chair-1,chair+2):
            if 0<=i<h and 0<= j < w:
                adjacentArray[itRow][itChair] = seatGrid[i][j]
            else:
                adjacentArray[itRow][itChair] = 3
            itChair += 1
        itRow += 1
        itChair = 0
    filledSeats = str(adjacentArray).count('1') - adjacentArray[1][1]
    if filledSeats == 0:
        return(1)
    elif filledSeats > 3:
        return(0)
    else:
        return(adjacentArray[1][1])

def occupySeats(seatGrid):
    newGrid = [[0 for i in range(w)] for j in range(h)]
    for rowIDX, row in enumerate(seatGrid):
        for chairIDX, chair in enumerate(row):
            newGrid[rowIDX][chairIDX] = checkAdjacent(rowIDX, chairIDX)
    return(newGrid)

directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

def checkAdjacent2(j, i):
    if seatGrid[j][i] == 3:
        return 3
    count = 0
    for direction in directions:
        distance = 0
        while True:
            distance += 1
            y = direction[0]*distance + j
            x = direction[1]*distance + i
            if not (y >= 0 and y < h and x >= 0 and x < w): break
            if seatGrid[y][x] == 1:
                count += 1
                break
            if seatGrid[y][x] == 0:
                break
    if count == 0:
        return(1)
    elif count > 4:
        return(0)
    else:
        return(seatGrid[j][i])
    
def occupySeats2(seatGrid):
    newGrid = [[0 for i in range(w)] for j in range(h)]
    for rowIDX, row in enumerate(seatGrid):
        for chairIDX, chair in enumerate(row):
            newGrid[rowIDX][chairIDX] = checkAdjacent2(rowIDX, chairIDX)
    return(newGrid)


iterator = 0
unchanged = False
while unchanged == False and iterator < 500:
    oldGrid = [x[:] for x in seatGrid]
    seatGrid = [x[:] for x in occupySeats2(seatGrid)]
    iterator+=1
    unchanged = oldGrid == seatGrid

print("part2: " + str(str(seatGrid).count('1')))
