# import math
# w, h = 48, 48
#
# m = [input() for _ in range(h)]
# astroids = {(x, y) for x in range(w) for y in range(h) if m[y][x] == "#"}
#
# best = 0
# at = ()
# for (ax, ay) in astroids:
#     s = 0
#     for (bx, by) in astroids:
#         if not (ax == bx and ay == by):
#             diffx = bx - ax
#             diffy = by - ay
#             if diffx == 0:
#                 sign = 1 if diffy > 0 else -1
#                 if not any((ax, ay + y * sign) in astroids for y in range(1, abs(diffy))):
#                     s += 1
#             elif diffy == 0:
#                 sign = 1 if diffx > 0 else -1
#                 if not any((ax + x * sign, ay) in astroids for x in range(1, abs(diffx))):
#                     s += 1
#             else:
#                 gcd = math.gcd(abs(diffx), abs(diffy))
#                 minDiffx = diffx // gcd
#                 minDiffy = diffy // gcd
#                 if not any((ax + minDiffx * i, ay + minDiffy * i) in astroids for i in range(1, gcd)):
#                     s += 1
#     if s > best:
#         best = s
#         at = (ax, ay)
#
# print(best, at)


# 309 (37, 25)

import math
w, h = 48, 48

m = [input() for _ in range(h)]
astroids = {(x, y) for x in range(w) for y in range(h) if m[y][x] == "#"}

(ax, ay) = (37, 25)
sees = set()
for (bx, by) in astroids:
    if not (ax == bx and ay == by):
        diffx = bx - ax
        diffy = by - ay
        if diffx == 0:
            sign = 1 if diffy > 0 else -1
            if not any((ax, ay + y * sign) in astroids for y in range(1, abs(diffy))):
                sees.add((bx, by))
                print(bx, by)
        elif diffy == 0:
            sign = 1 if diffx > 0 else -1
            if not any((ax + x * sign, ay) in astroids for x in range(1, abs(diffx))):
                sees.add((bx, by))
        else:
            gcd = math.gcd(abs(diffx), abs(diffy))
            minDiffx = diffx // gcd
            minDiffy = diffy // gcd
            if not any((ax + minDiffx * i, ay + minDiffy * i) in astroids for i in range(1, gcd)):
                sees.add((bx, by))


# def left_turn(p, q, r):
#     """ Check if r is to the left of the line through p and q
#     """
#     return (q[0]-p[0]) * (r[1]-p[1]) - (r[0]-p[0]) * (q[1]-p[1]) >= 0

def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang


# print(getAngle((0, 20), (0,0), (-2, 5)))
# print(getAngle((0, 20), (0,0), (-2, -5)))
# print(getAngle((0, 20), (0,0), (2, -5)))

c = (ax, ay)
sortedOrder = [(37, 13)]
sees.remove((37, 13))

for p in sees:
    sortedOrder.append(p)

for i in range(1, len(sortedOrder)):
    j = i
    while j > 1 and getAngle(sortedOrder[0], c, sortedOrder[j]) < getAngle(sortedOrder[0], c, sortedOrder[j-1]):
        sortedOrder[j-1], sortedOrder[j] = sortedOrder[j], sortedOrder[j-1]
        j -= 1

print(sortedOrder[199])

# m2 = [[p for p in m[i]] for i in range(h)]
# m2[ay][ax] = "X"
# m2[sortedOrder[0][1]][sortedOrder[0][0]] = "0"
# m2[sortedOrder[1][1]][sortedOrder[1][0]] = "1"
# m2[sortedOrder[2][1]][sortedOrder[2][0]] = "2"
# m2[sortedOrder[3][1]][sortedOrder[3][0]] = "3"
# m2[sortedOrder[4][1]][sortedOrder[4][0]] = "4"
# m2[sortedOrder[5][1]][sortedOrder[5][0]] = "5"
# m2[sortedOrder[6][1]][sortedOrder[6][0]] = "6"
# m2[sortedOrder[7][1]][sortedOrder[7][0]] = "7"
# for r in m2:
#     for c in r:
#         print(c, end="")
#     print()
