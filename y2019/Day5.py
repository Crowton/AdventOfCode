program = list(map(int, input().split(",")))

def getArg(loc, mode):
    a = program[loc]
    if mode == "0":
        a = program[a]
    return a

i = 0

while i < len(program):
    code = str(program[i])
    code = "0"*(5-len(code)) + code
    if code[3:5] == "01":
        a = getArg(i+1, code[2])
        b = getArg(i+2, code[1])
        program[program[i+3]] = a + b
        i += 4
    elif code[3:5] == "02":
        a = getArg(i+1, code[2])
        b = getArg(i+2, code[1])
        program[program[i+3]] = a * b
        i += 4
    elif code[3:5] == "03":
        program[program[i+1]] = int(input("In: "))
        i += 2
    elif code[3:5] == "04":
        print(getArg(i+1, code[2]))
        i += 2
    elif code[3:5] == "05":
        a = getArg(i+1, code[2])
        i = getArg(i+2, code[1]) if a != 0 else i + 3
    elif code[3:5] == "06":
        a = getArg(i+1, code[2])
        i = getArg(i+2, code[1]) if a == 0 else i + 3
    elif code[3:5] == "07":
        a = getArg(i+1, code[2])
        b = getArg(i+2, code[1])
        program[program[i+3]] = 1 if a < b else 0
        i += 4
    elif code[3:5] == "08":
        a = getArg(i+1, code[2])
        b = getArg(i+2, code[1])
        program[program[i+3]] = 1 if a == b else 0
        i += 4
    elif code[3:5] == "99":
        break
    else:
        print("PANIC!", code, i)
        break
