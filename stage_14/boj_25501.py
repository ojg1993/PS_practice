# 25501

arr = [ input() for i in range(int(input()))]

def recursion(s, l, r):
    if l >= r:
        return [1, l+1]
    elif s[l] != s[r]:
        return [0, l+1]
    else:
        return recursion(s, l+1, r-1)

def is_palin(s):
    return recursion(s, 0, len(s)-1)

for s in arr:
    print(*is_palin(s))