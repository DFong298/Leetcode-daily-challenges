class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen = {}
        pairs = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
                pairs[num] += seen[num]
            else:
                seen[num] = 0
                pairs[num] = 0

        return sum(i for i in pairs.values())
