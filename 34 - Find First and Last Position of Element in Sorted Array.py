class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i = bisect_left(nums, target)
        j = bisect_right(nums, target)-1
        if i < len(nums) and nums[i] == target:
            return [i, j]
        else:
            return [-1, -1]