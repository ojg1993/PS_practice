class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        res = []
        carry = 1
        for num in digits[::-1]:
            tmp = num+carry
            res.append(tmp % 10)
            carry = tmp//10
        if carry:
            res.append(carry)
        return res[::-1]
