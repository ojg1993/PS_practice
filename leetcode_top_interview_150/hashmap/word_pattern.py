class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split()
        zipped = zip(pattern, s)
        return len(set(zipped)) == len(set(pattern)) == len(set(s)) and len(pattern) == len(s)
