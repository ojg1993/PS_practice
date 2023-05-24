# 11021

b = []

for i in range(int(input())):
    c, d = map(int, input().split())
    b.append((c,d))
for i, t in enumerate(b):
    print(f"Case #{i+1}: {sum(t)}")