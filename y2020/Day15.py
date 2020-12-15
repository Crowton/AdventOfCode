with open("Day15.in") as f:
    data = list(map(int, f.readline().split(",")))

# Part 1
nums = list(data)
while len(nums) < 2020:
    nextNum = nums[-1]
    isTheNum = [i for i, n in enumerate(nums) if n == nextNum]
    if len(isTheNum) == 1:
        nums.append(0)
    else:
        nums.append(isTheNum[-1] - isTheNum[-2])
print(nums[-1])


# Part 2
nums = list(data)
indexes = {}
for no in nums:
    indexes[no] = [i for i, n in enumerate(nums) if n == no]
c = len(nums)
lastNum = nums[-1]

while c < 30000000:
    isTheNum = indexes[lastNum]
    toAppend = 0 if len(isTheNum) == 1 else isTheNum[-1] - isTheNum[-2]

    if toAppend not in indexes:
        indexes[toAppend] = []
    indexes[toAppend].append(c)
    if len(indexes[toAppend]) > 2:
        indexes[toAppend].pop(0)

    c += 1
    lastNum = toAppend

print(lastNum)
