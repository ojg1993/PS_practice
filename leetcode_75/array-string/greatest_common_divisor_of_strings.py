class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        if len(str1) == len(str2):
            return str1
        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        return self.gcdOfStrings(str1, str2[len(str1):])

        # l1, l2 = len(str1), len(str2)
        # def isDivisior(l):
        #     if l1 % l or l2 % l:
        #         return False
        #     f1, f2 = l1 // l, l2 // l
        #     return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

        # for l in range(min(l1, l2), 0, -1):
        #     if isDivisior(l):
        #         return str1[:l]
        # return ""
