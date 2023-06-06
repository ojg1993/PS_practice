# 25305
n,m=map(int, input().split())

a = list(map(int, input().split()))

a = sorted(a)

a = a[::-1]

print(a[m-1])