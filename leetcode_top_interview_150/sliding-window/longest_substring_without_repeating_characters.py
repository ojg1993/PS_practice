class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0

        left, right = 0, 0
        hash_map = set()
        res = 0

        while right < len(s):
            if s[right] in hash_map:
                hash_map.remove(s[left])
                left += 1
            else:
                hash_map.add(s[right])
                right += 1
                res = max(res, right - left)
        return res
