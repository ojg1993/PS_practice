class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(y, x):
            if board[y][x] == "O":
                board[y][x] = "V"
                for yy, xx in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]:
                    if 0 <= yy < M and 0 <= xx < N and board[yy][xx] == "O":
                        dfs(yy, xx)

        M, N = len(board), len(board[0])

        for i in range(M):
            dfs(i, 0)
            dfs(i, N - 1)
        for j in range(N):
            dfs(0, j)
            dfs(M - 1, j)

        for y in range(M):
            for x in range(N):
                if board[y][x] == "O":
                    board[y][x] = "X"
        for y in range(M):
            for x in range(N):
                if board[y][x] == "V":
                    board[y][x] = "O"
