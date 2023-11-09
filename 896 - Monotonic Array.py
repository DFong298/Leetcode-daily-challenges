class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = False
        dec = False

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc = True
            if nums[i] < nums[i-1]:
                dec = True
            
            if inc and dec:
                return False

        return True
