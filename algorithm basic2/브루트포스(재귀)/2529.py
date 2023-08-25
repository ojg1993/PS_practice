# 2529

import sys
def input():
    return sys.stdin.readline().rstrip()

def check(a, b, op):
    if op == '<':
        return a < b
    else:
        return a > b


def dfs(depth, num):
    if depth == n+1:
        ans.append(num)
        return
    else:
        for i in range(10):
            if not visit[i]:
                if not depth or check(num[depth-1], str(i), signs[depth-1]):
                    visit[i] = True
                    dfs(depth+1, num+str(i))
                    visit[i] = False



if __name__ == '__main__':
    n = int(input())
    signs = list(input().split())
    visit = [False] * 10
    ans = []
    dfs(0, '')
    print(ans[-1])
    print(ans[0])