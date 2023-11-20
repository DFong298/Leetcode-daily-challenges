class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        mx = 0
        nums.sort()
        i = 0
        j = len(nums) - 1
        while i < j:
            mx = max(mx, nums[i] + nums[j])
            i += 1
            j -= 1

        return mx