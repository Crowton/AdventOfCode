programInit = list(map(int, input().split(",")))
machines = [([p for p in programInit], 0, 0) for _ in range(50)]
inputs = [[i] for i in range(50)]


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
        

def runProgram(number):
    program, rel, i = machines[number]
    outputs = []
    failInput = 0
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
            if inputs[number]:
                d = inputs[number][0]
                inputs[number] = inputs[number][1:]
            else:
                if failInput == 5:
                    machines[number] = (program, rel, i)
                    return [], True
                d = -1
                failInput += 1
            setData(i + 1, code[2], d, program, rel)
            i += 2
        elif code[3:5] == "04":
            d = getArg(i + 1, code[2], program, rel)
            outputs.append(d)
            i += 2
            if len(outputs) == 3:
                machines[number] = (program, rel, i)
                return outputs, False
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
            machines[number] = (program, rel, i)
            break
        else:
            print("PANIC!", code, i, number)
            machines[number] = (program, rel, i)
            break
    return [], False


# running = True
# while running:
#     print("Cycle")
#     # print(all(len(i) % 2 == 0 for i in inputs))
#     for i in range(50):
#         output = runProgram(i)
#         if len(output) == 3:
#             if output[0] == 255:
#                 print(output[2])
#                 running = False
#                 break
#             inputs[output[0]].append(output[1])
#             inputs[output[0]].append(output[2])


NAT = []
seenY = set()
c, c1 = 0, 0
while True:
    c += 1
    noOutIn = True
    for i in range(50):
        output, failIn = runProgram(i)
        if len(output) == 3:
            noOutIn = False
            if output[0] == 255:
                NAT = [output[1], output[2]]
            else:
                inputs[output[0]].append(output[1])
                inputs[output[0]].append(output[2])
        if not failIn and noOutIn:
            noOutIn = False
    if noOutIn:
        c1 += 1
        if NAT[1] in seenY:
            print(NAT[1], c, c1)
            break
        seenY.add(NAT[1])
        inputs[0].append(NAT[0])
        inputs[0].append(NAT[1])
