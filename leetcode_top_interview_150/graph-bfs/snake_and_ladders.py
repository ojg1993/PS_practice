class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """
        moving range: 1-6
        start from cell 1 and reach to length^2 cell
        if reached n^2 cell return cnt else return -1

        ** ladder | snake: if value of the cell is not -1 it can moves to the cell number **
        """
        length = len(board)
        board.reverse()

        def cell_to_coordinate(cell):
            cell -= 1
            y = cell // length
            x = cell % length
            if y % 2:
                x = length - 1 - x
            return y, x

        q, visit = deque(), set()
        q.append((1, 0))
        visit.add(1)

        while q:
            cell_num, cnt = q.popleft()

            for i in range(1, 7):
                new_cell_num = cell_num + i
                y, x = cell_to_coordinate(new_cell_num)
                if board[y][x] != -1:
                    new_cell_num = board[y][x]
                if new_cell_num == length * length:
                    return cnt + 1
                if new_cell_num not in visit:
                    q.append((new_cell_num, cnt + 1))
                    visit.add(new_cell_num)
        return -1
