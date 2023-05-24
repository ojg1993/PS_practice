# 25304
price = int(input())
tot = 0
for i in range(int(input())):
    a, b = map(int, input().split())
    tot += a *b
if price == tot:
    print('Yes')
else:
    print('No')