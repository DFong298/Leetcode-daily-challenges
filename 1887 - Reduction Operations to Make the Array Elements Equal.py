class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        res = 0
        s = 0
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                res += s
            else:
                s += 1
                res += s
        return res