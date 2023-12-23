class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        s = 0
        for i in range(len(piles)//3):
            a = piles.pop()
            s += piles.pop()
        return s