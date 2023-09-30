# 16929
import sys
sys.setrecursionlimit(10**6)
def input():
    return sys.stdin.readline().rstrip()


def dfs(y, x, py, px, depth):
    if visited[y][x] and depth > 3:
        print('Yes')
        exit()
    visited[y][x] = 1
    
    for dy, dx in d:
        ny, nx = y + dy, x + dx
        
        if 0 <= ny < n and 0 <= nx < m and board[y][x] == board[ny][nx]:
            if (ny, nx) != (py, px):
                dfs(ny, nx, y, x, depth+1)
        

if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [input() for _ in range(n)]
    d = [(-1,0), (1,0), (0,-1), (0,1)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                dfs(i, j, i, j, 1)
    print('No')