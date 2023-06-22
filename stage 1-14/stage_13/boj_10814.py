10814
import sys
input = sys.stdin.readline

arr = []
for i in range(1, int(input())+1):
    a, n = input().split()
    arr.append((int(a), i, n))

arr.sort()

for a in arr:
    print(a[0], a[2])