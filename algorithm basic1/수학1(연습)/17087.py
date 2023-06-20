#17087
import math

n, s = map(int, input().split())
bros = list(map(int, input().split()))
steps = [abs(b-s) for b in bros]

ans = []
idx= 0

if len(steps) == 1:
    ans.append(steps[0])
else:
    while idx+1 < len(steps):
        if len(steps) == 1:
            ans.append(steps[0])
            break
        ans.append(math.gcd(steps[idx], steps[idx+1]))
        idx += 1

print(min(ans))
