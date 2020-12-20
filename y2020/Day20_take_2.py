with open("Day20.in") as f:
    tileData = f.read().split("\n\n")
    tiles = []
    for t in tileData:
        dat = t.split("\n")
        tiles.append((int(dat[0][5:-1]), dat[1:]))


# Timing
import time
start = time.time()


def permutateWholeTile(tileData):
    for _ in range(2):
        for _ in range(4):
            yield tileData
            tileData = [
                "".join([tileData[j][i] for j in reversed(range(len(tileData)))])
                for i in range(len(tileData))
            ]
        tileData = [s[::-1] for s in tileData]


def getSides(tileData):
    return [
        tileData[0],
        "".join([tileData[i][-1] for i in range(len(tileData))]),
        tileData[-1],
        "".join([tileData[i][0] for i in range(len(tileData))])
    ]


def getCenter(tileData):
    return [tileData[i][1:-1] for i in range(1, len(tileData) - 1)]


# Build using inline dfs
ids = {(0, 0): tiles[0][0]}
usedIds = {tiles[0][0]}
tilesPlace = {(0, 0): tiles[0][1]}
work = [(1, 0), (-1, 0), (0, 1), (0, -1)]
seen = {(0, 0)}
while work:
    x, y = work.pop()
    if (x, y) not in seen:
        seen.add((x, y))
        tileGen = ((id, tilePerm) for id, tileData in tiles if id not in usedIds for tilePerm in permutateWholeTile(tileData))
        for id, tilePerm in tileGen:
            sides = getSides(tilePerm)
            for d, dx, dy in [(1, 1, 0), (3, -1, 0), (2, 0, 1), (0, 0, -1)]:
                nx, ny = x + dx, y + dy
                if (nx, ny) in tilesPlace and sides[d] != getSides(tilesPlace[(nx, ny)])[(d + 2) % 4]:
                    break
            else:
                ids[(x, y)] = id
                usedIds.add(id)
                tilesPlace[(x, y)] = tilePerm
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    work.append((x + dx, y + dy))
                break

# Part 1
topX = max(x for x, _ in ids)
botX = min(x for x, _ in ids)
topY = max(y for _, y in ids)
botY = min(y for _, y in ids)
print(ids[(topX, topY)] * ids[(topX, botY)] * ids[(botX, topY)] * ids[(botX, botY)])


# Part 2
# Construct puzzle
completePuzzle = [
    [getCenter(tilesPlace[(i, j)]) for i in range(botX, topX + 1)]
    for j in range(botY, topY + 1)
]
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
            if all(puzzlePerm[row + j][col + i] == "#" for i in range(len(seamonster[0])) for j in
                   range(len(seamonster)) if seamonster[j][i] == "#"):
                isMonster.update(
                    (row + j, col + i) for i in range(len(seamonster[0])) for j in range(len(seamonster)) if
                    seamonster[j][i] == "#")
    if len(isMonster) > 0:
        print(totalHash - len(isMonster))

# Final Time
print(time.time() - start)
