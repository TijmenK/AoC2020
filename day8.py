#!/usr/bin/env python
#-*- coding: utf-8 -*-

q = [line.rstrip().split(" ") for line in open("day8_input.txt")]

def q_checker(q_variation):
    iterator = 0
    position = 0
    accumulator = 0
    previousIns = {}
    while(iterator < 1000):
        if str(position) in previousIns:
            return('Part 1 answer = ' + str(accumulator))
        previousIns[str(position)] = 1
        if position >= len(q_variation):
            return('Part 2 answer = ' + str(accumulator))
        if q_variation[position][0] == 'acc':
            accumulator += int(q[position][1])
            position += 1
        elif q_variation[position][0] == 'jmp':
            position += int(q[position][1])
        elif q_variation[position][0] == 'nop':
            position += 1
        else:
            print('unknown instruction')
            break
        iterator +=1

# part1
print(q_checker(q))

# part2
for index, line in enumerate(q):
    if line[0] == "jmp":
        q[index][0] = "nop"
        outcome = q_checker(q)
        if outcome[5] != "1":
            print(outcome)
        q[index][0] = "jmp"
    elif line[0] == "nop":
        q[index][0] = "jmp"
        outcome = q_checker(q)
        if outcome[5] != "1":
            print(outcome)
        q[index][0] = "nop"
