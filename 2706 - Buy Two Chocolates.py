class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        mn1 = min(prices[0], prices[1])
        mn2 = max(prices[0], prices[1])

        for p in prices[2:]:
            if p < mn1:
                mn2, mn1 = mn1, p
            elif p < mn2:
                mn2 = p

        if money >= mn1 + mn2: 
            return money - (mn1 + mn2)
        else:
            return money