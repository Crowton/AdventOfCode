from collections import deque

routes = input()[1:-1] + ')'


# def pretty(f, i):
#     while routes[f] != ')':
#         if routes[f] == '(':
#             print('\n' + ' ' * i * 4, end="")
#             f = pretty(f + 1, i + 1)
#         elif routes[f] == '|':
#             print()
#             print(' ' * i * 4, end="")
#         else:
#             print(routes[f], end="")
#         f += 1
#     print('\n' + ' ' * (i-1) * 4)
#     return f
#
#
# pretty(0, 1)


# def findMax(f):
#     parts = []
#     curr = 0
#     while routes[f] != ')':
#         if routes[f] == '(':
#             f, c = findMax(f + 1)
#             curr += c
#         elif routes[f] == '|':
#             parts.append(curr)
#             curr = 0
#         else:
#             curr += 1
#         f += 1
#
#     parts.append(curr)
#     print(parts)
#     return f, max(parts)
#
#
# print(findMax(0)[1])


# def find(f):
#     parts = []
#     curr = 0
#     while routes[f] != ')':
#         if routes[f] == '(':
#             f, p = find(f + 1)
#             if routes[f+1] == ')' or routes[f+1] == '|':
#                 curr += max(p)
#             else:
#                 curr += min(p)
#         elif routes[f] == '|':
#             parts.append(curr)
#             curr = 0
#         else:
#             curr += 1
#         f += 1
#
#     parts.append(curr)
#     # print(parts)
#     return f, parts
#
#
# print(max(find(0)[1]))

# 4340 too low

roads = {}

def connect(a, b):
    if a not in roads:
        roads[a] = [b]
    else:
        roads[a].append(b)
    if b not in roads:
        roads[b] = [a]
    else:
        roads[b].append(a)


def spreadFrom(f, pX, pY):
    startX = pX
    startY = pY
    while routes[f] != ')':
        if routes[f] == '(':
            f = spreadFrom(f + 1, pX, pY)
        elif routes[f] == '|':
            pX = startX
            pY = startY
        else:
            if routes[f] == 'N':
                connect((pX, pY), (pX, pY-1))
                pY -= 1
            elif routes[f] == 'S':
                connect((pX, pY), (pX, pY+1))
                pY += 1
            elif routes[f] == 'E':
                connect((pX, pY), (pX+1, pY))
                pX += 1
            else:
                connect((pX, pY), (pX-1, pY))
                pX -= 1
        f += 1

    return f


spreadFrom(0, 0, 0)

# print(roads)
#
# minX = min([t[0] for t in roads])
# maxX = max([t[0] for t in roads])
# minY = min([t[1] for t in roads])
# maxY = max([t[1] for t in roads])
#
# print('#' * ((maxX - minX + 1) * 2 + 1))
# for y in range(minY, maxY + 1):
#     print('#', end="")
#     for x in range(minX, maxX + 1):
#         if (x, y) == (0, 0):
#             print('X', end="")
#         else:
#             print('.', end="")
#         if (x+1, y) in roads[(x, y)]:
#             print('|', end="")
#         else:
#             print('#', end="")
#     print()
#     print('#', end="")
#     for x in range(minX, maxX + 1):
#         if (x, y+1) in roads[(x, y)]:
#             print('-', end="")
#         else:
#             print('#', end="")
#         print('#', end="")
#     print()

q = deque()
q.append((0, 0, 0))

visited = set()

distances = []

while len(q) > 0:
    x, y, d = q.popleft()

    if (x, y) in visited:
        continue

    visited.add((x, y))
    distances.append(d)

    if (x+1, y) in roads[(x, y)]:
        q.append((x+1, y, d + 1))
    if (x-1, y) in roads[(x, y)]:
        q.append((x-1, y, d + 1))
    if (x, y+1) in roads[(x, y)]:
        q.append((x, y+1, d + 1))
    if (x, y-1) in roads[(x, y)]:
        q.append((x, y-1, d + 1))

print(max(distances))
print(sum(d >= 1000 for d in distances))
