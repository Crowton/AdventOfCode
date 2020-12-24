with open("Day24.in") as f:
    tileFlips = f.read().split("\n")


# Part 1
black = set()
for flip in tileFlips:
    at = (0, 0)
    i = 0
    while i < len(flip):
        if flip[i] == "w":
            at = (at[0] - 1, at[1])
        elif flip[i] == "e":
            at = (at[0] + 1, at[1])
        elif flip[i] == "n":
            at = (at[0], at[1] + 1)
            if flip[i + 1] == "e":
                at = (at[0] + 1, at[1])
            i += 1
        else:
            at = (at[0], at[1] - 1)
            if flip[i + 1] == "w":
                at = (at[0] - 1, at[1])
            i += 1
        i += 1

    if at in black:
        black.remove(at)
    else:
        black.add(at)

print(len(black))


# Part 2
for _ in range(100):
    neighbourCount = {}
    for x, y in black:
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (-1, -1)]:
            n = (x + dx, y + dy)
            if n not in neighbourCount:
                neighbourCount[n] = 0
            neighbourCount[n] += 1

    toFlip = set()
    for tile in black:
        if tile not in neighbourCount:
            toFlip.add(tile)

    for tile, count in neighbourCount.items():
        if tile in black and count > 2:
            toFlip.add(tile)
        elif tile not in black and count == 2:
            toFlip.add(tile)

    for tile in toFlip:
        if tile in black:
            black.remove(tile)
        else:
            black.add(tile)

print(len(black))





