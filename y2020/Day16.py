with open("Day16.in") as f:
    fieldsData, myData, otherData = f.read().split("\n\n")

    types = []
    typesNames = []
    for field in fieldsData.split("\n"):
        name, ranges = field.split(": ")
        typesNames.append(name)
        types.append([tuple(map(int, r.split("-"))) for r in ranges.split(" or ")])

    myTicket = list(map(int, myData.split("\n")[-1].split(",")))
    otherTickets = [list(map(int, ticket.split(","))) for ticket in otherData.split("\n")[1:]]

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
