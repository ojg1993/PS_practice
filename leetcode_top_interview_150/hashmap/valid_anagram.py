from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt_map = defaultdict(int)

        for char in s:
            cnt_map[char] += 1

        for char in t:
            cnt_map[char] -= 1

        for val in cnt_map.values():
            if val:
                return False
        return True
