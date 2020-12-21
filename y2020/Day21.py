with open("Day21.in") as f:
    data = []
    for line in f.readlines():
        inc, contains = line.split(" (contains ")
        data.append((
            inc.split(" "),
            contains[:-2].split(", ")
        ))


# Part 1
allNames = {n for incs, _ in data for n in incs}
allAlg = {n for _, algs in data for n in algs}

canBe = {
    a: allNames.copy()
    for a in allAlg
}

for incs, algs in data:
    for a in algs:
        canBe[a].intersection_update(incs)

canContainAlg = {n for s in canBe.values() for n in s}
print(sum(i not in canContainAlg for incs, _ in data for i in incs))


# Part 2
candidates = [k for k, v in canBe.items() if len(v) == 1]
while candidates:
    inc = candidates.pop()
    mustBe = next(s for s in canBe[inc])
    for k, v in canBe.items():
        if k != inc and mustBe in v:
            v.remove(mustBe)
            if len(v) == 1:
                candidates.append(k)

assert all(len(v) == 1 for v in canBe.values())
isAlg = {next(s for s in v): k for k, v in canBe.items()}
incs = sorted(list(isAlg.keys()), key=lambda i: isAlg[i])
print(",".join(incs))
