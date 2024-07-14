class Solution(object):
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        rowZero = False

        for row in range(m):
            for col in range(n):
                if not matrix[row][col]:
                    matrix[0][col] = 0
                    if not row:
                        rowZero = True
                    else:
                        matrix[row][0] = 0

        for row in range(1, m):
            for col in range(1, n):
                if not matrix[0][col] or not matrix[row][0]:
                    matrix[row][col] = 0

        if not matrix[0][0]:
            for row in range(m):
                matrix[row][0] = 0

        if rowZero:
            for col in range(n):
                matrix[0][col] = 0
