s = 0
n = 10551396

for i in range(1, n + 1):
    if n % i == 0:
        s += i

print(s)

# 14068556 too low
# forgot to add n itself
# 24619952
