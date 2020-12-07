containedIn = {}
contains = {}
while True:
    line = input()
    if line == "":
        break

    outer, contents = line.split(" bags contain ")
    contains[outer] = []

    if contents != "no other bags.":
        bags = contents.split(", ")
        for b in bags:
            bData = b.split()
            count = int(b[0])
            bagType = " ".join(bData[1:-1])
            if bagType in containedIn:
                containedIn[bagType].append(outer)
            else:
                containedIn[bagType] = [outer]
            contains[outer].append((count, bagType))

# Part 1
seen = set()
work = ["shiny gold"]
while work:
    bag = work.pop()
    if bag not in seen:
        seen.add(bag)
        if bag in containedIn:
            for b in containedIn[bag]:
                work.append(b)

print(len(seen) - 1)


# Part 2
def traverse(bag):
    return 1 + sum(traverse(b) * c for c, b in contains[bag])


print(traverse("shiny gold") - 1)
