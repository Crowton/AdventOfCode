R0 = 1
R1 = 0
R3 = 0
R4 = 0
R5 = 0

R3 += 2
R3 = R3 * R3
R3 *= 19
R3 *= 11
R4 += 7
R4 *= 22
R4 += 6
R3 += R4

R4 = 27
R4 *= 28
R4 += 29
R4 *= 30
R4 *= 14
R4 *= 32
R3 += R4
R0 = 0

R1 = 1

print(R3)

superBreak = False
while True:
    R5 = 1

    while True:
        if R1 * R5 == R3:
            R0 += R1
        R5 += 1

        if R5 > R3:
            R1 += 1
            if R1 > R3:
                superBreak = True
                break
            else:
                break

    if superBreak:
        break

print(R0)
