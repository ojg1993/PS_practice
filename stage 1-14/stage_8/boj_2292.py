# 2292

destination = int(input())-1
ans = 1

while destination > 0:
    destination -= (6 * ans)
    ans += 1

print(ans)