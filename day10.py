chargers = [int(line.rstrip()) for line in open("day10_testinput.txt")]
chargers.append(max(chargers)+3)
chargers.append(0)
chargers.sort()

def findCharger1(chargers):
    count1 = 0
    count3 = 0
    for idx, charger in enumerate(chargers):
        if idx == len(chargers)-1:
            break
        if chargers[idx+1] == charger + 3:
            count3+=1
        elif chargers[idx+1] == charger + 1:
            count1+=1
    return([count1, count3])
part1 = findCharger1(chargers)

l = len(chargers)
ways = [1] + [0]*(l-1)
print(ways)
for i in range(1,l):
    ways[i] = sum((ways[o] for o in range(i-3,i) if chargers[i] <= (chargers[o]+3)))
part2 = ways[-1]

print("For part1 answer: " + str(part1) + " the result is "  + str(part1[0]) + " * " + str(part1[1]) + " = " + str(part1[0]*part1[1]))
print("The part2 answer is: " + str(part2))