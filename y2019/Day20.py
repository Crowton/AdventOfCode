# board = [[s for s in input()] for _ in range(133)]
#
# portals = {}
#
# for x in range(1, len(board[0])-1):
#     for y in range(1, len(board) - 1):
#         if "A" <= board[y][x] <= "Z":
#             entry = (0, 0)
#             if board[y-1][x] == ".":
#                 entry = (x, y-1)
#                 board[y][x] = board[y][x] + board[y+1][x]
#                 board[y+1][x] = " "
#             elif board[y+1][x] == ".":
#                 entry = (x, y+1)
#                 board[y][x] = board[y-1][x] + board[y][x]
#                 board[y-1][x] = " "
#             elif board[y][x-1] == ".":
#                 entry = (x-1, y)
#                 board[y][x] = board[y][x] + board[y][x+1]
#                 board[y][x+1] = " "
#             elif board[y][x+1] == ".":
#                 entry = (x+1, y)
#                 board[y][x] = board[y][x-1] + board[y][x]
#                 board[y][x-1] = " "
#
#             if board[y][x] not in portals:
#                 portals[board[y][x]] = ((x, y), entry)
#             else:
#                 otherPos, otherEntry = portals[board[y][x]]
#                 portals[otherPos] = entry
#                 portals[(x, y)] = otherEntry
#                 del portals[board[y][x]]
#
# queue = [(0, portals["AA"][0])]
# # print(portals["ZZ"])
# seen = set()
# while queue:
#     d, pos = queue.pop(0)
#     # print(d, pos)
#     # print(d, pos, board[pos[1]][pos[0]])
#     # if pos == portals["ZZ"]:
#     #     print(d)
#     #     break
#     if pos not in seen:
#         seen.add(pos)
#         for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#             if board[pos[1] + dy][pos[0] + dx] == ".":
#                 queue.append((d+1, (pos[0] + dx, pos[1] + dy)))
#             elif (pos[0] + dx, pos[1] + dy) in portals:
#                 queue.append((d+1, portals[(pos[0] + dx, pos[1] + dy)]))
#             elif board[pos[1] + dy][pos[0] + dx] == "ZZ":
#                 print(d-1)

board = [[s for s in input()] for _ in range(133)]

portals = {}

for x in range(1, len(board[0])-1):
    for y in range(1, len(board) - 1):
        if "A" <= board[y][x] <= "Z":
            entry = (0, 0)
            depth = 0
            if board[y-1][x] == ".":
                entry = (x, y-1)
                depth = -1 if y == len(board) - 2 else 1
                board[y][x] = board[y][x] + board[y+1][x]
                board[y+1][x] = " "
            elif board[y+1][x] == ".":
                entry = (x, y+1)
                depth = -1 if y == 1 else 1
                board[y][x] = board[y-1][x] + board[y][x]
                board[y-1][x] = " "
            elif board[y][x-1] == ".":
                entry = (x-1, y)
                depth = -1 if x == len(board[0]) - 2 else 1
                board[y][x] = board[y][x] + board[y][x+1]
                board[y][x+1] = " "
            elif board[y][x+1] == ".":
                entry = (x+1, y)
                depth = -1 if x == 1 else 1
                board[y][x] = board[y][x-1] + board[y][x]
                board[y][x-1] = " "
            
            if depth != 0:
                # print(board[y][x], (x, y), depth)
                if board[y][x] not in portals:
                    portals[board[y][x]] = ((x, y), entry, depth)
                else:
                    otherPos, otherEntry, otherDepth = portals[board[y][x]]
                    portals[otherPos] = (entry, otherDepth)
                    portals[(x, y)] = (otherEntry, depth)
                    del portals[board[y][x]]

# print()
queue = [(0, 0, portals["AA"][0])]
seen = set()
while queue:
    d, depth, pos = queue.pop(0)
    if (pos, depth) not in seen:
        seen.add((pos, depth))
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if board[pos[1] + dy][pos[0] + dx] == ".":
                queue.append((d+1, depth, (pos[0] + dx, pos[1] + dy)))
            elif (pos[0] + dx, pos[1] + dy) in portals:
                entry, depthDelta = portals[(pos[0] + dx, pos[1] + dy)]
                newDepth = depth + depthDelta
                if newDepth >= 0:
                    queue.append((d+1, newDepth, entry))
            elif board[pos[1] + dy][pos[0] + dx] == "ZZ" and depth == 0:
                print(d-1)
