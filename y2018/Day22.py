from collections import deque

# depth = 3879
# target = (8, 713)
depth = 510
target = (10, 10)

# geo = [[0] * (target[1] + 1) for i in range(target[0] + 1)]
#
# for x in range(1, target[0] + 1):
#     geo[x][0] = (x * 16807 + depth) % 20183
#
# for y in range(1, target[1] + 1):
#     geo[0][y] = (y * 48271 + depth) % 20183
#
# for x in range(1, target[0] + 1):
#     for y in range(1, target[1] + 1):
#         geo[x][y] = (geo[x-1][y] * geo[x][y-1] + depth) % 20183
#
# geo[0][0] = depth % 20183
# geo[target[0]][target[1]] = depth % 20183
#
# s = 0
#
# for x in range(0, target[0] + 1):
#     for y in range(0, target[1] + 1):
#         t = geo[x][y] % 3
#         s += t
#
#     #     if t == 0:
#     #         print('.', end="")
#     #     elif t == 1:
#     #         print('=', end="")
#     #     elif t == 2:
#     #         print('|', end="")
#     # print()
#
# print(s)

extra = 40

geo = [[0] * (target[1] + 1 + extra) for i in range(target[0] + 1 + extra)]

for x in range(1, target[0] + 1 + extra):
    geo[x][0] = (x * 16807 + depth) % 20183

for y in range(1, target[1] + 1 + extra):
    geo[0][y] = (y * 48271 + depth) % 20183

for x in range(1, target[0] + 1 + extra):
    for y in range(1, target[1] + 1 + extra):
        geo[x][y] = (geo[x-1][y] * geo[x][y-1] + depth) % 20183

geo[0][0] = depth % 20183
geo[target[0]][target[1]] = depth % 20183

for x in range(0, target[0] + 1 + extra):
    for y in range(0, target[1] + 1 + extra):
        geo[x][y] = geo[x][y] % 3

neither = 0
torch = 1
climping = 2

q = deque()
# x, y, delay, tool, totalTime, routeBeen
r = set()
r.add((0, 0))
q.append((0, 0, 0, torch, 0, r))

spaceSeen = {}
for x in range(0, target[0] + 1 + extra):
    for y in range(0, target[1] + 1 + extra):
        spaceSeen[(x, y)] = set()

spaceSeen[(0, 0)].add(torch)

