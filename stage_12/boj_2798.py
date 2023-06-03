# 2798

from itertools import combinations

a,b = map(int, input().split())
c = list(map(int, input().split()))
c = sorted(c)
ans = 0
for combi in combinations(c, 3):
    if sum(combi) <= b:
        ans = max(ans, sum(combi))

print(ans)
