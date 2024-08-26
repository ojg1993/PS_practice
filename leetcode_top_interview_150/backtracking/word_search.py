class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(y, x, left):
            if not left:
                return True

            for yy, xx in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]:
                if 0 <= yy < M and 0 <= xx < N and board[yy][xx] == left[0]:
                    if (yy, xx) not in visit:
                        visit.add((yy, xx))
                        if dfs(yy, xx, left[1:]):
                            return True
                        visit.remove((yy, xx))
            return False

        M, N = len(board), len(board[0])
        visit = set()
        for i in range(M):
            for j in range(N):
                if board[i][j] == word[0]:
                    visit.add((i, j))
                    if dfs(i, j, word[1:]):
                        return True
                    visit.remove((i, j))
        return False
