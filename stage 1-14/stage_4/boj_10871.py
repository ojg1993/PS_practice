# 10871

a, b = map(int, input().split())

c = list(map(int, input().split()))
d = []
for i in c:
    if i < b:
        d.append(str(i))
print(' '.join(d))