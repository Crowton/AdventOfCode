R0 = 0

R1 = 0
R2 = 0
R3 = 0
R4 = 0


R1 = 123
while True:
    R1 = R1 & 456
    if R1 == 72:
        break

R1 = 0

while True:
    R4 = R1 | 65536
    R1 = 12772194
    R3 = R4 & 255
    R1 += R3
    R1 = R1 & 16777215
    R1 *= 65899
    R1 = R1 & 16777215

    print(R4)
    exit()

    if 256 > R4:
        if R1 == R0:
            exit()
        # else:
            # goto 5
    else:
        R3 = 0
        R2 = R3 + 1
        R2 *= 256
        if R2 > R4:
            R4 = R3
