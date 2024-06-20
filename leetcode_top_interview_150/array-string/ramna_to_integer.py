class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        res = 0

        for p in range(len(s)):
            if p + 1 < len(s) and roman[s[p]] < roman[s[p + 1]]:
                res -= roman[s[p]]
            else:
                res += roman[s[p]]

        # s = s.replace("IV", "IIII").replace("IX", "VIIII")
        # s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        # s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

        # for char in s:
        #     res += roman[char]

        return res


a = Solution()
a.romanToInt("MCMXCIV")
