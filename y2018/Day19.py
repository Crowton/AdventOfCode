# #ip 2
# addi 2 16 2
# seti 1 1 1
# seti 1 8 5
# mulr 1 5 4
# eqrr 4 3 4
# addr 4 2 2
# addi 2 1 2
# addr 1 0 0
# addi 5 1 5
# gtrr 5 3 4
# addr 2 4 2
# seti 2 0 2
# addi 1 1 1
# gtrr 1 3 4
# addr 4 2 2
# seti 1 1 2
# mulr 2 2 2
# addi 3 2 3
# mulr 3 3 3
# mulr 2 3 3
# muli 3 11 3
# addi 4 7 4
# mulr 4 2 4
# addi 4 6 4
# addr 3 4 3
# addr 2 0 2
# seti 0 3 2
# setr 2 0 4
# mulr 4 2 4
# addr 2 4 4
# mulr 2 4 4
# muli 4 14 4
# mulr 4 2 4
# addr 3 4 3
# seti 0 4 0
# seti 0 4 2

instr = []

ipl = int(input().split()[1])

for i in range(36):
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


# registers = [0, 0, 0, 0, 0, 0]
registers = [1, 0, 0, 0, 0, 0]

i = 0

while 0 <= registers[ipl] < 36:
    cmd, A, B, C = instr[registers[ipl]]
    instrMap[cmd](registers, A, B, C)
    registers[ipl] += 1

    # i += 1
    # if i % 100 == 0:
    #     print(i, registers)
    print(registers[ipl])

print(registers[0])
