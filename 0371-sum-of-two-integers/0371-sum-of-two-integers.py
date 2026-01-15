class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32nd bit mask to handle Python's arbitrary precision
        mask = 0xFFFFFFFF
        while b & mask:
            # XOR gives the sum without carry
            # AND + shift gives the carry
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        # If a is positive, return a & mask
        # If a is negative, we need to handle the 32-bit two's complement
        return a & mask if b > 0 else a