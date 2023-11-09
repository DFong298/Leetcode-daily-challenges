MOD = 10**9 + 7
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr = set(arr)
        factorPairs = defaultdict(set)

        for x in arr:
            for p in arr:
                if x != p and x % p == 0 and x // p in arr:
                    factorPairs[x].add((p, x // p))

        @cache
        def numWays(x):
            ans = 1
            for p, q in factorPairs[x]:
                ans = (ans + numWays(p) * numWays(q)) % MOD
            return ans

        ans = 0
        for root in arr:
            ans = (ans + numWays(root)) % MOD
        return ans