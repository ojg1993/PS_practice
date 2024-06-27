class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s
        res = ""

        for r in range(numRows):
            plus = (numRows-1) * 2
            for i in range(r, len(s), plus):
                res += s[i]
                if (r > 0 and r < numRows -1 and i + plus - 2 * r < len(s)):
                    res += s[i + plus - 2 * r]

        return res