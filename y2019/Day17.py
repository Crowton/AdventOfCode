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


# board = set()
# atX = 0
# atY = 0
#
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
#         print("INPUT!")
#         setData(i+1, code[2], 0, program, rel)
#         i += 2
#     elif code[3:5] == "04":
#         d = getArg(i + 1, code[2], program, rel)
#         c = chr(d)
#         if c == "\n":
#             atX = 0
#             atY += 1
#         else:
#             if c in {"#", "^", "v", ">", "<"}:
#                 board.add((atX, atY))
#             elif c != ".":
#                 print("OUTPUT!", c)
#             atX += 1
#         print(c, end="")
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

# print(sum(x * y for x, y in board if all((x+dx, y+dy) in board for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)])))
# s = 0
# for x, y in board:
#     if all((x+dx, y+dy) in board for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]):
#         s += x * y
#         print(x, y)
# print(s)

# 3607 too low


phase = 0
board = set()
atX = 0
atY = 0
duster = (0, 0)
facing = (1, 0)


def computeSeqs(duster, facing):
    # for y in range(35):
    #     for x in range(55):
    #         if (x, y) in board:
    #             print("#", end="")
    #         else:
    #             print(" ", end="")
    #     print()
    
    turnLeft = {
        (0, 1) : (-1, 0),
        (0, -1): (1, 0),
        (1, 0) : (0, 1),
        (-1, 0): (0, -1),
    }
    m = 0
    seq = []
    while True:
        if (duster[0] + facing[0], duster[1] + facing[1]) not in board:
            seq.append(m)
            m = 0
            left = turnLeft[facing]
            if (duster[0] + left[0], duster[1] + left[1]) in board:
                print("R", facing, left)
                facing = left
                seq.append("R")
            else:
                right = turnLeft[turnLeft[turnLeft[facing]]]
                if (duster[0] + right[0], duster[1] + right[1]) in board:
                    print("L", facing, right)
                    facing = right
                    seq.append("L")
                else:
                    break
        else:
            m += 1
            duster = (duster[0] + facing[0], duster[1] + facing[1])
    
    seq.pop(0)
    # print(seq)
    print(','.join([str(s) for s in seq]))
    revMeans = {}
    means = {}
    nextSym = "A"
    newSeq = []
    for i in range(0, len(seq), 2):
        if (seq[i], seq[i+1]) in revMeans:
            newSeq.append(revMeans[(seq[i], seq[i+1])])
        else:
            revMeans[(seq[i], seq[i+1])] = nextSym
            means[nextSym] = [seq[i], seq[i+1]]
            newSeq.append(nextSym)
            nextSym = chr(ord(nextSym) + 1)
    print(''.join(newSeq))
    
    best = "ABACBCBCAC"
    revrev = {
        "A": "ABB",
        "B": "CDA",
        "C": "DAEC"
    }
    
    main = ','.join(best) + "\n"
    A = ','.join([str(y) for x in revrev["A"] for y in means[x]]) + "\n"
    B = ','.join([str(y) for x in revrev["B"] for y in means[x]]) + "\n"
    C = ','.join([str(y) for x in revrev["C"] for y in means[x]]) + "\n"
    print(main + A + B + C + "n\n")
    return main + A + B + C + "n\n"
    


program = list(map(int, input().split(",")))
program[0] = 2
inputs = ""
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
        d = ord(inputs[0])
        inputs = inputs[1:]
        setData(i+1, code[2], d, program, rel)
        i += 2
    elif code[3:5] == "04":
        d = getArg(i + 1, code[2], program, rel)
        c = chr(d)
        if phase == 0:
            if c == "M":
                phase = 1
                inputs = computeSeqs(duster, facing)
            elif c == "\n":
                atX = 0
                atY += 1
            else:
                if c in {"#", "^", "v", ">", "<"}:
                    board.add((atX, atY))
                    if c in {"^", "v", ">", "<"}:
                        duster = (atX, atY)
                        facing = {
                            "^": (0, -1), "v": (0, 1), ">": (1, 0), "<": (-1, 0),
                        }[c]
                atX += 1
        print(c, end="")
        if d >= 256:
            print(d)
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