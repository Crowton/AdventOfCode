import random

def getArg(loc, mode, program, rel):
    a = program[loc]
    if mode == "0":
        a = 0 if a >= len(program) else program[a]
    if mode == "2":
        a = 0 if a+rel >= len(program) else program[a+rel]
    return a


def setData(loc, mode, data, program, rel):
    a = program[loc]
    if mode == "0":
        while a >= len(program):
            program.append(0)
        program[a] = data
    elif mode == "2":
        while a+rel >= len(program):
            program.append(0)
        program[a+rel] = data

droid = (0, 0)
board = {droid: "."}

def redraw():
    minX = min(x for x, y in board)
    maxX = max(x for x, y in board)
    minY = min(y for x, y in board)
    maxY = max(y for x, y in board)
    
    for y in reversed(range(minY-1, maxY+2)):
        for x in range(minX-1, maxX+2):
            d = " "
            if (x, y) in board:
                d = board[(x, y)]
            if (x, y) == droid:
                d = "D"
            print(d, end="")
        print()
    print()


convertToCode = {
    "w": 1,
    "s": 2,
    "a": 3,
    "d": 4
}
convertToDir = {
    "w": (0, 1),
    "s": (0, -1),
    "a": (-1, 0),
    "d": (1, 0)
}
lastMove = "w"


# program = list(map(int, input().split(",")))
# rel = 0
# i = 0
# while i < len(program):
#     code = str(program[i])
#     code = "0" * (5 - len(code)) + code
#     if code[3:5] == "01":
#         a = getArg(i + 1, code[2], program, rel)
#         b = getArg(i + 2, code[1], program, rel)
#         setData(i+3, code[0], a+b, program, rel)
#         i += 4
#     elif code[3:5] == "02":
#         a = getArg(i + 1, code[2], program, rel)
#         b = getArg(i + 2, code[1], program, rel)
#         setData(i+3, code[0], a*b, program, rel)
#         i += 4
#     elif code[3:5] == "03":
#         # redraw()
#         # lastMove = input("Dir: ")
#         lastMove = "wasd"[random.randint(0, 3)]
#         d = convertToCode[lastMove]
#         setData(i+1, code[2], d, program, rel)
#         i += 2
#     elif code[3:5] == "04":
#         d = getArg(i + 1, code[2], program, rel)
#         if d == 0:
#             moved = convertToDir[lastMove]
#             board[(droid[0] + moved[0], droid[1] + moved[1])] = "#"
#         elif d == 1:
#             moved = convertToDir[lastMove]
#             droid = (droid[0] + moved[0], droid[1] + moved[1])
#             board[droid] = "."
#         elif d == 2:
#             moved = convertToDir[lastMove]
#             droid = (droid[0] + moved[0], droid[1] + moved[1])
#             print("Found end!")
#             break
#         i += 2
#     elif code[3:5] == "05":
#         a = getArg(i + 1, code[2], program, rel)
#         i = getArg(i + 2, code[1], program, rel) if a != 0 else i + 3
#     elif code[3:5] == "06":
#         a = getArg(i + 1, code[2], program, rel)
#         i = getArg(i + 2, code[1], program, rel) if a == 0 else i + 3
#     elif code[3:5] == "07":
#         a = getArg(i + 1, code[2], program, rel)
#         b = getArg(i + 2, code[1], program, rel)
#         setData(i+3, code[0], 1 if a < b else 0, program, rel)
#         i += 4
#     elif code[3:5] == "08":
#         a = getArg(i + 1, code[2], program, rel)
#         b = getArg(i + 2, code[1], program, rel)
#         setData(i+3, code[0], 1 if a == b else 0, program, rel)
#         i += 4
#     elif code[3:5] == "09":
#         rel += getArg(i+1, code[2], program, rel)
#         i += 2
#     elif code[3:5] == "99":
#         break
#     else:
#         print("PANIC!", code, i)
#         break
#
# redraw()
#
# queue = [(0, (0, 0))]
# seen = set()
# while queue:
#     d, space = queue.pop(0)
#     if space == droid:
#         print(d)
#         break
#     if space not in seen and space in board and board[space] != "#":
#         seen.add(space)
#         for m in "wasd":
#             dir = convertToDir[m]
#             queue.append((d+1, (space[0] + dir[0], space[1] + dir[1])))

