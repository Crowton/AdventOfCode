people = 424
marbles = 71144 * 100
# people = 10
# marbles = 25


class Marble:
    def __init__(self, val):
        self.prev = self
        self.val = val
        self.next = self


circle = Marble(0)
scores = [0] * people
pers = 0

for i in range(1, marbles+1):
    if i % 23 == 0:
        scores[pers] += i

        circle = circle.prev.prev.prev.prev.prev.prev.prev

        scores[pers] += circle.val

        circle.prev.next = circle.next
        circle.next.prev = circle.prev

        circle = circle.next

    else:
        circle = circle.next

        marb = Marble(i)

        tempNext = circle.next
        circle.next = marb
        tempNext.prev = marb

        marb.prev = circle
        marb.next = tempNext

        circle = circle.next


    # print(pers, circle)
    pers = (pers + 1) % people
    # print(circle.val, circle.next.val)

print(max(scores))
