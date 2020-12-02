from datetime import datetime

starttime = datetime.now()
print(starttime)
"""
import pandas as pd
input_df = pd.read_csv("day1_input.csv", header=None)
#part1
for index1, row in input_df.iterrows():
    for index2, row in input_df.iterrows():
        if row[0] + input_df[0][index1]  == 2020 :
            print(row[0] * input_df[0][index1])
            finishtime = datetime.now()
            print(finishtime)
            break

#part2
for index1, row in input_df.iterrows():
    for index2, row in input_df.iterrows():
        for index3, row in input_df.iterrows():
            if row[0] + input_df[0][index1] + input_df[0][index2]  == 2020 :
                print(row[0] * input_df[0][index1]* input_df[0][index2])
                finishtime = datetime.now()
                print(finishtime)

expense_list = [int(line) for line in open('day1_input.txt', 'r')]

for e in expense_list:
    for f in expense_list:
        if e + f  == 2020 :
            print(e * f)
            finishtime = datetime.now()
            print(finishtime)
        
for e in expense_list:
    for f in expense_list:
        for g in expense_list:
            if e + f + g == 2020 :
                print(e * f * g)
                finishtime = datetime.now()
                print(finishtime)
                break

expense_list = [int(line) for line in open('day1_input.txt', 'r')]

for e in expense_list:
    lookup1 = 2020 - e
    if lookup1 in expense_list:
        print(e * lookup1)
        
    for f in expense_list:
        lookup2 = lookup1 - f
        if lookup2 in expense_list:
            print(e * f * lookup2)

expense_list = [int(line) for line in open('day1_input.txt', 'r')]
solved1 = False
solved2 = False

for e in expense_list:
    lookup1 = 2020 - e
    if lookup1 in expense_list:
        print(e * lookup1)
        solved1 = True
        
    for f in expense_list:
        lookup2 = lookup1 - f
        if lookup2 in expense_list:
            print(e * f * lookup2)
            solved2 = True
            
    if solved1 & solved2:
        finishtime = datetime.now()
        print(finishtime)
        exit()
"""    
starttime = datetime.now();
expense_list = [int(line) for line in open('day1_input.txt', 'r')]

for e in expense_list:
    lookup1 = 2020 - e
    if lookup1 in expense_list:
        print(e * lookup1)
        
    for f in expense_list:
        lookup2 = lookup1 - f
        if lookup2 in expense_list:
            print(e * f * lookup2)
            
import pandas as pd
expense_dict = {row[0] for _, row in pd.read_csv("day1_input.csv").iterrows()}

for e in expense_dict:
    lookup1 = 2020 - e
    if lookup1 in expense_dict:
        print(e * lookup1)
        
for e in expense_dict:
    lookup1 = 2020 - e
    for f in expense_dict:
        lookup2 = lookup1 - f
        if lookup2 in expense_dict:
            print(e * f * lookup2)
            finishtime = datetime.now()
            print(finishtime)
            exit()
