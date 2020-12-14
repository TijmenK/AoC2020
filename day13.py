instructions = [line.rstrip() for line in open("day13_input.txt")]

timeStamp = int(instructions[0])
busIDs = [int(x) for x in instructions[1].split(",") if x != 'x']

shortestWait = [1000, 0]
for bus in busIDs:
    waitTime = bus - timeStamp % bus
    if waitTime < shortestWait[0]:
        shortestWait = [waitTime, bus]
        
print("Part 1 answer: " + str(shortestWait[0]) + " * " + str(shortestWait[1]) + " = " + str(shortestWait[0] * shortestWait[1]))

busID2 = [int(x) for x in instructions[1].replace('x', '1').split(",")]

from math import prod
def crt(ns, bs):
    # Chinese Remainder Theorem
    # https://brilliant.org/wiki/chinese-remainder-theorem/
    N = prod(ns)
    x = sum(b * (N // n) * pow(N // n, -1, n) for b, n in zip(bs, ns))
    return x % N

times = []
offsets = []
for idx, bus in enumerate(busID2):
    if bus != 1:
        times.append(bus)
        offsets.append(bus-idx)

print("Part 2 answer: " + str(crt(times, offsets)))