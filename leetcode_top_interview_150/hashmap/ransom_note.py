class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hash_table = {}

        for s in magazine:
            if s in hash_table:
                hash_table[s] += 1
            else:
                hash_table[s] = 1

        for s in ransomNote:
            if s in hash_table:
                hash_table[s] -= 1
                if hash_table[s] < 0:
                    return False
            else:
                return False
        return True
