with open("Day16.in") as f:
    types = []
    typesNames = []
    data = f.readlines()
    i = 0
    while data[i] != "\n":
        name, ranges = data[i].split(": ")
        typesNames.append(name)
        rangeData = []
        for r in ranges.split(" or "):
            f, t = map(int, r.split("-"))
            rangeData.append((f, t))
        types.append(rangeData)
        i += 1
    i += 2
    myTicket = list(map(int, data[i].split(",")))
    i += 3
    otherTickets = []
    while i < len(data):
        otherTickets.append(list(map(int, data[i].split(","))))
        i += 1

# Part 1
invalidSum = 0
invalidTickets = set()
for i, ticket in enumerate(otherTickets):
    for val in ticket:
        if all(not any(f <= val <= t for f, t in field) for field in types):
            invalidSum += val
            invalidTickets.add(i)
print(invalidSum)


# Part 2
# Get valid tickets and setup possible fields
validOtherTickets = [t for i, t in enumerate(otherTickets) if i not in invalidTickets]
canBe = [set(range(len(types))) for _ in range(len(types))]

# Invalidate fields
for ticket in validOtherTickets:
    for valIndex, val in enumerate(ticket):
        toRemove = set()
        for fieldNumber in canBe[valIndex]:
            if not any(f <= val <= t for f, t in types[fieldNumber]):
                toRemove.add(fieldNumber)
        canBe[valIndex] = canBe[valIndex].difference(toRemove)

# Clean fields, assuming that any set is always a singleton
# This element can then be removed from the rest
assert all(len(s) >= 1 for s in canBe)
while any(len(s) > 1 for s in canBe):
    for i, s in enumerate(canBe):
        if len(s) == 1:
            elm = next(e for e in s)
            for j, s2 in enumerate(canBe):
                if i != j and elm in s2:
                    s2.remove(elm)

# Calculate departure product
totalDeparture = 1
for i, val in enumerate(myTicket):
    fieldName = typesNames[next(e for e in canBe[i])]
    if fieldName[:9] == "departure":
        totalDeparture *= val
print(totalDeparture)
