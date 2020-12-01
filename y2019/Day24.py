board = [[s for s in input()] for _ in range(5)]


# def getBugs(x, y):
#     c = 0
#     if y > 0 and board[y-1][x] == "#":
#         c += 1
#     if y < 4 and board[y+1][x] == "#":
#         c += 1
#     if x > 0 and board[y][x-1] == "#":
#         c += 1
#     if x < 4 and board[y][x+1] == "#":
#         c += 1
#     return c
#
#
# seen = set()
# # rounds = 0
# while True:
#     boardState = tuple([s for line in board for s in line])
#     if boardState in seen:
#         break
#     seen.add(boardState)
#
#     newBoard = [[board[y][x] for x in range(5)] for y in range(5)]
#     for y in range(5):
#         for x in range(5):
#             if board[y][x] == "#":
#                 if getBugs(x, y) != 1:
#                     newBoard[y][x] = "."
#             else:
#                 if 1 <= getBugs(x, y) <= 2:
#                     newBoard[y][x] = "#"
#     board = newBoard
#
# diversity = 0
# counter = 1
# for y in range(5):
#     for x in range(5):
#         print(board[y][x], end="")
#         if board[y][x] == "#":
#             diversity += counter
#         counter *= 2
#     print()
# print()
# print(diversity)

neighbours = {}
for y in range(5):
    for x in range(5):
        if (x, y) != (2, 2):
            n = []
            if x == 0:
                n.append((1, 2, -1))
            elif x == 4:
                n.append((3, 2, -1))
            if y == 0:
                n.append((2, 1, -1))
            elif y == 4:
                n.append((2, 3, -1))
            
            if x == 2 and y == 1:
                for xPrime in range(5):
                    n.append((xPrime, 0, 1))
            if x == 2 and y == 3:
                for xPrime in range(5):
                    n.append((xPrime, 4, 1))
            if x == 1 and y == 2:
                for yPrime in range(5):
                    n.append((0, yPrime, 1))
            if x == 3 and y == 2:
                for yPrime in range(5):
                    n.append((4, yPrime, 1))
            
            if x > 0 and (x-1, y) != (2, 2):
                n.append((x-1, y, 0))
            if x < 4 and (x+1, y) != (2, 2):
                n.append((x+1, y, 0))
            if y > 0 and (x, y-1) != (2, 2):
                n.append((x, y-1, 0))
            if y < 4 and (x, y+1) != (2, 2):
                n.append((x, y+1, 0))
            neighbours[(x, y)] = n


boardLevels = {0: board}
boardLevels[-1] = [["." for x in range(5)] for y in range(5)]
boardLevels[1] = [["." for x in range(5)] for y in range(5)]

for l in range(200):
    newBoardLevels = {}
    
    newBoardLevels[-l-1] = [["." for x in range(5)] for y in range(5)]
    newBoardLevels[l+1] = [["." for x in range(5)] for y in range(5)]
    newBoardLevels[-l-2] = [["." for x in range(5)] for y in range(5)]
    newBoardLevels[l+2] = [["." for x in range(5)] for y in range(5)]
    boardLevels[-l-2] = [["." for x in range(5)] for y in range(5)]
    boardLevels[l+2] = [["." for x in range(5)] for y in range(5)]
        
    for levels in range(-l-1, l+2):
        newBoard = [[boardLevels[levels][y][x] for x in range(5)] for y in range(5)]
        for y in range(5):
            for x in range(5):
                if (x, y) != (2, 2):
                    # if (x, y) == (4, 0) and levels == 0:
                    #     print(neighbours[(x, y)])
                    #     print(sum(1 for x, y, diffL in neighbours[(x, y)] if boardLevels[levels + diffL][y][x] == "#"))
                    #     print(boardLevels[levels][y][x])
                    if boardLevels[levels][y][x] == "#":
                        if sum(1 for x, y, diffL in neighbours[(x, y)] if boardLevels[levels + diffL][y][x] == "#") != 1:
                            newBoard[y][x] = "."
                    else:
                        if 1 <= sum(1 for x, y, diffL in neighbours[(x, y)] if boardLevels[levels + diffL][y][x] == "#") <= 2:
                            newBoard[y][x] = "#"
        newBoardLevels[levels] = newBoard
    boardLevels = newBoardLevels
    # for lev in range(-2, 3):
    #     print("Depth", lev, ":")
    #     for y in range(5):
    #         for x in range(5):
    #             print(boardLevels[lev][y][x], end="")
    #         print()
    #     print()
    # print()

c = 0
for l in boardLevels:
    # print("Depth", l, ":")
    for y in range(5):
        for x in range(5):
            if boardLevels[l][y][x] == "#":
                c += 1
            # print(boardLevels[l][y][x], end="")
        # print()
    # print()
print(c)

# 1892 too low
