class Solution:
    def trailingZeroes(self, n: int) -> int:
        if not n: return n
        
        # # O(logN)
        cnt = 0
        while n:
            n //= 5
            cnt += n
        return cnt

        # # O(N)
        # import sys
        # sys.set_int_max_str_digits(10000)

        # fact = 1
        # for num in range(2, n+1):
        #     fact *= num

        # fact = str(fact)
        # cnt = 0
        # for i in range(len(fact)-1, -1, -1):
        #     if fact[i] != "0":
        #         return cnt
        #     else:
        #         cnt += 1
        