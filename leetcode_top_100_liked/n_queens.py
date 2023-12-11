class Solution:
    def solveNQueens(self, n: int):
        def backtrack(row):
            if row == n:
                res.append(["".join(row) for row in board])
                return
            for col in range(n):
                _sum = row+col
                diff = row-col

                if not (col in visit_col or _sum in visit_pd or diff in visit_nd):
                    visit_col.add(col)
                    visit_pd.add(_sum)
                    visit_nd.add(diff)
                    board[row][col] = 'Q'

                    backtrack(row+1)
                    visit_col.remove(col)
                    visit_pd.remove(_sum)
                    visit_nd.remove(diff)
                    board[row][col] = '.'

        res = []
        board = [['.'] * n for _ in range(n)]
        visit_col = set()
        visit_pd = set()
        visit_nd = set()
        backtrack(0)
        return res

a = Solution()
print(a.solveNQueens(4))