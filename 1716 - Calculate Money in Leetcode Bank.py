class Solution:
    def totalMoney(self, n: int) -> int:
        res = 1
        curr = 1
        for i in range(1, n):
            if i % 7 == 0:
                curr = (i // 7)+1
                res += curr
            else:
                curr += 1
                res += curr

        return res