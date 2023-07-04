# 1699

# import math
# n = int(input())
# cnt = 0
# for i in range(int(math.sqrt(n)), 0, -1):
#         while n >= i*i:
#             n -=  i*i
#             cnt += 1
# print(cnt)

n = int(input())
cache = [i for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, i):
        if j*j > i:
            break
        if cache[i] > cache[i - j * j] + 1:
            cache[i] = cache[i - j * j] + 1

print(cache[n])