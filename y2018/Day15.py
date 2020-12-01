################################
######......###...##..##########
######....#G###G..##.G##########
#####...G##.##.........#########
##....##..#.##...........#######
#....#G.......##.........G.#####
##..##GG....G.................##
##.......G............#.......##
###.....G.....G#......E.......##
##......##....................##
#.....####......G.....#...######
#.#########.G....G....#E.#######
###########...#####......#######
###########..#######..E.......##
###########.#########......#.###
########..#.#########.........##
#######G....#########........###
##.##.#.....#########...EE#..#.#
#...GG......#########.#...##..E#
##...#.......#######..#...#....#
###.##........#####......##...##
###.........................#..#
####.............##........###.#
####............##.........#####
####..##....###.#...#.....######
########....###..............###
########..G...##.###...E...E.###
#########...G.##.###.E....E.####
#########...#.#######.......####
#############..########...######
##############.########.########
################################

#######
#G..#E#
#E#E.E#
#G.##.#
#...#E#
#...E.#
#######

from collections import deque

# elfAttack = 15
elfAttack = 3
# 58395 is too low

# w = 32
# h = 32
w = 7
h = 7

theMap = []

# (x, y) -> (unitType, hp, att)
units = {}
count = 0

for i in range(h):
    line = input()
    line2 = ""
    for j in range(w):
        c = line[j]
        if c == 'G':
            units[(j, i)] = (c, 200, 3)
            c = '.'
        elif c == 'E':
            units[(j, i)] = (c, 200, elfAttack)
            c = '.'
            count += 1
        line2 += c
    theMap.append(line2)

turns = 0
while True:
    attacked = False
    unitsToMoveOrder = sorted(units, key=lambda t: (t[1], t[0]))
    for (x, y) in unitsToMoveOrder:
        unitType = units[(x, y)][0]
        unitHP = units[(x, y)][1]
        unitAtt = units[(x, y)][2]

        if unitHP <= 0:
            continue

        q = deque()
        q.append((x, y))
        cameFrom = {
            (x, y): (x, y)
        }

        goto = (x, y)

        while len(q) > 0:
            nx, ny = q.popleft()
            if (nx, ny) in units and units[(nx, ny)][1] > 0 and (x, y) != (nx, ny):
                if units[(nx, ny)][0] != unitType:
                    goto = (nx, ny)
                    while cameFrom[goto] != (x, y):
                        goto = cameFrom[goto]
                    break
            else:
                if ((nx, ny-1) not in cameFrom or cameFrom[(nx, ny-1)][1] <= 0) and theMap[ny-1][nx] == '.':
                    q.append((nx, ny-1))
                    cameFrom[(nx, ny-1)] = (nx, ny)
                if ((nx-1, ny) not in cameFrom or cameFrom[(nx-1, ny)][1] <= 0) and theMap[ny][nx-1] == '.':
                    q.append((nx-1, ny))
                    cameFrom[(nx-1, ny)] = (nx, ny)
                if ((nx+1, ny) not in cameFrom or cameFrom[(nx+1, ny)][1] <= 0) and theMap[ny][nx+1] == '.':
                    q.append((nx+1, ny))
                    cameFrom[(nx+1, ny)] = (nx, ny)
                if ((nx, ny+1) not in cameFrom or cameFrom[(nx, ny+1)][1] <= 0) and theMap[ny+1][nx] == '.':
                    q.append((nx, ny+1))
                    cameFrom[(nx, ny+1)] = (nx, ny)

        mx, my = goto

        if goto in units and units[goto][1] > 0:
            mx = x
            my = y

        possible = []
        if (mx, my-1) in units and units[(mx, my-1)][0] != unitType and units[(mx, my-1)][1] > 0:
            possible.append((mx, my-1, 1))
        if (mx-1, my) in units and units[(mx-1, my)][0] != unitType and units[(mx-1, my)][1] > 0:
            possible.append((mx-1, my, 2))
        if (mx+1, my) in units and units[(mx+1, my)][0] != unitType and units[(mx+1, my)][1] > 0:
            possible.append((mx+1, my, 3))
        if (mx, my+1) in units and units[(mx, my+1)][0] != unitType and units[(mx, my+1)][1] > 0:
            possible.append((mx, my+1, 4))

        possible = sorted(possible, key=lambda t: (units[(t[0], t[1])][1], t[2]))

        if len(possible) > 0:
            ux, uy, prio = possible[0]
            tempT, tempHP, tempAtt = units[(ux, uy)]
            units[(ux, uy)] = (tempT, tempHP - unitAtt, tempAtt)
            attacked = True

        if (x, y) != (mx, my):
            units[(mx, my)] = (unitType, unitHP, unitAtt)
            del units[(x, y)]

    units2 = {}
    for u in units:
        if units[u][1] > 0:
            units2[u] = units[u]
    units = units2

    print()
    print(turns + 1)
    for y in range(h):
        info = "    "
        for x in range(w):
            if (x, y) in units:
                print(units[(x, y)][0], end="")
                info += str(units[(x, y)][0]) + "(" + str(units[(x, y)][1]) + ") "
            else:
                print(theMap[y][x], end="")
        print(info)

    types = set()
    for u in units:
        types.add(units[u][0])

    if len(types) == 1:
        totalHP = 0
        for u in units:
            totalHP += units[u][1]
            # print(u, units[u][1])
        print(turns)
        print(totalHP * turns)
        print(count, len(units))
        break

    turns += 1


    # input()

# 216540 too high
# 3*90 too high - one unit didn't lose health

















