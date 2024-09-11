class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        a, b = a[::-1], b[::-1]
        al, bl = len(a), len(b)

        for i in range(max(al, bl)):
            ad = int(a[i]) if i < al else 0
            bd = int(b[i]) if i < bl else 0

            tot = ad + bd + carry
            res = str(tot % 2) + res
            carry = tot // 2
        return "1" + res if carry else res
