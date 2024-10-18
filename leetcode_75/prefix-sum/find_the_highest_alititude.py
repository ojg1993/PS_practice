class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prev, res = 0, 0

        for i in range(len(gain)):
            gain[i], prev = prev, prev + gain[i]
            res = max(res, gain[i])
        return res
