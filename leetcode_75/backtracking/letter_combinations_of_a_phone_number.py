class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        num_to_word = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def backtrack(digits, chars):
            if not digits:
                return res.append(chars)
            for c in num_to_word[digits[0]]:
                backtrack(digits[1:], chars + c)

        res = []
        backtrack(digits, "")
        return res
