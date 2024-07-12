class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        res = []
        left, top, right, bottom = 0, 0, len(matrix[0]) - 1, len(matrix) - 1

        while left <= right and top <= bottom:
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1

            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1

            if top <= bottom:
                for c in range(right, left - 1, -1):
                    res.append(matrix[bottom][c])
                bottom -= 1

            if left <= right:
                for r in range(bottom, top - 1, -1):
                    res.append(matrix[r][left])
                left += 1
        return res
