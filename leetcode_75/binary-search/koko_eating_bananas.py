class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            hrs = 0
            m = (l + r) // 2

            for p in piles:
                hrs += ceil(p / m)
                if hrs > h:
                    l = m + 1
                    break
            if hrs <= h:
                r = m - 1
        return l
