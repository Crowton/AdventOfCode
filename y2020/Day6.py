# Part 1
# totalYes = 0
# currentYes = set()
#
# while True:
#     line = input()
#     if line == "-1":
#         break
#     elif line == "":
#         totalYes += len(currentYes)
#         currentYes = set()
#     else:
#         currentYes = currentYes.union({s for s in line})
#
# print(totalYes)


# Part 2
totalYes = 0
currentYes = None

while True:
    line = input()
    if line == "-1":
        break
    elif line == "":
        totalYes += len(currentYes) if currentYes is not None else 0
        currentYes = None
    else:
        if currentYes is None:
            currentYes = {s for s in line}
        else:
            currentYes = currentYes.intersection({s for s in line})

print(totalYes)
