class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # matrix.reverse()

        # for i in range(len(matrix)):
        #     for j in range(i):
        #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        matrix[:] = [[row[i] for row in matrix[::-1]] for i in range(len(matrix))]


a = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a.rotate(matrix)
