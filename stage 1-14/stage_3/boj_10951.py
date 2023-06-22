# 10951

c = []
while True:
    try:
        a,b = map(int, input().split())
        c.append([a,b])
    except:
        break

for i in c:
    print(sum(i))