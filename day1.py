from datetime import datetime

starttime = datetime.now()
print(starttime)

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
