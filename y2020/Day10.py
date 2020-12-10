with open("Day10.in") as f:
    data = list(map(int, f.readlines()))

s = 0
data.append(s)
t = max(data) + 3
data.append(t)

# Part 1
data.sort()
diffs = [0] * 4
for i in range(len(data) - 1):
    diffs[data[i + 1] - data[i]] += 1
print(diffs[1] * diffs[3])


# Part 2
waysTo = {i: 0 for i in data}
waysTo[t] = 1
for d in reversed(data):
    for e in range(1, 4):
        if d + e in waysTo:
            waysTo[d] += waysTo[d + e]
print(waysTo[s])
