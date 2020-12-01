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


# programInit = list(map(int, input().split(",")))
# s = 0
#
# for y in range(50):
#     for x in range(50):
#         program = [p for p in programInit]
#         inputs = [x, y]
#         rel = 0
#         i = 0
#         while i < len(program):
#             code = str(program[i])
#             code = "0" * (5 - len(code)) + code
#             if code[3:5] == "01":
#                 a = getArg(i + 1, code[2], program, rel)
#                 b = getArg(i + 2, code[1], program, rel)
#                 setData(i+3, code[0], a+b, program, rel)
#                 i += 4
#             elif code[3:5] == "02":
#                 a = getArg(i + 1, code[2], program, rel)
#                 b = getArg(i + 2, code[1], program, rel)
#                 setData(i+3, code[0], a*b, program, rel)
#                 i += 4
#             elif code[3:5] == "03":
#                 d = inputs[0]
#                 inputs = inputs[1:]
#                 setData(i+1, code[2], d, program, rel)
#                 i += 2
#             elif code[3:5] == "04":
#                 d = getArg(i + 1, code[2], program, rel)
#                 s += d
#                 if d == 0:
#                     print(".", end="")
#                 else:
#                     print("#", end="")
#                 i += 2
#             elif code[3:5] == "05":
#                 a = getArg(i + 1, code[2], program, rel)
#                 i = getArg(i + 2, code[1], program, rel) if a != 0 else i + 3
#             elif code[3:5] == "06":
#                 a = getArg(i + 1, code[2], program, rel)
#                 i = getArg(i + 2, code[1], program, rel) if a == 0 else i + 3
#             elif code[3:5] == "07":
#                 a = getArg(i + 1, code[2], program, rel)
#                 b = getArg(i + 2, code[1], program, rel)
#                 setData(i+3, code[0], 1 if a < b else 0, program, rel)
#                 i += 4
#             elif code[3:5] == "08":
#                 a = getArg(i + 1, code[2], program, rel)
#                 b = getArg(i + 2, code[1], program, rel)
#                 setData(i+3, code[0], 1 if a == b else 0, program, rel)
#                 i += 4
#             elif code[3:5] == "09":
#                 rel += getArg(i+1, code[2], program, rel)
#                 i += 2
#             elif code[3:5] == "99":
#                 break
#             else:
#                 print("PANIC!", code, i)
#                 break
#     print()
#
# print(s)

programInit = list(map(int, input().split(",")))
tractor = set()
x, y = 4, 5
rowSeen = False
rowX = 4

end = False
c = 0
while not end:
    c += 1
    if c % 1000 == 0:
        print(x, y)
    program = [p for p in programInit]
    inputs = [x, y]
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
            d = inputs[0]
            inputs = inputs[1:]
            setData(i+1, code[2], d, program, rel)
            i += 2
        elif code[3:5] == "04":
            d = getArg(i + 1, code[2], program, rel)
            if d == 1:
                tractor.add((x, y))
                if (x-99, y) in tractor and (x, y-99) in tractor and (x-99, y-99) in tractor:
                    print((x-99)*10000 + y-99)
                    end = True
                if not rowSeen:
                    rowX = x
                    rowSeen = True
                x += 1
            elif rowSeen:
                rowSeen = False
                x = rowX
                y += 1
            else:
                x += 1
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


# 8821063 too high

# 8831064 too high


# programInit = list(map(int, input().split(",")))
# tractor = set()
# x, y = 1000, 1200
#
# dir = [(-1, 0), (0, -1), (-1, -1)]
# test = 0
# fails = 0
#
# while True:
#     success = True
#     for checkX, checkY in [(100, 0), (0, 100)]:
#         program = [p for p in programInit]
#         inputs = [x + checkX + dir[test][0], y + checkY + dir[test][1]]
#         rel = 0
#         i = 0
#         while i < len(program):
#             code = str(program[i])
#             code = "0" * (5 - len(code)) + code
#             if code[3:5] == "01":
#                 a = getArg(i + 1, code[2], program, rel)
#                 b = getArg(i + 2, code[1], program, rel)
#                 setData(i+3, code[0], a+b, program, rel)
#                 i += 4
#             elif code[3:5] == "02":
#                 a = getArg(i + 1, code[2], program, rel)
#                 b = getArg(i + 2, code[1], program, rel)
#                 setData(i+3, code[0], a*b, program, rel)
#                 i += 4
#             elif code[3:5] == "03":
#                 d = inputs[0]
#                 inputs = inputs[1:]
#                 setData(i+1, code[2], d, program, rel)
#                 i += 2
#             elif code[3:5] == "04":
#                 d = getArg(i + 1, code[2], program, rel)
#                 if d == 0:
#                     success = False
#                 i += 2
#             elif code[3:5] == "05":
#                 a = getArg(i + 1, code[2], program, rel)
#                 i = getArg(i + 2, code[1], program, rel) if a != 0 else i + 3
#             elif code[3:5] == "06":
#                 a = getArg(i + 1, code[2], program, rel)
#                 i = getArg(i + 2, code[1], program, rel) if a == 0 else i + 3
#             elif code[3:5] == "07":
#                 a = getArg(i + 1, code[2], program, rel)
#                 b = getArg(i + 2, code[1], program, rel)
#                 setData(i+3, code[0], 1 if a < b else 0, program, rel)
#                 i += 4
#             elif code[3:5] == "08":
#                 a = getArg(i + 1, code[2], program, rel)
#                 b = getArg(i + 2, code[1], program, rel)
#                 setData(i+3, code[0], 1 if a == b else 0, program, rel)
#                 i += 4
#             elif code[3:5] == "09":
#                 rel += getArg(i+1, code[2], program, rel)
#                 i += 2
#             elif code[3:5] == "99":
#                 break
#             else:
#                 print("PANIC!", code, i)
#                 break
#
#     if not success:
#         test = 1 - test
#         fails += 1
#         if fails == 2:
#             test = 2
#     else:
#         x += dir[test][0]
#         y += dir[test][1]
#         test = 0
#         print(x*10000 + y)