while len(q) > 0:
    x, y, delay, tool, totalTime, routeBeen = q.popleft()
    print(x, y, delay, tool, totalTime, routeBeen)

    if delay > 0:
        q.append((x, y, delay-1, tool, totalTime, routeBeen))

    elif (x, y) == target:
        if tool != torch:
            q.append((x, y, 7, torch, totalTime + 7, routeBeen))
        else:
            print(totalTime)

            # for y in range(0, target[1] + 1 + extra):
            #     for x in range(0, target[0] + 1 + extra):
            #         if (x, y) in routeBeen:
            #             print("X", end="")
            #         else:
            #             print(".", end="")
            #     print()

            break

    else:
        if x > 0 and (x-1, y) not in routeBeen:
            rb = routeBeen.copy()
            rb.add((x-1, y))
            if geo[x-1][y] == tool:
                if tool == neither:
                    if torch not in spaceSeen[(x-1, y)]:
                        q.append((x-1, y, 7, torch, totalTime + 8, rb.copy()))
                        spaceSeen[(x-1, y)].add(torch)
                    if climping not in spaceSeen[(x-1, y)]:
                        q.append((x-1, y, 7, climping, totalTime + 8, rb.copy()))
                        spaceSeen[(x-1, y)].add(climping)
                elif tool == torch:
                    if neither not in spaceSeen[(x-1, y)]:
                        q.append((x-1, y, 7, neither, totalTime + 8, rb.copy()))
                        spaceSeen[(x-1, y)].add(neither)
                    if climping not in spaceSeen[(x-1, y)]:
                        q.append((x-1, y, 7, climping, totalTime + 8, rb.copy()))
                        spaceSeen[(x-1, y)].add(climping)
                else:
                    if neither not in spaceSeen[(x-1, y)]:
                        q.append((x-1, y, 7, neither, totalTime + 8, rb.copy()))
                        spaceSeen[(x-1, y)].add(neither)
                    if torch not in spaceSeen[(x-1, y)]:
                        q.append((x-1, y, 7, torch, totalTime + 8, rb.copy()))
                        spaceSeen[(x-1, y)].add(torch)
            elif tool not in spaceSeen[(x-1, y)]:
                q.append((x-1, y, 0, tool, totalTime + 1, rb))
                spaceSeen[(x-1, y)].add(tool)
        if y > 0 and (x, y-1) not in routeBeen:
            rb = routeBeen.copy()
            rb.add((x, y-1))
            if geo[x][y-1] == tool:
                if tool == neither:
                    if torch not in spaceSeen[(x, y-1)]:
                        q.append((x, y-1, 7, torch, totalTime + 8, rb.copy()))
                        spaceSeen[(x, y-1)].add(torch)
                    if climping not in spaceSeen[(x, y-1)]:
                        q.append((x, y-1, 7, climping, totalTime + 8, rb.copy()))
                        spaceSeen[(x, y-1)].add(climping)
                elif tool == torch:
                    if neither not in spaceSeen[(x, y-1)]:
                        q.append((x, y-1, 7, neither, totalTime + 8, rb.copy()))
                        spaceSeen[(x, y-1)].add(neither)
                    if climping not in spaceSeen[(x, y-1)]:
                        q.append((x, y-1, 7, climping, totalTime + 8, rb.copy()))
                        spaceSeen[(x, y-1)].add(climping)
                else:
                    if neither not in spaceSeen[(x, y-1)]:
                        q.append((x, y-1, 7, neither, totalTime + 8, rb.copy()))
                        spaceSeen[(x, y-1)].add(neither)
                    if torch not in spaceSeen[(x, y-1)]:
                        q.append((x, y-1, 7, torch, totalTime + 8, rb.copy()))
                        spaceSeen[(x, y-1)].add(torch)
            elif tool not in spaceSeen[(x, y-1)]:
                q.append((x, y-1, 0, tool, totalTime + 1, rb))
                spaceSeen[(x, y-1)].add(tool)
        if (x+1, y) not in routeBeen:
            rb = routeBeen.copy()
            rb.add((x+1, y))
            if geo[x+1][y] == tool:
                if tool == neither:
                    if torch not in spaceSeen[(x+1, y)]:
                        q.append((x+1, y, 7, torch, totalTime + 8, rb.copy()))
                        spaceSeen[(x+1, y)].add(torch)
                    if climping not in spaceSeen[(x+1, y)]:
                        q.append((x+1, y, 7, climping, totalTime + 8, rb.copy()))
                        spaceSeen[(x+1, y)].add(climping)
                elif tool == torch:
                    if neither not in spaceSeen[(x+1, y)]:
                        q.append((x+1, y, 7, neither, totalTime + 8, rb.copy()))
                        spaceSeen[(x+1, y)].add(neither)
                    if climping not in spaceSeen[(x+1, y)]:
                        q.append((x+1, y, 7, climping, totalTime + 8, rb.copy()))
                        spaceSeen[(x+1, y)].add(climping)
                else:
                    if neither not in spaceSeen[(x+1, y)]:
                        q.append((x+1, y, 7, neither, totalTime + 8, rb.copy()))
                        spaceSeen[(x+1, y)].add(neither)
                    if torch not in spaceSeen[(x+1, y)]:
                        q.append((x+1, y, 7, torch, totalTime + 8, rb.copy()))
                        spaceSeen[(x+1, y)].add(torch)
            elif tool not in spaceSeen[(x+1, y)]:
                q.append((x+1, y, 0, tool, totalTime + 1, rb))
                spaceSeen[(x+1, y)].add(tool)
        if (x, y+1) not in routeBeen:
            rb = routeBeen.copy()
            rb.add((x, y+1))
            if geo[x][y+1] == tool:
                if tool == neither:
                    if torch not in spaceSeen[(x, y+1)]:
                        q.append((x, y+1, 7, torch, totalTime + 8, rb.copy()))
                        spaceSeen[(x, y+1)].add(torch)
                    if climping not in spaceSeen[(x, y+1)]:
                        q.append((x, y+1, 7, climping, totalTime + 8, rb.copy()))
                        spaceSeen[(x, y+1)].add(climping)
                elif tool == torch:
                    if neither not in spaceSeen[(x, y+1)]:
                        q.append((x, y+1, 7, neither, totalTime + 8, rb.copy()))
                        spaceSeen[(x, y+1)].add(neither)
                    if climping not in spaceSeen[(x, y+1)]:
                        q.append((x, y+1, 7, climping, totalTime + 8, rb.copy()))
                        spaceSeen[(x, y+1)].add(climping)
                else:
                    if neither not in spaceSeen[(x, y+1)]:
                        q.append((x, y+1, 7, neither, totalTime + 8, rb.copy()))
                        spaceSeen[(x, y+1)].add(neither)
                    if torch not in spaceSeen[(x, y+1)]:
                        q.append((x, y+1, 7, torch, totalTime + 8, rb.copy()))
                        spaceSeen[(x, y+1)].add(torch)
            elif tool not in spaceSeen[(x, y+1)]:
                q.append((x, y+1, 0, tool, totalTime + 1, rb))
                spaceSeen[(x, y+1)].add(tool)

# 48 is not right
