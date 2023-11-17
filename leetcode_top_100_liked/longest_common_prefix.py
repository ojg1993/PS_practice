class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        ans=""
        strs.sort()

        for i in range(len(min(strs[0], strs[-1]))):
            if strs[0][i] != strs[-1][i]:
                return ans
            else:
                ans += strs[0][i]
        return ans