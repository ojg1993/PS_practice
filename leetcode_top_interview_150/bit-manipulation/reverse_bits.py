class Solution:
    def reverseBits(self, n: int) -> int:
        r_n = 0

        for _ in range(32):
            r_n <<= 1  # 0
            bit = n & 1  # 0 or 1
            r_n |= bit  # 0 or 1
            n >>= 1  # shifting n to the right by 1
        return r_n
