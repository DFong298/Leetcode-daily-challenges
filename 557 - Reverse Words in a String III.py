class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        res = ""
        
        for word in arr:
            res += word[::-1] + " "
            
        return res[:-1]