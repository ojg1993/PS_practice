class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""

        for a, b in zip(word1, word2):
            res += a + b
        res += word1[len(word2):]
        res += word2[len(word1):]
        return res
