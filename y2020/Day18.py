with open("Day18.in") as f:
    data = [l.replace("\n", "") for l in f.readlines()]


# Part 1
total = 0
for eq in data:
    nums = []
    opr = []
    stack = []
    for s in "(" + eq + ")":
        if s == " ":
            continue
        if "0" <= s <= "9":
            nums.append(int(s))
        elif s == "(":
            stack.append((nums, opr))
            nums, opr = [], []
        elif s == ")":
            res = nums[0]
            for n, o in zip(nums[1:], opr):
                if o == "+":
                    res += n
                else:
                    res *= n
            nums, opr = stack.pop()
            nums.append(res)
        else:
            opr.append(s)
    total += nums.pop()
print(total)


# Part 2
total = 0
for eq in data:
    nums = []
    opr = []
    stack = []
    for s in "(" + eq + ")":
        if s == " ":
            continue
        if "0" <= s <= "9":
            nums.append(int(s))
        elif s == "(":
            stack.append((nums, opr))
            nums, opr = [], []
        elif s == ")":
            res = nums[-1]
            for n, o in reversed(list(zip(nums[:-1], opr))):
                if o == "+":
                    res += n
                else:
                    res *= n
            nums, opr = stack.pop()
            nums.append(res)
        else:
            if s == "*":
                while len(nums) >= 2 and opr[-1] == "+":
                    nums.append(nums.pop() + nums.pop())
                    opr.pop()
            opr.append(s)
    total += nums.pop()
print(total)


# Hacky way for part 2
class MyInt:
    def __init__(self, val):
        self.val = val
    def __mul__(self, other):
        return MyInt(self.val + other.val)
    def __add__(self, other):
        return MyInt(self.val * other.val)

total = 0
for eq in data:
    update = eq.replace("+", "-").replace("*", "+").replace("-", "*")
    for n in range(10):
        update = update.replace(str(n), "MyInt(" + str(n) + ")")
    total += eval(update).val
print(total)
