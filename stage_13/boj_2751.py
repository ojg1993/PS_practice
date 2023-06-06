# 2751
import sys
input = sys.stdin.readline

n = int(input())

a =[]

for _ in range(n):
    a.append(int(input()))

for i in sorted(a):
    print(i)