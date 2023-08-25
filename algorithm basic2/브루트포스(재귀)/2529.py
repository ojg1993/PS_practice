# 2529

import sys
def input():
    return sys.stdin.readline().rstrip()

def check(a, b, op):
    if op == '<':
        if a > b: return False
    elif op == '>':
        if a < b: return False
    return True


def dfs(cnt, num):
    if cnt == n+1:
        ans.append(num)
        return
    else:
        for i in range(10):
            if visit[i]: continue

            if not cnt or check(num[cnt-1], str(i), signs[cnt-1]):
                visit[i] = True
                dfs(cnt+1, num+str(i))
                visit[i] = False



if __name__ == '__main__':
    n = int(input())
    signs = list(input().split())
    visit = [False] * 10
    ans = []
    dfs(0, '')
    ans.sort()
    print(ans[-1])
    print(ans[0])