inputSequence = [17,1,3,16,19,0]
lastNumber = inputSequence[-1]
inputSequence= inputSequence[0:-1]
memoryDict = {}

index = 0
for number in inputSequence:
    memoryDict[number] = [index]
    index+=1
    
def nextNumber(number, index, memDict):
    if number in memDict:
        memDict[number].append(index)
        return(index-memDict[number][-2])
    else:
        memDict[number] = [index]
        return(0)

while index < 30000000 -1:
    lastNumber = nextNumber(lastNumber, index, memoryDict)
    index+=1
    if index == 2020-1:
        print(lastNumber)

print(lastNumber)
