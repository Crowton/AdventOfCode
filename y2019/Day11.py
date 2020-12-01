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


# board = {}
board = {(0, 0): 1}
robot = (0, 0)
rotate = {
    (0, 1): (-1, 0),
    (-1, 0): (0, -1),
    (0, -1): (1, 0),
    (1, 0): (0, 1)
}
facing = (0, 1)
phaseIsPaint = True

program = list(map(int, input().split(",")))
print(len(program))
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
        color = 0  #default black
        if robot in board:
            color = board[robot]
        setData(i+1, code[2], color, program, rel)
        i += 2
    elif code[3:5] == "04":
        data = getArg(i + 1, code[2], program, rel)
        if phaseIsPaint:
            board[robot] = data
        else:
            facing = rotate[facing]
            if data == 1:
                facing = rotate[facing]
                facing = rotate[facing]
            robot = (robot[0] + facing[0], robot[1] + facing[1])
        phaseIsPaint = not phaseIsPaint
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

print(len(board))
# 9275 too high

minX = min(x for x, y in board)
maxX = max(x for x, y in board)
minY = min(y for x, y in board)
maxY = max(y for x, y in board)

for y in reversed(range(minY-1, maxY+2)):
    for x in range(minX-1, maxX+2):
        d = " "
        if (x, y) in board:
            if board[(x, y)] == 1:
                d = "#"
        print(d, end="")
    print()

# RPJCFZKF
