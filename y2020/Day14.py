with open("Day14.in") as f:
    data = [l[:-1] for l in f.readlines()]


def toBinStr(num, l):
    numStr = str(bin(int(num)))[2:]
    numStrPad = "0" * (l - len(numStr)) + numStr
    return numStrPad


# Part 1
mask = "X" * 36
mem = {}
for line in data:
    writeTo, value = line.split(" = ")
    if writeTo == "mask":
        mask = value
    else:
        adr = int(writeTo[4:-1])
        valStrPadList = list(toBinStr(int(value), 36))
        for i, t in enumerate(mask):
            if t != "X":
                valStrPadList[i] = t
        valueUpdate = int("".join(valStrPadList), base=2)
        mem[adr] = valueUpdate

print(sum(v for v in mem.values()))


# Part 2
mask = "0" * 36
mem = {}
for line in data:
    writeTo, value = line.split(" = ")
    if writeTo == "mask":
        mask = value
    else:
        adr = int(writeTo[4:-1])
        adrStrPadList = list(toBinStr(adr, 36))
        floats = []
        for i, t in enumerate(mask):
            if t == "X":
                floats.append(i)
            elif t == "1":
                adrStrPadList[i] = "1"
        if not floats:
            adrUpdate = int("".join(adrStrPadList), base=2)
            mem[adrUpdate] = int(value)
        else:
            val = int(value)
            for adrChance in range(2**len(floats)):
                adrChanceStrPad = toBinStr(adrChance, len(floats))
                for i, v in zip(floats, adrChanceStrPad):
                    adrStrPadList[i] = v
                adrUpdate = int("".join(adrStrPadList), base=2)
                mem[adrUpdate] = val

print(sum(v for v in mem.values()))
