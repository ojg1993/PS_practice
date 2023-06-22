# 15552

import sys
input = sys.stdin.readline

a = []
for i in range(int(input())):
    b,c = map(int, input().split())
    a.append([b,c])

for i in a:
    print(sum(i))