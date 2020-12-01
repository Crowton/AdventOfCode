people = 424
marbles = 71144 * 100
# people = 10
# marbles = 25

scores = [0] * people
circle = [0]
curr = 1
pers = 0

for i in range(1, marbles+1):
    if i % 23 == 0:
        scores[pers] += i
        curr = (curr - 9) % len(circle)
        scores[pers] += circle.pop(curr)
        curr = (curr + 2) % len(circle)

    else:
        if curr == 0:
            curr = len(circle)
        circle.insert(curr, i)
        curr = (curr + 2) % len(circle)

    # print(pers, circle)
    pers = (pers + 1) % people

    if i % 100 == 0:
        print(i)

print(max(scores))
