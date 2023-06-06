# 11650
n = int(input())

arr =[]

for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort()

for a in arr:
    print(*a)