class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2:
            return False

        parentheses = {'(': ')', "[": "]", "{": "}"}
        stk = []

        for char in s:
            if char in parentheses:
                stk.append(char)
            elif not len(stk) or parentheses[stk.pop()] != char:
                return False
        return not len(stk)