# 265 too low

def findNewMoves():
    poi = set()
    for s in board:
        if board[s] == "." and any((s[0] + convertToDir[m][0], s[1] + convertToDir[m][1]) not in board for m in "wasd"):
            poi.add(s)
    print(len(poi))
    
    if len(poi) == 0:
        return []
    
    queue = [droid]
    seen = {droid: ("", droid)}
    inverse = {
        "w": "s", "s": "w",
        "a": "d", "d": "a"
    }
    last = droid
    while queue:
        space = queue.pop(0)
        if space in poi:
            last = space
            break
        for m in "wasd":
            dir = convertToDir[m]
            newSpace = (space[0] + dir[0], space[1] + dir[1])
            if newSpace not in seen and newSpace in board and board[newSpace] != "#":
                queue.append(newSpace)
                seen[newSpace] = (m, space)
    
    result = []
    space = last
    for m in "wasd":
        dir = convertToDir[m]
        if (space[0] + dir[0], space[1] + dir[1]) not in board:
            result.append(m)
            break
    while True:
        d, space = seen[space]
        if d == "":
            break
        result.append(d)
    return result


poi = {droid}
oxygen = (0, 0)
moveSeq = []

program = list(map(int, input().split(",")))
rel = 0
i = 0
while i < len(program):
    code = str(program[i])
    code = "0" * (5 - len(code)) + code
    if code[3:5] == "01":
        a = getArg(i + 1, code[2], program, rel)
        b = getArg(i + 2, code[1], program, rel)
        setData(i+3, code[0], a+b, program, rel)
        i += 4
    elif code[3:5] == "02":
        a = getArg(i + 1, code[2], program, rel)
        b = getArg(i + 2, code[1], program, rel)
        setData(i+3, code[0], a*b, program, rel)
        i += 4
    elif code[3:5] == "03":
        if not moveSeq:
            moveSeq = findNewMoves()
            # redraw()
            if not moveSeq:
                break
        lastMove = moveSeq.pop()
        d = convertToCode[lastMove]
        setData(i+1, code[2], d, program, rel)
        i += 2
    elif code[3:5] == "04":
        d = getArg(i + 1, code[2], program, rel)
        if d == 0:
            moved = convertToDir[lastMove]
            board[(droid[0] + moved[0], droid[1] + moved[1])] = "#"
        elif d == 1:
            moved = convertToDir[lastMove]
            droid = (droid[0] + moved[0], droid[1] + moved[1])
            board[droid] = "."
        elif d == 2:
            moved = convertToDir[lastMove]
            droid = (droid[0] + moved[0], droid[1] + moved[1])
            board[droid] = "."
            oxygen = droid
        i += 2
    elif code[3:5] == "05":
        a = getArg(i + 1, code[2], program, rel)
        i = getArg(i + 2, code[1], program, rel) if a != 0 else i + 3
    elif code[3:5] == "06":
        a = getArg(i + 1, code[2], program, rel)
        i = getArg(i + 2, code[1], program, rel) if a == 0 else i + 3
    elif code[3:5] == "07":
        a = getArg(i + 1, code[2], program, rel)
        b = getArg(i + 2, code[1], program, rel)
        setData(i+3, code[0], 1 if a < b else 0, program, rel)
        i += 4
    elif code[3:5] == "08":
        a = getArg(i + 1, code[2], program, rel)
        b = getArg(i + 2, code[1], program, rel)
        setData(i+3, code[0], 1 if a == b else 0, program, rel)
        i += 4
    elif code[3:5] == "09":
        rel += getArg(i+1, code[2], program, rel)
        i += 2
    elif code[3:5] == "99":
        break
    else:
        print("PANIC!", code, i)
        break

queue = [(0, oxygen)]
seen = set()
bestDist = 0
while queue:
    d, space = queue.pop(0)
    if space not in seen and board[space] == ".":
        seen.add(space)
        bestDist = d
        for m in "wasd":
            dir = convertToDir[m]
            queue.append((d+1, (space[0] + dir[0], space[1] + dir[1])))

redraw()
print(bestDist)
# 275 too high
# 274 is right
