# basePattern = [0, 1, 0, -1]
# number = [int(i) for i in input()]
#
# for _ in range(100):
#     newNum = []
#     print(_)
#     for i in range(len(number)):
#         pattern = []
#         q = 0
#         while len(pattern) <= len(number):
#             for j in range(i + 1):
#                 pattern.append(basePattern[q])
#             q = (q + 1) % 4
#         pattern.pop(0)
#         newNum.append(abs(sum(k*l for k, l in zip(number, pattern))) % 10)
#         print(i)
#     number = newNum
#
# for d in range(8):
#     print(number[d], end="")


numberGiven = '59705379150220188753316412925237003623341873502562165618681895846838956306026981091618902964505317589975353803891340688726319912072762197208600522256226277045196745275925595285843490582257194963750523789260297737947126704668555847149125256177428007606338263660765335434914961324526565730304103857985860308906002394989471031058266433317378346888662323198499387391755140009824186662950694879934582661048464385141787363949242889652092761090657224259182589469166807788651557747631571357207637087168904251987880776566360681108470585488499889044851694035762709053586877815115448849654685763054406911855606283246118699187059424077564037176787976681309870931'
number = [int(i) for _ in range(10000) for i in numberGiven]
offset = int(numberGiven[:7])

for _ in range(100):
    # print _

    ps = [0]
    for i in number:
        ps.append(ps[-1] + i)

    for i in range(len(number)):
        s = 0
        for j in range(i, len(number), (i+1)*4):
            s += ps[min(len(number) - 1, j + i + 1)] - ps[j]
        for j in range(3*(i+1) - 1, len(number), (i+1)*4):
            s -= ps[min(len(number) - 1, j + i + 1)] - ps[j]
        number[i] = abs(s) % 10

# print 'num'
# for d in range(8):
#     print number[d + offset]

# numberGiven = input()
# number = [int(i) for _ in range(10000) for i in numberGiven]
# offset = int(numberGiven[:7])
#
# for _ in range(100):
#     print(_)
#
#     ps = [0]
#     for i in number:
#         ps.append(ps[-1] + i)
#
#     newNum = []
#     for i in range(len(number) // 2):
#         s = 0
#         for j in range(i, len(number), (i+1)*4):
#             s += ps[min(len(number) - 1, j + i + 1)] - ps[j]
#         for j in range(3*(i+1) - 1, len(number), (i+1)*4):
#             s -= ps[min(len(number) - 1, j + i + 1)] - ps[j]
#         newNum.append(abs(s) % 10)
#
#     s = 0
#     for i in reversed(range(len(number) // 2, len(number))):
#         s += number[i]
#         newNum.append(abs(s) % 10)
#     number = newNum
#
# for d in range(8):
#     print(number[d + offset], end="")
