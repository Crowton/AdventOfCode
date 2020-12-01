moonPos = [
    -3, 15, -11,
    3, 13, -19,
    -13, 18, -2,
    6, 0, -1
]

moonVel = [0] * 12

# for _ in range(1000):
#     for i in range(4):
#         for j in range(4):
#             if i != j:
#                 for c in range(3):
#                     moonVel[i * 3 + c] += -1 if moonPos[i * 3 + c] > moonPos[j * 3 + c] \
#                         else 1 if moonPos[i * 3 + c] < moonPos[j * 3 + c] \
#                         else 0
#     for i in range(12):
#         moonPos[i] += moonVel[i]

# print("After", _, "steps:")
# for i in range(0, 12, 3):
#     print("pos=<x=" + str(moonPos[i]) + ", y=" + str(moonPos[i + 1]) + ", z=" + str(moonPos[i + 2]) + ">, "
#           + "vel=<x=" + str(moonVel[i]) + ", y=" + str(moonVel[i + 1]) + ", z=" + str(moonVel[i + 2]) + ">, ")

# totalEnergy = 0
# for i in range(4):
#     pot = sum(abs(moonPos[i * 3 + c]) for c in range(3))
#     kin = sum(abs(moonVel[i * 3 + c]) for c in range(3))
#     totalEnergy += pot * kin
# print(totalEnergy)

# moonPos = [
#     -1, 0, 2,
#     2, -10, -7,
#     4, -8, 8,
#     3, 5, -1,
# ]

from time import time
start = time()

cycleLen = []

for c in range(3):
    iterPos = [moonPos[i*3+c] for i in range(4)]
    iterVel = [moonVel[i*3+c] for i in range(4)]
    initPos = tuple(iterPos)
    initVel = tuple(iterVel)
    
    it = 0
    
    while True:
        for i in range(4):
            for j in range(4):
                if i != j:
                    iterVel[i] += -1 if iterPos[i] > iterPos[j] \
                        else 1 if iterPos[i] < iterPos[j] \
                        else 0

        for i in range(4):
            iterPos[i] += iterVel[i]
        
        it += 1
        if tuple(iterPos) == initPos and tuple(iterVel) == initVel:
            cycleLen.append(it)
            break

import math
lcm = (cycleLen[0] * cycleLen[1]) // (math.gcd(cycleLen[0], cycleLen[1]))
lcm = (lcm * cycleLen[2]) // (math.gcd(lcm, cycleLen[2]))
print(lcm)
print(cycleLen)

print("------ Running time", "{0:.2f}".format(time() - start), "seconds ------")
