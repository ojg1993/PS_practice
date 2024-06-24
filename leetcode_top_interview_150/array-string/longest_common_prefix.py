class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""

        for i in range(len(strs[0])):
            for word in strs:
                if i == len(word) or word[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
