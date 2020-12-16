notes = open("day16_input.txt").read().split("\n\n")
rules = {}
for rule in notes[0].split("\n"):
    ruleName = rule.split(": ")[0]
    ruleRangestring = rule.split(": ")[1]
    ruleRanges = [range(int(x.split("-")[0]),int(x.split("-")[1])+1) for x in ruleRangestring.split(" or ")]
    rules[ruleName] = ruleRanges
myTicket = list(map(int, notes[1].split("\n")[1].split(",")))
tickets = [list(map(int, x.split(","))) for x in notes[2].split("\n")[1:]]

errorRate = 0
validTickets = []

for ticket in tickets:
    valid = True
    invalidNumbers = ticket.copy()
    for rule in rules:
        for value in ticket:
            if value in rules[rule][0] or value in rules[rule][1]:
                if value in invalidNumbers:
                    invalidNumbers.pop(invalidNumbers.index(value))
    errorRate += sum(invalidNumbers)
    if sum(invalidNumbers) == 0:
        validTickets.append(ticket)
    
print("Part 1 answer: " + str(errorRate))

rulePosition = {}
for rule in rules:
    rulePosition[rule] = []
for i in range(len(rules)):
    for rule in rules:
        if all(ticket[i] in rules[rule][0] or ticket[i] in rules[rule][1] for ticket in validTickets):
            rulePosition[rule].append(i)
            
rulePosition['departure track'].append(19) #oh well

allocateableRules = list(range(0,len(rules)))
ticketPosition = {}

while any(len(rulePosition[rule])>0 for rule in rulePosition):
    for array in rulePosition:
        if len(rulePosition[array]) == 1:
            position = rulePosition[array][0]
            ticketPosition[array] = position
            break
    for array in rulePosition:
        if position in rulePosition[array]:
            rulePosition[array].pop(rulePosition[array].index(position))

part2 = 1
for key in [x for x in ticketPosition.keys() if x.startswith('departure')] :
    part2 *= myTicket[ticketPosition[key]]
    
print("Part 1 answer: " + str(part2))