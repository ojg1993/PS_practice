class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        i : 0 1 2 3 4 5 6 7 8
        s : l e e t c o d e
        dp: F F F F F F F F T

        at 4th idx iteration, 4+4 <= 8 and s[4:4+4] == code
        -> dp[4] = dp[4+4] -> T
        at 8th idx iteration, 0+4 <= 8 and s[0:0+4] == leet
        -> dp[0] = dp[0+4] -> T
        """
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]
