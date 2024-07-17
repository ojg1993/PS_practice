class Solution(object):
    def isIsomorphic(self, s, t):
        # s_to_t = {}
        # t_to_s = {}

        # for i in range(len(s)):
        #     if s[i] not in s_to_t and t[i] not in t_to_s:
        #         s_to_t[s[i]] = t[i]
        #         t_to_s[t[i]] = s[i]
        #     elif s_to_t.get(s[i]) != t[i] or t_to_s.get(t[i]) != s[i]:
        #         return False
        # return True

        zipped_set = set(zip(s, t))
        return len(zipped_set) == len(set(s)) == len(set(t))
