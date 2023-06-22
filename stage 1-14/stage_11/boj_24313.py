# 24313

a, b = map(int, input().split())
c = int(input())
n = int(input())

f = a * n + b
g = c * n

print(1 if f <= g and c >= a else 0)