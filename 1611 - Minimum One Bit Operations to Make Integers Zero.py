class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        ans = 0
        xors = []
        b = bin(n)

        for i in range(1, len(b)):
            if b[-i] == '1':
                xors.append(2**i - 1)

        for x in xors:
            ans ^= x
        return ans