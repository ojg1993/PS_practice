class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1])


a = Solution()
print(a.lengthOfLastWord("   fly me   to   the moon  "))
