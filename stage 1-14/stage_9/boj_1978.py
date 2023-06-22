# 1978

a = input()

b = list(map(int, input().split()))
c = 0
for i in b:
    cnt = 0
    for j in range(2,i+1):
        if not i % j:
            cnt += 1
    if cnt == 1:
        c += 1

print(c)