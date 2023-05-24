# 10952

c = []

while True:
    a,b = map(int, input().split())
    if not a and not b:
        break
    else:
        c.append([a,b])

for i in c:
    print(sum(i))