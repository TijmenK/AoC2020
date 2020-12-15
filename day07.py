#!/usr/bin/env python3
from collections import defaultdict
import re

q = [line.rstrip() for line in open("day7_input.txt")]

bags_that_include = defaultdict(list)
contents = {}
for line in q:
    parentbag = re.search(r'(.*) bags contain', line).group(1)
    for bag in re.findall(r'\d+ (.*?) bag', line):
        bags_that_include[bag].append(parentbag)
    contents[parentbag] = re.findall(r'(\d+) (.*?) bag', line)

def countbags(bag):
    t = set(bag)
    for b in bag:
        t |= countbags(bags_that_include[b])
    return t
print(len(countbags(bags_that_include['shiny gold'])))

def unpack(bag):
    t = 0
    for n, m in contents[bag]:
        t += int(n)*unpack(m)
    return 1+t
print(unpack('shiny gold')-1)