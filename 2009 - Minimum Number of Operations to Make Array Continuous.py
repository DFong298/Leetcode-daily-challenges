class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        nums = sorted(set(nums))

        for i, x in enumerate(nums):
            end = x + n - 1
            j = bisect_right(nums, end)
            contCnt = j - i
            ans = min(ans, n - contCnt)

        return ans