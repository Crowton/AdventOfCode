import math

reactionsReversed = {}
for _ in range(57):
    line = input().split(" => ")
    dataIn = line[0].split(", ")
    needed = []
    for d in dataIn:
        data = d.split(" ")
        needed.append((int(data[0]), data[1]))
    dataOut = line[1].split(" ")
    reactionsReversed[dataOut[1]] = (int(dataOut[0]), needed)

# missing = [(1, "FUEL")]
# rest = {t: 0 for t in reactionsReversed}
# ore = 0
# while missing:
#     # print(missing)
#     # print(rest)
#     amount, typ = missing.pop()
#     if amount <= rest[typ]:
#         rest[typ] -= amount
#     else:
#         amount -= rest[typ]
#         getting, needs = reactionsReversed[typ]
#         mul = math.ceil(amount / getting)
#         rest[typ] = (getting * mul) - amount
#         for needAmount, needTyp in needs:
#             if needTyp == "ORE":
#                 ore += needAmount * mul
#             else:
#                 missing.append((needAmount * mul, needTyp))
#     # print(rest)
#     # print()
    
# print("Ore pr fuel:", ore)


oneTrillion = 1000000000000
rest = {t: 0 for t in reactionsReversed}
produced = 0
multiplum = 2**20
while multiplum != 0:
    print(oneTrillion, multiplum)
    missing = [(multiplum, "FUEL")]
    restClone = {t: rest[t] for t in rest}
    ore = 0
    while missing:
        amount, typ = missing.pop()
        if amount <= rest[typ]:
            rest[typ] -= amount
        else:
            amount -= rest[typ]
            getting, needs = reactionsReversed[typ]
            mul = math.ceil(amount / getting)
            rest[typ] = (getting * mul) - amount
            for needAmount, needTyp in needs:
                if needTyp == "ORE":
                    ore += needAmount * mul
                else:
                    missing.append((needAmount * mul, needTyp))
    if ore <= oneTrillion:
        produced += multiplum
        oneTrillion -= ore
    else:
        multiplum //= 2
        rest = restClone

print(produced)
# 2267482 too low
# 2267483 too low
# 2267488 wrong
# 2267489 too high

# 2^20 -> 2267482 too low
# 2^14 -> 2267483 too low
# 2^13 -> 2267488
# 2^12 -> 2267489 too high
# 2^11 -> 2267483 too low
# 2^10 -> 2267489 too high
