# 2501

a, b = map(int, input().split())
c = []

for i in range(1, a+1):
    if not a % i:
        c.append(i)
try:
    print(c[b-1])
except:
    print(0)