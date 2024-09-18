class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n >= 0:
            res = x ** n
        else:
            x = 1 / x
            res = x ** (n*-1)
        return res
