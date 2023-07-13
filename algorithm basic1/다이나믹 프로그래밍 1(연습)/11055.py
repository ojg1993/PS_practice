# 11055

# 1차 풀이(오답)
# 4 1 2 3 10의 경우 4에서 tmp가 막혀 1,2,3이 들어오지 못함

# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split()))
# dp = [0] * n

# for i in range(n):
#     tmp = [0]
#     for j in range(i):
#         if arr[j] < arr[i] and arr[j] > tmp[-1]:
#             tmp.append(arr[j])
#     dp[i] = (arr[i] + sum(tmp))
#     print(dp)

# 2차 풀이

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = arr[:]

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + arr[i])
print(max(dp))

