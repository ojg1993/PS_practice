class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        0 to 0 = 0
        1 to 0 = 1
        0 to 1 = 2
        1 to 1 = 3
        """
        M, N = len(board), len(board[0])

        def cnt_neighbours(row, col):
            cnt = 0
            for r in range(row - 1, row + 2):
                for c in range(col - 1, col + 2):
                    if r < 0 or c < 0 or r == M or c == N or (r == row and c == col):
                        continue
                    if board[r][c] in [1, 3]:
                        cnt += 1
            return cnt

        for r in range(M):
            for c in range(N):
                cnt = cnt_neighbours(r, c)

                if board[r][c] and cnt in [2, 3]:
                    board[r][c] = 3
                elif cnt == 3:
                    board[r][c] = 2

        for r in range(M):
            for c in range(N):
                if board[r][c] == 1:
                    board[r][c] = 0
                elif board[r][c] in [2, 3]:
                    board[r][c] = 1
