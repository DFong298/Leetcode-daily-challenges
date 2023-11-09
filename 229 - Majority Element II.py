class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) // 3
        c = Counter(nums)
        res = []
        for key in c.keys():
            if c[key] > n:
                res.append(key)

        return res