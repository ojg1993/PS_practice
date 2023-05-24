# 2739

b = []

for i in range(int(input())):
    c, d = map(int, input().split())
    b.append((c,d))
for t in b:
    print(t[0]+t[1])