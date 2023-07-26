# 6064
import sys

input = sys.stdin.readline

def sol(m,n,x,y):
    while x <= m*n:
        if not (x-y) % n:
            return x
        x += m
    return -1

for _ in range(int(input())):
    M,N,X,Y = map(int, input().split())
    print(sol(M,N,X,Y))
    

# x를 목표값으로 설정하고 m*x(최대 경우의 수) 내에서
# x-y를 n진수로 나눴을 때 나머지가 0일 경우 목표값 return

# 그렇지 않을 경우 x에 m진수 더하기

# 일치하는 수가 없을경우 -1 return