# cards = 10007
# deck = [i for i in range(cards)]
#
# while True:
#     line = input()
#     if line == "":
#         break
#
#     if line == "deal into new stack":
#         deck = list(reversed(deck))
#     elif line[:4] == "cut ":
#         num = int(line[4:])
#         if num < 0:
#             num = cards + num
#         deck = deck[num:] + deck[:num]
#     elif line[:20] == "deal with increment ":
#         num = int(line[20:])
#         newDeck = [0] * cards
#         p = 0
#         for c in deck:
#             newDeck[p] = c
#             p = (p + num) % cards
#         deck = newDeck
#
# for i, c in enumerate(deck):
#     if c == 2019:
#         print(i)

# cards = 11 #119315717514047
# interPos = 0 #2020
# commands = []
#
# while True:
#     line = input()
#     if line == "":
#         break
#
#     if line == "deal into new stack":
#         commands.append(("s", 0))
#     elif line[:4] == "cut ":
#         num = int(line[4:])
#         if num < 0:
#             num = cards + num
#         commands.append(("c", num))
#     elif line[:20] == "deal with increment ":
#         num = int(line[20:])
#         # p = 0
#         # i = 0
#         # t = []
#         # while True:
#         #     if (interPos - p) % num == 0:
#         #         break
#         #     else:
#         #         i += (cards - p) // num
#         #         t.append((cards - p) // num)
#         #         p = num - (cards - p) % num
#         commands.append(("i", num))
#
#
# from time import time
# start = time()
#
# for _ in range(1): #101741582076661):
#     if _ % 1000 == 999:
#         print("------ Running time", "{0:.2f}".format(time() - start), "seconds ------")
#         break
#     for c, n in reversed(commands):
#         print(interPos)
#         if c == "s":
#             interPos = cards - interPos - 1
#         elif c == "c":
#             interPos = (interPos + n) % cards
#         elif c == "i":
#             # interPos = pow(interPos, cards-2, cards)
#             interPos = interPos // n
#
# print(interPos)


cards = 119315717514047

offset, increment = 0, 1

while True:
    line = input()
    if line == "":
        break

    if line == "deal into new stack":
        increment *= -1
        offset += increment
    elif line[:4] == "cut ":
        num = int(line[4:])
        offset += increment * num
    elif line[:20] == "deal with increment ":
        num = int(line[20:])
        increment *= pow(num, cards-2, cards)

passes = 101741582076661
finalInc = pow(increment, passes, cards)
finalOff = offset * (1 - pow(increment, passes, cards)) * pow(1 - increment, cards-2, cards)
print((finalOff + finalInc * 2020) % cards)
