c = 0

for p in range(245318, 765747 + 1):
    ps = str(p)
    good = True
    pair = False
    for d in range(len(ps) - 1):
        if ps[d] > ps[d+1]:
            good = False
            break
        if ps[d] == ps[d+1]:
            if sum(1 for dd in ps if dd == ps[d]) == 2:
                pair = True
    
    if good and pair:
        c += 1

print(c)
