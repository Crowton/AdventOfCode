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


# Part 2
# valid = 0
# currHave = 0
# while True:
#     line = input()
#     if line == "-1":
#         break
#     if line == "":
#         valid += currHave == 7
#         currHave = 0
#     else:
#         for dat in line.split():
#             key, value = dat.split(":")
#             if key == "byr":
#                 currHave += (1920 <= int(value) <= 2002)
#             elif key == "iyr":
#                 currHave += (2010 <= int(value) <= 2020)
#             elif key == "eyr":
#                 currHave += (2020 <= int(value) <= 2030)
#             elif key == "hgt":
#                 h = int("0" + value[:-2])
#                 if value[-2:] == "cm":
#                     currHave += (150 <= h <= 193)
#                 elif value[-2:] == "in":
#                     currHave += (59 <= h <= 76)
#             elif key == "hcl":
#                 currHave += (value[0] == "#" and len(value) == 7 and all(v in "0123456789abcdef" for v in value[1:]))
#             elif key == "ecl":
#                 currHave += (value in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"})
#             elif key == "pid":
#                 currHave += (len(value) == 9 and all(v in "0123456789" for v in value))
#
# print(valid)

conditions = {
    "byr": lambda value: 1920 <= int(value) <= 2002,
    "iyr": lambda value: 2010 <= int(value) <= 2020,
    "eyr": lambda value: 2020 <= int(value) <= 2030,
    "hgt": lambda value: value[-2:] == "cm" and (150 <= int("0" + value[:-2]) <= 193) or \
                         value[-2:] == "in" and (59 <= int("0" + value[:-2]) <= 76),
    "hcl": lambda value: value[0] == "#" and len(value) == 7 and all(v in "0123456789abcdef" for v in value[1:]),
    "ecl": lambda value: value in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
    "pid": lambda value: len(value) == 9 and all(v in "0123456789" for v in value),
    "cid": lambda value: False
}

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
            currHave += conditions[key](value)

print(valid)
