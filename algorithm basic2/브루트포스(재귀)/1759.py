# 1759
import sys
from itertools import combinations
input = sys.stdin.readline


L, C = map(int, input().split())
letters = sorted(list(input().split()))
v = 'aeiou'

for c in combinations(letters, L):
    flag = False
    s = 0
    for str in c:
        if str in v:
            flag = True
        else:
            s += 1
    if flag and s >= 2:
        print(''.join(c))