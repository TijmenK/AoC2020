import re

allDicts = []
passKeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid','cid']
passDict = dict.fromkeys(passKeys)
passString = ''

with open("day4_input.txt", "r") as a_file:
  for line in a_file:
    stripped_line = line.strip()
    if stripped_line == "":
        for subPair in (passString.split(' ')):  
             couples= subPair.split(':')
             passDict[couples[0]] = couples[1]
        allDicts.append(passDict)
        passDict = dict.fromkeys(passKeys)
        passString = ''
    elif passString == '':
        passString = stripped_line
    else:
        passString = passString + ' ' + stripped_line

validCounter = 0
invalidCounter = 0

def passChecker(passport):
    emptyKeys = []
    for key in passport:
        if passport[key] == None:
            emptyKeys.append(key)
    if len(emptyKeys) > 1:
        return False
    if len(emptyKeys) == 1 and emptyKeys[0] != 'cid':
        return False
    if int(passport['byr']) < 1920 or 2002 < int(passport['byr']):
        return False
    if int(passport['iyr']) < 2010 or 2020 < int(passport['iyr']):
        return False
    if int(passport['eyr']) < 2020 or 2030 < int(passport['eyr']):
        return False
    lengthUnit = re.sub('[^a-zA-Z]','', passport['hgt'])
    lengthNumber = int(re.sub('[^0-9]','', passport['hgt']))
    if lengthUnit == 'cm' and (lengthNumber < 150 or 193 < lengthNumber):
        return False
    if lengthUnit == 'in' and (lengthNumber < 59 or 76 < lengthNumber):
        return False
    if lengthUnit == '':
        return False
    if re.match("^#[a-fA-F0-9]{6}$", passport['hcl']) == None:
        return False
    if re.match("^(amb|blu|brn|gry|grn|hzl|oth)$", passport['ecl']) == None:
        return False
    if re.match("^[0]*\d{9}$", passport['pid']) == None:
        return False
    return True
    
for passport in allDicts:
    if(passChecker(passport)):
        validCounter = validCounter + 1
    else:
        invalidCounter = invalidCounter + 1

print(len(allDicts))
print(validCounter)
print(invalidCounter + validCounter)