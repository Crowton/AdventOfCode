program = []
while True:
    line = input()
    if line == "":
        break

    instr, count = line.split()
    program.append((instr, int(count)))

# Part 1
# accVal = 0
# programPointer = 0
# linesSeen = set()
# while True:
#     if programPointer in linesSeen:
#         print(accVal)
#         break
#     linesSeen.add(programPointer)
#
#     instr, num = program[programPointer]
#     if instr == "acc":
#         accVal += num
#     elif instr == "jmp":
#         programPointer += num - 1
#
#     programPointer += 1


# Part 2
def runProgram(chanceLine):
    accVal = 0
    programPointer = 0
    linesSeen = set()
    while programPointer < len(program):
        if programPointer in linesSeen:
            return None
        linesSeen.add(programPointer)

        instr, num = program[programPointer]

        if programPointer == chanceLine:
            instr = "jmp" if instr == "nop" else "nop"

        if instr == "acc":
            accVal += num
        elif instr == "jmp":
            programPointer += num - 1

        programPointer += 1

    return accVal


for i in range(len(program)):
    if program[i][0] != "acc":
        ret = runProgram(i)
        if ret is not None:
            print(ret)
