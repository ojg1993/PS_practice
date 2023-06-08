# 10828

import sys

input = sys.stdin.readline
n = int(input())
stack=[]

for i in range(n):
    a = input().split()
    
    if a[0] == 'push':
        stack.append(a[1])
    elif a[0] == 'pop':
        if not len(stack):
            print(-1)
        else:
            print(stack.pop())
    elif a[0] == 'size':
        print(len(stack))
    elif a[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif a[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)