# 2193

n = int(input())

cache = [0] * (n+1)
cache[1] = 1

# top down

def pinary_number(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif cache[n]:
        return cache[n]
    else:
        cache[n] = pinary_number(n-1) + pinary_number(n-2)
    return cache[n]

print(pinary_number(n))


# bottom up

for i in range(2, n+1):
    cache[i] = cache[i-1] + cache[i-2]

print(cache[n])