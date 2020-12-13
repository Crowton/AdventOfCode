with open("Day13.in") as f:
    data = f.readlines()
    waitsFrom = int(data[0])
    bussesTimesWithIndex = [(int(t), i) for i, t in enumerate(data[1].split(",")) if t != "x"]

# Part 1
best = (float("inf"), -1)
for b, _ in bussesTimesWithIndex:
    departedBefore = waitsFrom % b
    departsIn = b - departedBefore
    best = min(best, (departsIn, b))
print(best[0] * best[1])


# Part 2
# Find t, such that "b | t + i" for all busses
# Observation: each bus has a period of b, and thus the event must happen every product time of all the b's
# Given a time that it happens, and the period of the event, the period can be multiplied up, to fit the next event
mustHappenEvery = bussesTimesWithIndex[0][0]
happenAt = bussesTimesWithIndex[0][0]
for b, i in bussesTimesWithIndex[1:]:
    x = 0
    while (happenAt + mustHappenEvery * x + i) % b != 0:
        x += 1
    happenAt += mustHappenEvery * x
    mustHappenEvery *= b
print(happenAt)
