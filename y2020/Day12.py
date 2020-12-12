import math


with open("Day12.in") as f:
    instr = f.readlines()
    instr = [(l[0], int(l[1:])) for l in instr]


# Part 1
pos = (0, 0)
facing = 0
go = {
    "E": (1, 0),
    "W": (-1, 0),
    "N": (0, 1),
    "S": (0, -1)
}

for ins, num in instr:
    if ins in go:
        pos = (pos[0] + go[ins][0] * num, pos[1] + go[ins][1] * num)
    elif ins == "F":
        pos = (pos[0] + math.cos(facing) * num, pos[1] + math.sin(facing) * num)
    else:
        if ins == "R":
            num = -num
        facing = (facing + math.radians(num)) % (math.pi * 2)

print(abs(round(pos[0])) + abs(round(pos[1])))


# Part 2
pos = (0, 0)
wayPos = (10, 1)

for ins, num in instr:
    if ins in go:
        wayPos = (wayPos[0] + go[ins][0] * num, wayPos[1] + go[ins][1] * num)
    elif ins == "F":
        pos = (pos[0] + wayPos[0] * num, pos[1] + wayPos[1] * num)
    else:
        if ins == "R":
            num = -num

        s = math.sin(math.radians(num))
        c = math.cos(math.radians(num))
        wayPos = (wayPos[0] * c - wayPos[1] * s, wayPos[0] * s + wayPos[1] * c)

print(abs(round(pos[0])) + abs(round(pos[1])))
