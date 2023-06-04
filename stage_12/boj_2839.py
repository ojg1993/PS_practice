# 2839

n = int(input())
tot = 0

while n > 0:
    if n % 5 == 0:
        tot += n//5
        n %= 5
        break
    n -= 3
    tot += 1
    
if not n:
    print(tot)
else:
    print(-1)