class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = curr_min = nums[k]
        i = j = k
        while i >= 0 or j < n:
            curr_min = min(curr_min, nums[i], nums[j])
            ans = max(ans, curr_min*(j-i+1))
            if i == 0 and j == n-1:
                break
            elif i == 0 and j < n-1:
                j += 1
                continue
            elif i > 0 and j == n-1:
                i -= 1
                continue

            if nums[i-1] > nums[j+1]:
                i -= 1
            elif nums[i-1] < nums[j+1]:
                j += 1
            else:
                i -= 1
                j += 1

        return ans
