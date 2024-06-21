class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        roman = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
        }
        roman_array = [num for num in roman.keys()]
        i = len(roman_array) - 1
        while num:
            if num >= roman_array[i]:
                num -= roman_array[i]
                res += roman[roman_array[i]]
            else:
                i -= 1
        res = res.replace("DCCCC", "CM").replace("CCCC", "CD")
        res = res.replace("LXXXX", "XC").replace("XXXX", "XL")
        res = res.replace("VIIII", "IX").replace("IIII", "IV")
        return res


a = Solution()
print(a.intToRoman(1994))
