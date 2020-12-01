# #ip 5
# seti 123 0 1
# bani 1 456 1
# eqri 1 72 1
# addr 1 5 5
# seti 0 0 5
# seti 0 4 1
# bori 1 65536 4
# seti 12772194 7 1
# bani 4 255 3
# addr 1 3 1
# bani 1 16777215 1
# muli 1 65899 1
# bani 1 16777215 1
# gtir 256 4 3
# addr 3 5 5
# addi 5 1 5
# seti 27 3 5
# seti 0 0 3
# addi 3 1 2
# muli 2 256 2
# gtrr 2 4 2
# addr 2 5 5
# addi 5 1 5
# seti 25 5 5
# addi 3 1 3
# seti 17 4 5
# setr 3 4 4
# seti 7 1 5
# eqrr 1 0 3
# addr 3 5 5
# seti 5 1 5

instr = []

ipl = int(input().split()[1])

for i in range(31):
    ins, a, b, c = input().split()
    instr.append([ins, int(a), int(b), int(c)])


def addr(registers, A, B, C):
    registers[C] = registers[A] + registers[B]


def addi(registers, A, B, C):
    registers[C] = registers[A] + B


def mulr(registers, A, B, C):
    registers[C] = registers[A] * registers[B]


def muli(registers, A, B, C):
    registers[C] = registers[A] * B


def banr(registers, A, B, C):
    registers[C] = registers[A] & registers[B]


def bani(registers, A, B, C):
    registers[C] = registers[A] & B


def borr(registers, A, B, C):
    registers[C] = registers[A] | registers[B]


def bori(registers, A, B, C):
    registers[C] = registers[A] | B


def setr(registers, A, B, C):
    registers[C] = registers[A]


def seti(registers, A, B, C):
    registers[C] = A


def gtir(registers, A, B, C):
    if A > registers[B]:
        registers[C] = 1
    else:
        registers[C] = 0


def gtri(registers, A, B, C):
    if registers[A] > B:
        registers[C] = 1
    else:
        registers[C] = 0


def gtrr(registers, A, B, C):
    if registers[A] > registers[B]:
        registers[C] = 1
    else:
        registers[C] = 0


def eqir(registers, A, B, C):
    if A == registers[B]:
        registers[C] = 1
    else:
        registers[C] = 0


def eqri(registers, A, B, C):
    if registers[A] == B:
        registers[C] = 1
    else:
        registers[C] = 0


def eqrr(registers, A, B, C):
    if registers[A] == registers[B]:
        registers[C] = 1
    else:
        registers[C] = 0


instrMap = {
    "addr": addr,
    "addi": addi,
    "mulr": mulr,
    "muli": muli,
    "banr": banr,
    "bani": bani,
    "borr": borr,
    "bori": bori,
    "setr": setr,
    "seti": seti,
    "gtir": gtir,
    "gtri": gtri,
    "gtrr": gtrr,
    "eqir": eqir,
    "eqri": eqri,
    "eqrr": eqrr
}

registers = [-1, 0, 0, 0, 0, 0]

R1Seen = set()
last = 0

while 0 <= registers[ipl] < 36:
    cmd, A, B, C = instr[registers[ipl]]
    instrMap[cmd](registers, A, B, C)

    if registers[ipl] == 28:
        # print(registers[1])
        # exit()
        # It ternimates, when R1 == R0 in line 28
        # R1 = 2159153 at this point, the first time

        if registers[1] in R1Seen:
            print(last)
            exit()
        else:
            R1Seen.add(registers[1])
            last = registers[1]

        if len(R1Seen) % 50 == 0:
            print("len", len(R1Seen))

    registers[ipl] += 1

