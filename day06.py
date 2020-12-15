import re
allGroups = []
groupDict = {}
answerCount = 0
allAnswerCount = 0
groupSize = 0

with open("day6_input.txt", "r") as a_file:
    for line in a_file:
      stripped_line = line.strip()
      if stripped_line == "":
          for key, value in groupDict.items():
              if value == groupSize:
                  allAnswerCount = allAnswerCount + 1
          answerCount = len(groupDict) + answerCount
          allGroups.append(groupDict)
          groupDict = dict()
          groupSize = 0
      if re.match("[a-z]", stripped_line) :
          groupSize = groupSize + 1
          for elem in stripped_line :
              if (elem in groupDict.keys()) == False:
                  groupDict[elem] = 1
              else:
                  groupDict[elem] = 1 + groupDict[elem]

print(answerCount)
print(allAnswerCount)