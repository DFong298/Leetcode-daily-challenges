class Solution:
    def hammingWeight(self, n: int) -> int:
        i = 0b11111111111111111111111111111111
        return (n & i).count('1')