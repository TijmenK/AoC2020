import pandas as pd
expense_dict = {row[0] for _, row in pd.read_csv("day1_input.csv").iterrows()}

print(len(expense_dict))
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
            exit()
