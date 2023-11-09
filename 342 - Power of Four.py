class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return (n & n-1) == 0 and (n & 0b01010101010101010101010101010101 != 0)
