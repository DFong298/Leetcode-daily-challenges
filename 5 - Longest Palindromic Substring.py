#BAD SOLUTION

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(string):
            return string == string[::-1]

        dp = ["" for _ in range(len(s))]
        dp[0] = s[0]
        curr_best = 0

        for i in range(1, len(s)):
            for j in range(i):
                if i-j+1 > curr_best:
                    if isPalindrome(s[j:i+1]):
                        print(s[j:i+1])
                        dp[i] = s[j:i+1]
                        break
                else:
                    break

        ans = ""
        for string in dp:
            if len(string) > len(ans):
                ans = string

        return ans
