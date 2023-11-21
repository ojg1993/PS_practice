class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2:
            return False

        parentheses = {'(': ')', "[": "]", "{": "}"}
        stk = []

        for char in s:
            if char in parentheses.keys():
                stk.append(char)
            elif not len(stk) or parentheses[stk.pop()] != char:
                return False
        return not len(stk)

    """
    1. Make a dictionary of parenthese pairs
    2. Loop through input s
        a. if char in parentheses.keys() -> append to stk
        b. if stk is empty or parentheses[stk.pop()] doesn't matches char -> return False 
    3. return True if stk is empty or return False
    
    """