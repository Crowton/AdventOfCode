def getArg(loc, mode, program, rel):
    a = program[loc]
    if mode == "0":
        a = 0 if a >= len(program) else program[a]
    if mode == "2":
        a = 0 if a + rel >= len(program) else program[a + rel]
    return a


def setData(loc, mode, data, program, rel):
    a = program[loc]
    if mode == "0":
        while a >= len(program):
            program.append(0)
        program[a] = data
    elif mode == "2":
        while a + rel >= len(program):
            program.append(0)
        program[a + rel] = data
        

command = ""
program = list(map(int, input().split(",")))
rel = 0
i = 0
while i < len(program):
    code = str(program[i])
    code = "0" * (5 - len(code)) + code
    if code[3:5] == "01":
        a = getArg(i + 1, code[2], program, rel)
        b = getArg(i + 2, code[1], program, rel)
        setData(i + 3, code[0], a + b, program, rel)
        i += 4
    elif code[3:5] == "02":
        a = getArg(i + 1, code[2], program, rel)
        b = getArg(i + 2, code[1], program, rel)
        setData(i + 3, code[0], a * b, program, rel)
        i += 4
    elif code[3:5] == "03":
        if not command:
            command = input() + "\n"
        d = command[0]
        command = command[1:]
        setData(i + 1, code[2], ord(d), program, rel)
        i += 2
    elif code[3:5] == "04":
        d = getArg(i + 1, code[2], program, rel)
        if d < 256:
            print(chr(d), end="")
        else:
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
        setData(i + 3, code[0], 1 if a < b else 0, program, rel)
        i += 4
    elif code[3:5] == "08":
        a = getArg(i + 1, code[2], program, rel)
        b = getArg(i + 2, code[1], program, rel)
        setData(i + 3, code[0], 1 if a == b else 0, program, rel)
        i += 4
    elif code[3:5] == "09":
        rel += getArg(i + 1, code[2], program, rel)
        i += 2
    elif code[3:5] == "99":
        break
    else:
        print("PANIC!", code, i)
        break

# space heater
# hologram
# space law space brochure
# spool of cat6
# 2098048
