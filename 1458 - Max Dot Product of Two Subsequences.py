class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0 for _ in range(len(nums2))] for _ in range(len(nums1))]

        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)
        
        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if i == j == 0:
                    dp[i][j] = max(0, nums1[i]*nums2[j])
                elif i == 0:
                    dp[i][j] = max(dp[i][j-1], nums1[i]*nums2[j])
                elif j == 0:
                    dp[i][j] = max(dp[i-1][j], nums1[i]*nums2[j])
                else:
                    dp[i][j] = max(dp[i-1][j-1] + nums1[i]*nums2[j],
                                   dp[i][j-1], dp[i-1][j])

        return dp[-1][-1]