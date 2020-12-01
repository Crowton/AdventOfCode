def getArg(loc, mode, program, rel):
    a = program[loc]
    if mode == "0":
        a = 0 if a >= len(program) else program[a]
    if mode == "2":
        a = a = 0 if a+rel >= len(program) else program[a+rel]
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


# data = []
# board = {}
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
#         print("INPUT!?")
#         setData(i+1, code[2], 0, program, rel)
#         i += 2
#     elif code[3:5] == "04":
#         d = getArg(i + 1, code[2], program, rel)
#         data.append(d)
#         if len(data) == 3:
#             board[(data[0], data[1])] = data[2]
#             data = []
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
# s = 0
# for b in board:
#     if board[b] == 2:
#         s += 1
# print(s)

data = []
board = {}

def redraw():
    minX = min(x for x, y in board)
    maxX = max(x for x, y in board)
    minY = min(y for x, y in board)
    maxY = max(y for x, y in board)
    
    for y in range(minY-1, maxY+2):
        for x in range(minX-1, maxX+2):
            d = " "
            if (x, y) in board:
                if board[(x, y)] == 1:
                    d = "#"
                if board[(x, y)] == 2:
                    d = "."
                if board[(x, y)] == 3:
                    d = "-"
                if board[(x, y)] == 4:
                    d = "o"
            print(d, end="")
        print()
    print()


program = list(map(int, input().split(",")))
program[0] = 2
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
        # redraw()
        # input()
        s = 0
        for b in board:
            if board[b] == 2:
                s += 1
        print(s)
        # d = int(input("Dir: "))
        d = 0 if ballX == paddleX else -1 if ballX < paddleX else 1
        setData(i+1, code[2], d, program, rel)
        i += 2
    elif code[3:5] == "04":
        d = getArg(i + 1, code[2], program, rel)
        data.append(d)
        if len(data) == 3:
            if data[0] == -1 and data[1] == 0:
                score = data[2]
            else:
                board[(data[0], data[1])] = data[2]
                if data[2] == 3:
                    paddleX = data[0]
                elif data[2] == 4:
                    ballX = data[0]
            data = []
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

print(score)
