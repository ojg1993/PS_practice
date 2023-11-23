class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def backtrack(left, right, s):
            if not left and not right:
                res.append(s)
            if left > 0:
                backtrack(left - 1, right, s + "(")
            if left < right:
                backtrack(left, right - 1, s + ")")

        res = []
        backtrack(n, n, "")
        return res