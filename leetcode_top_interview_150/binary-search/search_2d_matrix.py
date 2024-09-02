class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])
        l, r = 0, M * N - 1

        while l <= r:
            mid = (l + r) // 2
            min_val = matrix[mid // N][mid % N]

            if min_val == target:
                return True
            elif min_val < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
