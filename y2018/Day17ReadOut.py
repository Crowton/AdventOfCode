count = 0
for i in range(1881):
   for c in input():
        # if c == '|' or c == '~':
        if c == '~':
            count += 1
print(count)

# data = []
#
# for i in range(1881):
#     data.append("." + input() + ".")
# data.append('|' * len(data[0]))
#
# for y in range(len(data) - 1):
#     for x in range(1, len(data[0]) - 1):
#         if data[y][x] == '|':
#             if data[y + 1][x] == '.':
#                 print("Error at", x, ",", y, " Missing water under flow")
#             elif data[y + 1][x] == '|':
#                 if data[y][x-1] != '.' and data[y][x+1] != '.':
#                     print("Error at", x, ",", y, " Water spread with running under")
#             elif data[y][x-1] != '|' and data[y][x+1] != '|':
#                 print("Error at", x, ",", y, " Water doesn't spread")
#         elif data[y][x] == '~':
#             if data[y+1][x] != '~' and data[y+1][x] != '#' or data[y][x-1] != '~' and data[y][x-1] != '#' or data[y][x+1] != '~' and data[y][x+1] != '#':
#                 print("Error at", x, ",", y, " Still water could flow")

# 34288 too low
# 34285 also low

# 34398 also low

# 34422 is wrong