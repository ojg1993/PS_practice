class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        smap = dict()

        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in smap:
                smap[sorted_s] = [s]
            else:
                smap[sorted_s].append(s)
        return smap.values()