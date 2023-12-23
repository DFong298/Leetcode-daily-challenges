class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n, l, r, res = len(nums), 0, sum(nums[:len(nums)+1]), []
        for i in range(len(nums)):
            res.append((i*nums[i] - l) + (r - (n-i)*nums[i]))
            l += nums[i]
            r -= nums[i]

        return res