from time import time


program = []
while True:
    line = input()
    if line == "":
        break

    instr, count = line.split()
    program.append((instr, int(count)))

# Part 1
accVal = 0
programPointer = 0
linesSeen = set()
while True:
    if programPointer in linesSeen:
        print("Part1", accVal)
        break
    linesSeen.add(programPointer)

    instr, num = program[programPointer]
    if instr == "acc":
        accVal += num
    elif instr == "jmp":
        programPointer += num - 1

    programPointer += 1


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


start = time()
for i in range(len(program)):
    if program[i][0] != "acc":
        ret = runProgram(i)
        if ret is not None:
            print("Part2", ret, "chanced line", i)
end = time()
slowTime = end - start
print("Slow:", slowTime, "s")

# Faster part 2
# Construct graph
# Reverse and find set of need to reach nodes
# Traverse from start, and flip if possible to reach set
start = time()
graph = {}
for i, (instr, num) in enumerate(program):
    if instr == "acc":
        graph[i] = i + 1
    elif instr == "nop":
        graph[i] = (i + 1, i + num)
    else:
        graph[i] = (i + num, i + 1)

reverseGraph = {}
for node, goto in graph.items():
    if isinstance(goto, int):
        at = goto
    else:
        at = goto[0]
    at = min(at, len(program))
    if at not in reverseGraph:
        reverseGraph[at] = []
    reverseGraph[at].append(node)

canReach = set()
work = [len(program)]
while work:
    at = work.pop()
    canReach.add(at)
    if at in reverseGraph:
        for node in reverseGraph[at]:
            work.append(node)

at = 0
while True:
    if isinstance(graph[at], int):
        at = graph[at]
    else:
        goto, canGoto = graph[at]
        if canGoto in canReach:
            break
        else:
            at = goto

instr, num = program[at]
program[at] = ("jmp" if instr == "nop" else "nop", num)

accVal = 0
programPointer = 0
while programPointer < len(program):
    instr, num = program[programPointer]
    if instr == "acc":
        accVal += num
    elif instr == "jmp":
        programPointer += num - 1

    programPointer += 1

print("Part2 fast", accVal, "chanced line", at)

end = time()
fastTime = end - start
print("Fast:", fastTime, "s")
print("Faster by factor", slowTime / fastTime)
