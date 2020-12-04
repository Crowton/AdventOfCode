# Part 1
# mustHave = {
#     "byr",
#     "iyr",
#     "eyr",
#     "hgt",
#     "hcl",
#     "ecl",
#     "pid",
# }

# valid = 0
# currHave = set()
# while True:
#     line = input()
#     if line == "-1":
#         break
#     if line == "":
#         valid += mustHave == currHave
#         currHave = set()
#     else:
#         for dat in line.split():
#             key, value = dat.split(":")
#             if key in mustHave:
#                 currHave.add(key)
# valid += mustHave == currHave
# print(valid)


valid = 0
currHave = 0
while True:
    line = input()
    if line == "-1":
        break
    if line == "":
        valid += currHave == 7
        currHave = 0
    else:
        for dat in line.split():
            key, value = dat.split(":")
            if key == "byr":
                currHave += (1920 <= int(value) <= 2002)
            elif key == "iyr":
                currHave += (2010 <= int(value) <= 2020)
            elif key == "eyr":
                currHave += (2020 <= int(value) <= 2030)
            elif key == "hgt":
                h = int("0" + value[:-2])
                if value[-2:] == "cm":
                    currHave += (150 <= h <= 193)
                elif value[-2:] == "in":
                    currHave += (59 <= h <= 76)
            elif key == "hcl":
                currHave += (value[0] == "#" and len(value) == 7 and all(v in "0123456789abcdef" for v in value[1:]))
            elif key == "ecl":
                currHave += (value in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"})
            elif key == "pid":
                currHave += (len(value) == 9 and all(v in "0123456789" for v in value))
            # print(key, value, currHave)

print(valid)
