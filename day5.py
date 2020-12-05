import re
allPasses = []

with open("day5_input.txt", "r") as a_file:
    for line in a_file:
      stripped_line = line.strip()
      if re.match("[B|F|L|R]{10}", stripped_line) :
          stripped_line = re.sub(r"[FL]", "0", stripped_line)
          stripped_line = re.sub(r"[RB]", "1", stripped_line)
          allPasses.append((stripped_line[0:7:],stripped_line[7:10:]))

def binStringtoInt(binary_str):
    num = 0
    for i in range(len(binary_str)):
        num = num * 2
        num = num + int(binary_str[i])
    return num

IDlist =[]

for boardingPass in allPasses:
    ID = binStringtoInt(boardingPass[0])*8+ binStringtoInt(boardingPass[1])
    IDlist.append(ID)
        
IDlist.sort()
print("The highest ID : " + str(IDlist[-1])) 
res = [ele for ele in range(IDlist[0], IDlist[-1]+1) if ele not in IDlist] 
print("The missing ID : " + str(res[0])) 