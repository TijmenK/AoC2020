inputSequence = [17,1,3,16,19,0]
lastNumber = inputSequence[-1]
inputSequence= inputSequence[0:-1]
memoryDict = {}

index = 0
for number in inputSequence:
    memoryDict[number] = [index]
    index+=1

print(memoryDict)
    
def nextNumber(number, index, memDict):
    if number in memDict.keys():
        memDict[number].append(index)
        if len(memDict[number]) > 1:
            return(memDict[number][-1]-memDict[number][-2])
        else:
            return(0)
    else:
        memDict[number] = [index]
        return(0)


while index < 30000000-1:
    lastNumber = nextNumber(lastNumber, index, memoryDict)
    index+=1

print(lastNumber)
