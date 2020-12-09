#!/usr/bin/env python
#-*- coding: utf-8 -*-

q = [int(line.rstrip()) for line in open("day9_input.txt")]

preambleSize = 25
def findNumber(preAmble, q):
    for idx, value in enumerate(q[preAmble:]):
        searchDict = {el:1 for el in q[idx:idx+preAmble]}
        found = False
        for key in searchDict:
            if value - key in searchDict:
                found = True
                break
        if found == False:
            return(value)
        
target = findNumber(preambleSize, q)

contigIndex = 0
contigLength = 0

for idx,value in enumerate(q):
    contigSum = 0
    iterator = 0
    while(contigSum < target):
        contigSum += q[idx+iterator]
        iterator +=1
    if contigSum == target and iterator > contigLength:
        contigIndex = idx
        contigLength = iterator

subQ = q[contigIndex:contigIndex+contigLength-1]

print("For part1 answer: " + str(target) + " the longest contig of length: " + str(contigLength) + " is found at index: " + str(contigIndex))
print("So the part2 answer is: " + str(min(subQ)) + " + " + str(max(subQ)) + " = " + str(min(subQ)+max(subQ)))