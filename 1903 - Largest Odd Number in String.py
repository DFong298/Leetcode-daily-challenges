class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in reversed(range(len(num))):
            if int(num[i]) & 1:
              return num[:i+1]
        return ""