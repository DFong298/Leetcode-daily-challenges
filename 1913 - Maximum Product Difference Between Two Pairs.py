class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        mx1 = max(nums[0], nums[1]) #greatest max
        mx2 = min(nums[0], nums[1]) #second greatest max

        mn1 = min(nums[0], nums[1]) #smallest min
        mn2 = max(nums[0], nums[1]) #second smallest min

        for n in nums[2:]:
            if n > mx1:
                mx2 = mx1
                mx1 = n
            elif n > mx2:
                mx2 = n

            if n < mn1:
                mn2 = mn1
                mn1 = n
            elif n < mn2:
                mn2 = n

        return mx1*mx2 - mn1*mn2