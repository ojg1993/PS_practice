class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        cnt, res = 0, 0
        vowels = set(['a', 'e', 'i', 'o', 'u'])

        for i in range(len(s)):
            if i >= k and s[i-k] in vowels:
                cnt -= 1
            if s[i] in vowels:
                cnt += 1
            res = max(res, cnt)
        return res
