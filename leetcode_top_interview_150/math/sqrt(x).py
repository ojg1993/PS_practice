class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x

        while l <= r:
            m = (l+r) // 2
            p_m = m*m
            if p_m == x:
                return m
            elif p_m < x:
                l = m + 1
                res = m
            else:
                r = m - 1
        return res

        # res = 1
        # while res * res <= x:
        #     res += 1
        # return res - 1
