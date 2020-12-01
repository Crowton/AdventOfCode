def getArg(loc, mode, program):
    a = program[loc]
    if mode == "0":
        a = program[a]
    return a


def run(program, inputs):
    output = []
    i = 0
    c = 0
    while i < len(program):
        code = str(program[i])
        code = "0" * (5 - len(code)) + code
        c += 1
        # if c % 100000 == 0:
        #     print(program[theList : theList + 81])
        if code[3:5] == "01":
            a = getArg(i + 1, code[2], program)
            b = getArg(i + 2, code[1], program)
            program[program[i + 3]] = a + b
            i += 4
        elif code[3:5] == "02":
            a = getArg(i + 1, code[2], program)
            b = getArg(i + 2, code[1], program)
            program[program[i + 3]] = a * b
            i += 4
        elif code[3:5] == "03":
            program[program[i + 1]] = inputs.pop()
            i += 2
        elif code[3:5] == "04":
            output.append(getArg(i + 1, code[2], program))
            i += 2
        elif code[3:5] == "05":
            a = getArg(i + 1, code[2], program)
            i = getArg(i + 2, code[1], program) if a != 0 else i + 3
        elif code[3:5] == "06":
            a = getArg(i + 1, code[2], program)
            i = getArg(i + 2, code[1], program) if a == 0 else i + 3
        elif code[3:5] == "07":
            a = getArg(i + 1, code[2], program)
            b = getArg(i + 2, code[1], program)
            program[program[i + 3]] = 1 if a < b else 0
            i += 4
        elif code[3:5] == "08":
            a = getArg(i + 1, code[2], program)
            b = getArg(i + 2, code[1], program)
            program[program[i + 3]] = 1 if a == b else 0
            i += 4
        elif code[3:5] == "99":
            print("Instructions executed:", c)
            return output
        else:
            print("PANIC!", code, i)
            break


off = 398
arg0 = 0 + off
arg1 = 1 + off
argp = 2 + off
argr = 3 + off
argc = 4 + off
argb = 5 + off
argbprime = 6 + off
argv = 7 + off
argrv = 8 + off
argcv = 9 + off
argbv = 10 + off
argbvprime = 11 + off
arggood = 12 + off
theList = 13 + off
theList2 = 94 + off

program = [1007, arg0, 81, 5,
           1106, 0, 20,
           1001, arg0, theList, 12,
           3, 0,
           101, 1, arg0, arg0,
           1105, 1, 0,

           1101, 0, 0, arg0,
           1007, arg0, 81, 29,
           1106, 0, 61,

           101, theList, arg0, 36,
           1008, 0, 0, 40,
           1106, 0, 54,

           101, theList2, arg1, 49,
           101, 0, arg0, 0,
           101, 1, arg1, arg1,

           101, 1, arg0, arg0,
           1105, 1, 24,

           1101, 0, 0, arg0,
           107, -1, arg0, 70,
           1106, 0, 363,
           7, arg0, arg1, 77,
           1106, 0, 363,

           101, theList2, arg0, 85,
           101, theList, 0, 92,
           1001, 92, 0, 94,
           1001, 0, 1, 0,

           1001, 92, 0, 100,
           1008, 0, 10, 104,
           1106, 0, 121,

           1001, 92, 0, 113,
           1101, 0, 0, 0,
           1001, arg0, -1, arg0,
           1105, 1, 65,

           1101, 0, 0, argr,
           1001, 92, -theList, argc,

           107, 8, argc, 134,
           1106, 0, 147,
           1001, argr, 1, argr,
           1001, argc, -9, argc,
           1105, 1, 129,

           1101, 0, 0, argb,
           1001, argr, 0, argbprime,

           107, 2, argbprime, 160,
           1106, 0, 173,
           1001, argb, 1, argb,
           1001, argbprime, -3, argbprime,
           1105, 1, 155,

           1002, argb, 3, argb,
           1001, argc, 0, argbprime,

           107, 2, argbprime, 186,
           1106, 0, 199,
           1001, argb, 1, argb,
           1001, argbprime, -3, argbprime,
           1105, 1, 181,

           1101, 0, 1, arggood,
           1101, 0, 0, argv,

           1007, argv, 81, 212,
           1106, 0, 353,

           1001, 85, 0, 220,
           8, argv, 0, 223,
           1105, 0, 346,
           1001, argv, theList, 234,
           1001, 92, 0, 235,
           8, 0, 0, 238,
           1106, 0, 346,

           1101, 0, 0, argrv,
           101, 0, argv, argcv,

           107, 8, argcv, 253,
           1106, 0, 266,
           1001, argrv, 1, argrv,
           1001, argcv, -9, argcv,
           1105, 1, 248,

           1101, 0, 0, argbv,
           101, 0, argrv, argbvprime,

           107, 2, argbvprime, 279,
           1106, 0, 292,
           1001, argbv, 1, argbv,
           1001, argbvprime, -3, argbvprime,
           1105, 1, 274,

           1002, argbv, 3, argbv,
           1001, argcv, 0, argbvprime,

           107, 2, argbvprime, 305,
           1106, 0, 318,
           1001, argbv, 1, argbv,
           1001, argbvprime, -3, argbvprime,
           1105, 1, 300,

           8, argr, argrv, 323,
           1105, 0, 342,
           8, argc, argcv, 330,
           1105, 0, 342,
           8, argb, argbv, 337,
           1105, 0, 342,
           1105, 1, 346,

           1101, 0, 0, arggood,

           1001, argv, 1, argv,
           1105, 1, 207,

           1006, arggood, 65,
           1001, arg0, 1, arg0,
           1105, 1, 65,

           1008, arg0, -1, 368,
           1106, 0, 373,
           104, -1,
           99,

           1101, 0, 0, arg0,
           1007, arg0, 81, 382,
           1106, 0, 397,

           101, theList, arg0, 389,
           4, 0,
           1001, arg0, 1, arg0,
           1105, 1, 377,

           99,

           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,

           0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0,

           0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0,
           ]
sudoku = list(
    reversed([int(i) for i in "530070000600195000098000060800060003400803001700020006060000280000419005000080079"]))

from time import time
start = time()

result = run(program, sudoku)
print(result)

print("------ Running time", "{0:.2f}".format(time() - start), "seconds ------")

# Instructions: 44.244.462
