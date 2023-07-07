# 15988

nums = []
for i in range(int(input())):
    nums.append(int(input()))

mod = 1_000_000_009
cache = [0] * (max(nums)+1)
cache[1] = 1
cache[2] = 2
cache[3] = 4
for i in range(4, max(nums)+1):
    cache[i] = (cache[i-1] + cache[i-2] + cache[i-3]) % mod

for i in nums:
    print(cache[i] % mod)