with open("Day23.in") as f:
    cups = list(map(int, f.read()))
    cupsClone = cups.copy()

# Part 1
for _ in range(100):
    current = cups[0]
    nextCups = cups[1:4]
    cups = cups[4:] + cups[:1]
    destination = current - 1
    while destination not in cups:
        destination -= 1
        if destination <= 0:
            destination = 9
    destinationPos = cups.index(destination)
    cups = cups[:destinationPos + 1] + nextCups + cups[destinationPos + 1:]

first = cups.index(1)
cups = cups[first + 1:] + cups[:first]
print("".join([str(c) for c in cups]))


# Part 2
class node:
    def __init__(self, val):
        self.val = val

# Build list
cupsExtended = cupsClone + list(range(10, 1_000_000 + 1))
nodes = {
    c: node(c)
    for c in cupsExtended
}
for i in range(len(cupsExtended) - 1):
    nodes[cupsExtended[i]].next = nodes[cupsExtended[i + 1]]
nodes[cupsExtended[-1]].next = nodes[cupsExtended[0]]

# Run moves
current = nodes[cupsClone[0]]
for _ in range(10_000_000):
    nextNode = current.next
    nextNextNextNode = nextNode.next.next
    current.next = nextNextNextNode.next
    cannotBe = [nextNode.val, nextNode.next.val, nextNode.next.next.val]
    destinationVal = current.val - 1
    if destinationVal == 0:
        destinationVal = 1_000_000
    while destinationVal in cannotBe:
        destinationVal -= 1
        if destinationVal == 0:
            destinationVal = 1_000_000
    destinationNode = nodes[destinationVal]
    nextNextNextNode.next = destinationNode.next
    destinationNode.next = nextNode
    current = current.next

# Find nodes after 1
oneNode = nodes[1]
print(oneNode.next.val * oneNode.next.next.val)
