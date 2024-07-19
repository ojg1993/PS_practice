class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}

        for char in strs:
            target = "".join(sorted(char))
            if target not in res:
                res[target] = [char]
            else:
                res[target].append(char)
        return res.values()
