# 11723

import sys
def input():
    return sys.stdin.readline().rstrip()

M = int(input())
S = set()

for i in range(M):
    command = input().split()

    if len(command) == 1:
        cal = command[0]
        if cal == 'all':
            S = set(range(1, 21))
            
        elif cal == 'empty':
            S.clear()
            
    else:
        cal, val = command
        val = int(val)
    
        if cal == 'add':
            S.add(val)
            
        elif cal == 'remove':
            S.discard(val)
            
        elif cal == 'check':
            print(1 if val in S else 0)
            
        elif cal == 'toggle':
            if val in S:
                S.discard(val)
            else:
                S.add(val)