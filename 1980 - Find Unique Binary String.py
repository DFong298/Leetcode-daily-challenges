class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        curr_index = 0
        res = ""
        for s in nums:
            if s[curr_index] == '0':
                res += '1'
            else:
                res += '0'
            curr_index += 1

        return res