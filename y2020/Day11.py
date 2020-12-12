with open("Day11.in") as f:
    seats = [[c for c in line[:-1]] for line in f.readlines()]

width, height = len(seats[0]), len(seats)

# Part 1
# Ommitted, as it is slow
# And to preserve seats to part 2
while False:
    updates = []

    for i in range(width):
        for j in range(height):
            if seats[j][i] != ".":
                occupied = 0
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if di == dj == 0:
                            continue
                        ni, nj = i + di, j + dj
                        if 0 <= ni < width and 0 <= nj < height and seats[nj][ni] == "#":
                            occupied += 1
                if seats[j][i] == "L" and occupied == 0:
                    updates.append((i, j, "#"))
                elif seats[j][i] == "#" and occupied >= 4:
                    updates.append((i, j, "L"))

    if updates:
        for i, j, c in updates:
            seats[j][i] = c
    else:
        break

count = 0
for i in range(width):
    for j in range(height):
        if seats[j][i] == "#":
            count += 1
print(count)
# prints 2438


# Part 2
sees = {}
for i in range(width):
    for j in range(height):
        sees[(i, j)] = []
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if di == dj == 0:
                    continue
                dis = 1
                while 0 <= i + di * dis < width and 0 <= j + dj * dis < height:
                    if seats[j + dj * dis][i + di * dis] != ".":
                        sees[(i, j)].append((i + di * dis, j + dj * dis))
                        break
                    dis += 1

while True:
    updates = []

    for i in range(width):
        for j in range(height):
            if seats[j][i] != ".":
                occupied = sum(seats[nj][ni] == "#" for ni, nj in sees[(i, j)]) if sees[(i, j)] else 0
                if seats[j][i] == "L" and occupied == 0:
                    updates.append((i, j, "#"))
                elif seats[j][i] == "#" and occupied >= 5:
                    updates.append((i, j, "L"))

    if updates:
        for i, j, c in updates:
            seats[j][i] = c
    else:
        break

count = 0
for i in range(width):
    for j in range(height):
        if seats[j][i] == "#":
            count += 1
print(count)
# prints 2174
