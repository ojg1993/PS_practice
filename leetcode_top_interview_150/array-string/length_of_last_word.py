class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        for word in words[::-1]:
            if word != "":
                return len(word)


a = Solution()
print(a.lengthOfLastWord("   fly me   to   the moon  "))
