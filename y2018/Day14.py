itr = 260321

recipes = [3, 7]

elf1 = 0
elf2 = 1

# while len(recipes) < itr + 10:
#     newRecipe = recipes[elf1] + recipes[elf2]
#
#     for c in str(newRecipe):
#         recipes.append(int(c))
#
#     elf1 = (elf1 + recipes[elf1] + 1) % len(recipes)
#     elf2 = (elf2 + recipes[elf2] + 1) % len(recipes)
#
# for i in range(itr, itr+10):
#     print(recipes[i], end="")

seenRight = 0
itrString = str(itr)

found = False
while not found:
    newRecipe = recipes[elf1] + recipes[elf2]

    for c in str(newRecipe):
        recipes.append(int(c))

        if itrString[seenRight] == c:
            seenRight += 1
            if seenRight == len(itrString):
                print(len(recipes) - len(itrString))
                found = True
                break
        else:
            seenRight = 0

            if itrString[seenRight] == c:
                seenRight += 1
                if seenRight == len(itrString):
                    print(len(recipes) - len(itrString))
                    found = True
                    break

    elf1 = (elf1 + recipes[elf1] + 1) % len(recipes)
    elf2 = (elf2 + recipes[elf2] + 1) % len(recipes)

# 20319117
