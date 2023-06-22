# 2571

start = int(input())
end = int(input())
tot = []
min_prime = float('inf')

for i in range(start, end+1):
    cnt = 0
    for j in range(1, i+1):
        if not i % j:
            cnt += 1
    if cnt == 2:
        tot.append(i)

if tot:
    print(sum(tot))
    print(tot[0])
else:
    print(-1)