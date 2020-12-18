import pandas as pd
raw_df = pd.read_csv("day02_input.txt", header=None)

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        if last == "" :
            end = len(s)
        else:
            end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""                                  

passedPasswords1 = 0
passedPasswords2 = 0

for index, row in raw_df.iterrows():
    lower = int(find_between(row[0], "", "-"))
    upper = int(find_between(row[0], "-", " "))
    check = find_between(row[0], " ", ": ")
    password = find_between(row[0], ": ", "")
    count = password.count(check)
    if lower <= count & count <= upper:
        passedPasswords1 = passedPasswords1 + 1

for index, row in raw_df.iterrows():
    lower = int(find_between(row[0], "", "-"))
    upper = int(find_between(row[0], "-", " "))
    check = find_between(row[0], " ", ": ")
    password = find_between(row[0], ":", "")
    checksum = 0
    if lower<len(password):
        if password[lower] == check:
            checksum = 1
    if upper<len(password):
        if password[upper] == check:
            checksum = checksum + 1
    if checksum == 1: 
        passedPasswords2 = passedPasswords2 + 1
        
        
print(passedPasswords1)
print(passedPasswords2)