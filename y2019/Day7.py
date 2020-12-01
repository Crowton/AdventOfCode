# def getArg(loc, mode, program):
#     a = program[loc]
#     if mode == "0":
#         a = program[a]
#     return a
#
# def run(program, inputs):
#     i = 0
#     while i < len(program):
#         code = str(program[i])
#         code = "0"*(5-len(code)) + code
#         if code[3:5] == "01":
#             a = getArg(i+1, code[2], program)
#             b = getArg(i+2, code[1], program)
#             program[program[i+3]] = a + b
#             i += 4
#         elif code[3:5] == "02":
#             a = getArg(i+1, code[2], program)
#             b = getArg(i+2, code[1], program)
#             program[program[i+3]] = a * b
#             i += 4
#         elif code[3:5] == "03":
#             program[program[i+1]] = inputs.pop()
#             i += 2
#         elif code[3:5] == "04":
#             return getArg(i+1, code[2], program)
#             # i += 2
#         elif code[3:5] == "05":
#             a = getArg(i+1, code[2], program)
#             i = getArg(i+2, code[1], program) if a != 0 else i + 3
#         elif code[3:5] == "06":
#             a = getArg(i+1, code[2], program)
#             i = getArg(i+2, code[1], program) if a == 0 else i + 3
#         elif code[3:5] == "07":
#             a = getArg(i+1, code[2], program)
#             b = getArg(i+2, code[1], program)
#             program[program[i+3]] = 1 if a < b else 0
#             i += 4
#         elif code[3:5] == "08":
#             a = getArg(i+1, code[2], program)
#             b = getArg(i+2, code[1], program)
#             program[program[i+3]] = 1 if a == b else 0
#             i += 4
#         elif code[3:5] == "99":
#             break
#         else:
#             print("PANIC!", code, i)
#             break
#
#
# initprogram = list(map(int, input().split(",")))
# best = 0
# at = 0
# for i in range(44444):
#     strV = str(i)
#     strV = "0"*(5-len(strV)) + strV
#     if len({j for j in strV}) == 5 and max(int(j) for j in strV) == 4:
#         amp = 0
#         for j in range(5):
#             amp = run([p for p in initprogram], [amp, int(strV[j])])
#         if best <= amp:
#             best = amp
#             at = i
#
# print(best, at)

def getArg(loc, mode, program):
    a = program[loc]
    if mode == "0":
        a = program[a]
    return a

def run(program, inputs, i):
    while i < len(program):
        code = str(program[i])
        code = "0"*(5-len(code)) + code
        if code[3:5] == "01":
            a = getArg(i+1, code[2], program)
            b = getArg(i+2, code[1], program)
            program[program[i+3]] = a + b
            i += 4
        elif code[3:5] == "02":
            a = getArg(i+1, code[2], program)
            b = getArg(i+2, code[1], program)
            program[program[i+3]] = a * b
            i += 4
        elif code[3:5] == "03":
            program[program[i+1]] = inputs.pop()
            i += 2
        elif code[3:5] == "04":
            return getArg(i+1, code[2], program), program, i+2
        elif code[3:5] == "05":
            a = getArg(i+1, code[2], program)
            i = getArg(i+2, code[1], program) if a != 0 else i + 3
        elif code[3:5] == "06":
            a = getArg(i+1, code[2], program)
            i = getArg(i+2, code[1], program) if a == 0 else i + 3
        elif code[3:5] == "07":
            a = getArg(i+1, code[2], program)
            b = getArg(i+2, code[1], program)
            program[program[i+3]] = 1 if a < b else 0
            i += 4
        elif code[3:5] == "08":
            a = getArg(i+1, code[2], program)
            b = getArg(i+2, code[1], program)
            program[program[i+3]] = 1 if a == b else 0
            i += 4
        elif code[3:5] == "99":
            return None, None, None
        else:
            print("PANIC!", code, i)
            break


initprogram = list(map(int, input().split(",")))
best = 0
at = 0
for i in range(44444):
    strV = str(i)
    strV = "0"*(5-len(strV)) + strV
    if len({j for j in strV}) == 5 and max(int(j) for j in strV) == 4:
        data = []
        amp = 0
        for j in range(5):
            amp, p, pi = run([p for p in initprogram], [amp, int(strV[j]) + 5], 0)
            data.append((p, pi, j))
        lamp = amp
        while True:
            p, pi, j = data.pop(0)
            newAmp, np, npi = run(p, [lamp], pi)
            if newAmp is None:
                break
            lamp = newAmp
            if j == 4:
                amp = newAmp
            data.append((np, npi, j))
        if best <= amp:
            best = amp
            at = i

print(best, at)
