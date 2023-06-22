# 2720

for i in range(int(input())):
    a = int(input())
    changes = [25, 10, 5, 1]
    ans = []
    for c in changes:
        ans.append(a//c)
        a %= c
    print(*ans)