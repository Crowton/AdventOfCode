# 341, 330
# 85, 214
# 162, 234
# 218, 246
# 130, 67
# 340, 41
# 206, 342
# 232, 295
# 45, 118
# 93, 132
# 258, 355
# 187, 302
# 181, 261
# 324, 246
# 150, 203
# 121, 351
# 336, 195
# 44, 265
# 51, 160
# 63, 133
# 58, 117
# 109, 276
# 292, 241
# 81, 56
# 281, 284
# 226, 104
# 98, 121
# 178, 234
# 319, 332
# 279, 234
# 143, 163
# 109, 333
# 80, 188
# 106, 242
# 65, 59
# 253, 137
# 287, 317
# 185, 50
# 193, 132
# 96, 319
# 193, 169
# 100, 155
# 113, 161
# 182, 82
# 157, 148
# 132, 67
# 339, 296
# 243, 208
# 196, 234
# 87, 335

points = []
for i in range(50):
    px, py = map(int, input().split(", "))
    points.append((px, py))

# owns = {}
# for p in points:
#     owns[p] = 0
#
# inf = set()
#
# for x in range(0, 500):
#     for y in range(0, 500):
#         dist = []
#         for i in range(len(points)):
#             p = points[i]
#             dist.append((abs(p[0]-x) + abs(p[1]-y), p))
#         dist2 = sorted(dist, key=lambda q: q[0])
#         if dist2[0][0] != dist2[1][0]:
#             owns[dist2[0][1]] += 1
#             if x == 0 or x == 499 or y == 0 or y == 499:
#                 inf.add(dist2[0][1])
#
# disttt = []
# for o in owns:
#     if o not in inf:
#         disttt.append(owns[o])
# print(max(disttt))

count = 0

for x in range(-500, 1000):
    for y in range(-500, 1000):
        dist = 0
        for i in range(len(points)):
            p = points[i]
            dist += abs(p[0]-x) + abs(p[1]-y)
        if dist < 10000:
            count += 1

print(count)