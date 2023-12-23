class Solution:
    def maxScore(self, s: str) -> int:
        l = s[0] == '0'
        r = s[1:].count('1')
        curr = l + r
        for i in range(1, len(s)-1):
            if s[i] == '0':
                l += 1
            elif s[i] == '1':
                r -= 1
            curr = max(curr, l+r)
        return curr