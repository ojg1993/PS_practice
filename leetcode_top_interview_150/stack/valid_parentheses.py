class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        for char in s:
            if char in ["(", "{", "["]:
                stk.append(char)
            else:
                if not stk:
                    return False
                elif char == ")" and stk.pop() != "(":
                    return False
                elif char == "}" and stk.pop() != "{":
                    return False
                elif char == "]" and stk.pop() != "[":
                    return False
        if stk:
            return False
        return True
