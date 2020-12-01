gridSerial = 5791

# powerlevels = [[0] * 300 for i in range(300)]
powerlevels = [[0] * 301 for i in range(301)]

for x in range(300):
    for y in range(300):
        rackID = x + 10
        powerLevelStart = rackID * y
        addingSerial = powerLevelStart + gridSerial
        multRackID = addingSerial * rackID
        hundredsDigit = int((multRackID % 1000) / 100)
        subFive = hundredsDigit - 5

        # powerlevels[x][y] = subFive
        powerlevels[x+1][y+1] = subFive

best = 0
at = ""

# for x in range(300-2):
#     for y in range(300-2):
#         s = 0
#         for xx in range(x, x+3):
#             for yy in range(y, y+3):
#                 s += powerlevels[xx][yy]
#
#         if s > best:
#             best = s
#             at = str(x) + "," + str(y)

for x in range(300):
    for y in range(300):
        powerlevels[x+1][y+1] += powerlevels[x][y+1] + powerlevels[x+1][y] - powerlevels[x][y]

for x in range(300):
    for y in range(300):
        size = 1
        while x+size < 301 and y+size < 301:
            val = powerlevels[x+size][y+size] - powerlevels[x][y+size] - powerlevels[x+size][y] + powerlevels[x][y]
            if val > best:
                best = val
                at = str(x) + "," + str(y) + "," + str(size)
            size += 1

print(at)