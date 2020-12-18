with open("Day17.in") as f:
    data = f.readlines()

    active = set()
    for i, line in enumerate(data):
        for j, c in enumerate(line[:-1]):
            if c == "#":
                active.add((i, j, 0))

    active4d = set()
    for i, line in enumerate(data):
        for j, c in enumerate(line[:-1]):
            if c == "#":
                active4d.add((i, j, 0, 0))

# Part 1
for _ in range(6):
    newActive = set()
    newInActive = set()

    toProcess = set()
    for x, y, z in active:
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                for dz in range(-1, 2):
                    toProcess.add((x + dx, y + dy, z + dz))

    for x, y, z in toProcess:
        activeNeigh = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                for dz in range(-1, 2):
                    if dx == dy == dz == 0:
                        continue
                    if (x + dx, y + dy, z + dz) in active:
                        activeNeigh += 1
        if (x, y, z) in active and not (2 <= activeNeigh <= 3):
            newInActive.add((x, y, z))
        elif (x, y, z) not in active and activeNeigh == 3:
            newActive.add((x, y, z))

    active = active.difference(newInActive)
    active = active.union(newActive)

print(len(active))


# Part 2
for _ in range(6):
    newActive = set()
    newInActive = set()

    toProcess = {}
    for x, y, z, w in active4d:
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                for dz in range(-1, 2):
                    for dw in range(-1, 2):
                        cube = (x + dx, y + dy, z + dz, w + dw)
                        if cube not in toProcess:
                            toProcess[cube] = 0
                        toProcess[cube] += 1

    for cube in toProcess:
        activeNeigh = toProcess[cube] - (cube in active4d)
        if cube in active4d and not (2 <= activeNeigh <= 3):
            newInActive.add(cube)
        elif cube not in active4d and activeNeigh == 3:
            newActive.add(cube)

    active4d = active4d.difference(newInActive)
    active4d = active4d.union(newActive)

print(len(active4d))
