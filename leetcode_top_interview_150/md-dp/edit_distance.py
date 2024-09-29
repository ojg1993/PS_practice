class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        operations = [insert, remove, replace]
        1. w1[i] = w2[j]  -> 0 operation -> dp[i][j] = dp[i+1][j+1]
        2. w1[i] != w2[j] -> 1 operation -> dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
        """
        dp = [[0 for _ in range(len(word1)+1)] for _ in range(len(word2)+1)]

        for i in range(len(word1)+1):
            dp[-1][i] = len(word1) - i

        for i in range(len(word2)+1):
            dp[i][-1] = len(word2) - i

        for y in range(len(word2)-1, -1, -1):
            for x in range(len(word1)-1, -1, -1):
                if word1[x] == word2[y]:
                    dp[y][x] = dp[y+1][x+1]
                else:
                    dp[y][x] = min(dp[y+1][x], dp[y][x+1], dp[y+1][x+1]) + 1
        return dp[0][0]
