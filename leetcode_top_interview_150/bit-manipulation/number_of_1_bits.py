class Solution:
    def hammingWeight(self, n: int) -> int:
        set_bits = 0

        for _ in range(32):
            bit = n & 1
            if bit:
                set_bits += 1
            n >>= 1
        return set_bits
