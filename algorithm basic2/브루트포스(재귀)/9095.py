# 9095
import sys
input = sys.stdin.readline
n = int(input())
cache = [1] + [0] * 10
cache[1] = 1 # 1
cache[2] = 2 # 1+1, 2
cache[3] = 4 # 1+1+1, 2+1, 1+2, 3


for i in range(3, 11):
    cache[i] = cache[i-3] + cache[i-2] + cache[i-1]

for i in range(n):
    n = int(input())
    print(cache[n])