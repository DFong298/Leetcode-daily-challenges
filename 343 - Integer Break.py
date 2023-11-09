class Solution:
    def integerBreak(self, n: int) -> int:
        simple_case = [1, 2, 4] # n = 2, 3, 4
        if n in range(2, 5):
            return simple_case[n-2]

        if n % 3 == 0:
            return int(3 ** (n/3))
    
        if n % 3 == 1:
            return int(4 * 3**((n-4)/3))

        if n % 3 == 2:
            return int(2 * 3**((n-2)/3))