class Solution:
    # brute-force
    def longestPalindrome(self, s: str) -> str:
        def palindrome(left, right):
            while 0 <= left and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        res = ""
        for i in range(len(s)):
            res = max(res, palindrome(i, i), palindrome(i, i+1), key=len)
        return res
