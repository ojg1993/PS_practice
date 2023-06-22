# 3009

# from collections import Counter

# dots = [input().split() for i in range(3)]
# x = []
# y = []
# for dot in dots:
#     x.append(dot[0])
#     y.append(dot[1])
# x = Counter(x)
# y = Counter(y)
# ans = (1000,1000)
# ans2 = (1000,1000)

# for d, t in x.items():
#     if t < ans[1]:
#         ans = (d, t)
# for d, t in y.items():
#     if t < ans2[1]:
#         ans2 = (d, t)
# print(ans[0], ans2[0])

X = []
Y = []

for _ in range(3):
    x, y = map(int, input().split())
    if x in X:
        X.remove(x)
    else:
        X.append(x)
    if y in Y:
        Y.remove(y)
    else:
        Y.append(y)
print(*X, *Y)