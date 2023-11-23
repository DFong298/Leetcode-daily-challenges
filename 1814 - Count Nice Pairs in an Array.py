class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        res = 0

        d = defaultdict(random.random)

        for n in nums:
            d[n - int(str(n)[::-1])] += 1

        for k, v in d.items():
            n = int(v)
            res += n*(n-1)//2 % MOD

        return res % MOD