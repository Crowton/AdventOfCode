w = 25
h = 6
image = input()
layers = [image[i:i+w*h] for i in range(0, len(image), w*h)]

# min0, minLay = min((sum(1 for p in l if p == "0"), l) for l in layers)
# print(sum(1 for p in minLay if p == "1") * sum(1 for p in minLay if p == "2"))

finalImg = [p for p in layers[-1]]
for l in reversed(layers):
    for i, p in enumerate(l):
        if p != "2":
            finalImg[i] = p

imgimg = [finalImg[i:i+w] for i in range(0, len(finalImg), w)]
# s = 0
for l in imgimg:
    for p in l:
        if p == "1":
            print("#", end="")
            # s += 1
        else:
            print(" ", end="")
    print()
# AZCJC
# print(s, len(finalImg) - s)
