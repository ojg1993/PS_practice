# 9465

# 1차풀이(오답)

# for i in range(int(input())):
#     n = int(input())
#     ans = [0, 0]
#     cache = [list(map(int, input().split())) for _ in range(2)]
#
#     if n == 1:
#         ans[0] += cache[0][0]
#         ans[1] += cache[1][0]
#     elif n == 2:
#         ans[0] = cache[0][0] + cache[1][1]
#         ans[1] = cache[1][0] + cache[0][1]
#     else:
#         for j in range(n-2):
#             if not j % 2:
#                 ans[0] += cache[0][j]
#                 ans[1] += cache[1][j]
#             else:
#                 ans[0] += cache[1][j]
#                 ans[1] += cache[0][j]
#
#         if n % 2:
#             ans[0] += max((cache[1][n-2]+cache[0][n-1]), cache[1][n-1])
#             ans[1] += max((cache[0][n-2]+cache[1][n-1]), cache[0][n-1])
#
#     print(max(ans))


# 2차 풀이

for _ in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]

    if n > 1 :
        arr[0][1] += arr[1][0]
        arr[1][1] += arr[0][0]

        for i in range(2, n):
            arr[0][i] += max(arr[1][i-1], arr[1][i-2])
            arr[1][i] += max(arr[0][i-1], arr[0][i-2])
    print(arr[0])
    print(arr[1])
    print(max(arr[0][n-1], arr[1][n-1]))