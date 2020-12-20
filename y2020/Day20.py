with open("Day20.in") as f:
    tileData = f.read().split("\n\n")
    tiles = []
    for t in tileData:
        dat = t.split("\n")
        tiles.append((int(dat[0][5:-1]), dat[1:]))


# Timing
import time
start = time.time()


# Part 1
def getSides(tileData):
    return [
        tileData[0],
        "".join([tileData[i][-1] for i in range(len(tileData))]),
        tileData[-1][::-1],
        "".join([tileData[i][0] for i in reversed(range(len(tileData)))])
    ]


def permutateSides(sides):
    for _ in range(4):
        yield sides
        sides = [sides[-1]] + sides[:-1]
    for i in range(4):
        sides[i] = sides[i][::-1]
    sides[1], sides[3] = sides[3], sides[1]
    for _ in range(4):
        yield sides
        sides = [sides[-1]] + sides[:-1]


tileBorders = [(name, getSides(rawTile)) for name, rawTile in tiles]

matchSide = {id: set() for id, _ in tileBorders}
for i, (id, sides) in enumerate(tileBorders):
    for idO, sidesO in tileBorders[i + 1:]:
        for sidesPerm in permutateSides(sides):
            for si, s in enumerate(sidesPerm):
                iO = (si + 2) % 4
                if s == sidesO[iO]:
                    matchSide[id].add(idO)
                    matchSide[idO].add(id)
cornersMult = 1
for k, v in matchSide.items():
    if len(v) == 2:
        cornersMult *= k
print(cornersMult)


# Part 2
tileMapping = {id: sides for id, sides in tileBorders}
corner = next(k for k, v in matchSide.items() if len(v) == 2)
sidePiece = next(s for s in matchSide[corner])
order = [[corner, sidePiece]]
puzzle = [[]]

# Find first 2 pieces
loopData = ((c, a)
            for c in permutateSides(tileMapping[corner])
            for a in permutateSides(tileMapping[sidePiece]))
for cornerSidePerm, sidesPiecePerm in loopData:
    if cornerSidePerm[1] == sidesPiecePerm[3][::-1]:
        puzzle[0].append(cornerSidePerm)
        puzzle[0].append(sidesPiecePerm)
        break

# Find first row
sideLen = int(len(tileBorders) ** 0.5)
for col in range(2, sideLen):
    end = False
    for nextTile in matchSide[order[0][col - 1]]:
        for sidesPerm in permutateSides(tileMapping[nextTile]):
            if puzzle[0][col - 1][1] == sidesPerm[3][::-1]:
                order[0].append(nextTile)
                puzzle[0].append(sidesPerm)
                end = True
                break
        if end:
            break

# Find rest
for row in range(1, sideLen):
    order.append([])
    puzzle.append([])
    for col in range(sideLen):
        aboveNeigh = {order[row-1+dr][col+dc] for dc, dr in [(0, -1), (-1, 0), (1, 0)] if 0 <= row-1+dr < sideLen and 0 <= col+dc < sideLen}
        nextTile = next(t for t in matchSide[order[row - 1][col]] if t not in aboveNeigh)
        order[row].append(nextTile)
        for sidesPerm in permutateSides(tileMapping[nextTile]):
            if puzzle[row - 1][col][2][::-1] == sidesPerm[0]:
                if col == 0 or puzzle[row][col - 1][1] == sidesPerm[3][::-1]:
                    puzzle[row].append(sidesPerm)
                    break


def permutateWholeTile(tileData):
    for _ in range(2):
        for _ in range(4):
            yield tileData
            tileData = [
                "".join([tileData[j][i] for j in reversed(range(len(tileData)))])
                for i in range(len(tileData))
            ]
        tileData = [s[::-1] for s in tileData]


def getCenter(tileData):
    return [tileData[i][1:-1] for i in range(1, len(tileData) - 1)]


# Collect center data
wholeTileMapping = {id: tileData for id, tileData in tiles}
completePuzzle = []
for row in range(sideLen):
    completePuzzle.append([])
    for col in range(sideLen):
        for wholePerm in permutateWholeTile(wholeTileMapping[order[row][col]]):
            if getSides(wholePerm) == puzzle[row][col]:
                completePuzzle[-1].append(getCenter(wholePerm))
                break

fullPuzzle = []
for row in completePuzzle:
    for innerRow in zip(*row):
        fullPuzzle.append("".join(innerRow))

# Locate monsters
seamonster = ["                  # ",
              "#    ##    ##    ###",
              " #  #  #  #  #  #   "]
totalHash = sum(r.count("#") for r in fullPuzzle)
for puzzlePerm in permutateWholeTile(fullPuzzle):
    isMonster = set()
    for row in range(len(puzzlePerm) - len(seamonster) + 1):
        for col in range(len(puzzlePerm[row]) - len(seamonster[0]) + 1):
            if all(puzzlePerm[row + j][col + i] == "#" for i in range(len(seamonster[0])) for j in range(len(seamonster)) if seamonster[j][i] == "#"):
                isMonster.update((row + j, col + i) for i in range(len(seamonster[0])) for j in range(len(seamonster)) if seamonster[j][i] == "#")
    if len(isMonster) > 0:
        print(totalHash - len(isMonster))

# Final Timing
print(time.time() - start)
