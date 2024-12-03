class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            if not n:
                return 0
            return 1

        i, j, h = 0, 1, 1

        for _ in range(3, n+1):
            i, j, h = j, h, i + j + h
        return h
