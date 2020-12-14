import re
instructions = [line.rstrip().split(" = ") for line in open("day14_input.txt")]
mem = [0] * 100000
mask = ""

def bitmask(value, mask):
    for idx, char in enumerate(mask[::-1]):
        if char == '0':
            value &=~ (1<<idx)
        if char == '1':
            value |= (1<<idx)
    return(value)
    

for line in instructions:
    if line[0] == 'mask':
        mask = line[1]
    else:
        memloc = re.findall('\d+', line[0] )[0]
        value = int(line[1])
        mem[int(memloc)] = bitmask(value, mask)

memSum = 0
for value in mem:
    memSum+= value

print("Part 1 answer: " + str(memSum))
memdict = {}
def bitmask2(value, mask):
    bitString = ""
    for idx, char in enumerate(mask[::-1]):
        if char == '0':
            bitString = str(value >> idx & 1) + bitString
        elif char == '1':
            bitString = str(1) + bitString
        elif char == 'X':
            bitString = 'X' + bitString
    addresses = []
    X_indices = [i for i, e in enumerate(bitString) if e == "X"]
    for i in range(2**bitString.count('X')):
        stringList = list(bitString)
        for j in range(len(X_indices)):
            stringList[X_indices[j]] = str(i >> j & 1)
        addresses.append(int("".join(stringList),2))
    return(addresses)
    

for line in instructions:
    if line[0] == 'mask':
        mask = line[1]
    else:
        memloc = re.findall('\d+', line[0] )[0]
        value = int(line[1])
        memlocs = bitmask2(int(memloc), mask)
        for each in memlocs:
            memdict[each] = value

mem2Sum = sum(memdict.values())
print("Part 2 answer: " + str(mem2Sum))