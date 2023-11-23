class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for i, j in zip(l, r):
            r = sorted(nums[i:j+1])
            for k in range(1, len(r)-1):
                if r[k+1] - r[k] != r[1] - r[0]:
                    res.append(False)
                    break
            else:
                res.append(True)
        return res