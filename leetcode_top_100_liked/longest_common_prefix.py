class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        ans=""
        strs.sort()
        l = strs[0]
        r = strs[-1]

        for i in range(len(min(l, r))):
            if l[i] != r[i]:
                return ans
            else:
                ans += l[i]
        return ans