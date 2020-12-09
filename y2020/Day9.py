preambleLen = 25
data = []

while True:
    line = input()
    if line == "":
        break

    num = int(line)
    data.append(num)


# Part 1
nums = data[:preambleLen]
badNum = "not found"
for num in data[preambleLen:]:
    for i, j in ((i, j) for i in range(preambleLen - 1) for j in range(i + 1, preambleLen)):
        if nums[i] + nums[j] == num:
            break
    else:
        badNum = num
        break

    nums.pop(0)
    nums.append(num)

print(badNum)


# Part 2
cumSum = [0]
for d in data:
    cumSum.append(cumSum[-1] + d)

for i in range(len(data)):
    # Note that this is linear search in sorted list
    # Binary search can therefore be implemented
    for j in range(i + 1, len(data)):
        if cumSum[j + 1] - cumSum[i] == badNum:
            numsInRange = data[i:j + 1]
            print(min(numsInRange) + max(numsInRange))
