class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        matrix = [[int(x) for x in row] for row in matrix]
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i and j and matrix[i][j]:
                    matrix[i][j] = 1 + \
                        min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])
                res = max(res, matrix[i][j])
        return res*res
