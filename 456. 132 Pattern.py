class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        s = []
        min_val = float('inf')
        
        for n in nums:
            while s and s[-1][0] <= n:
                s.pop()

            if s and s[-1][1] < n:
                return True
                
            min_val = min(min_val, n)
            s.append([n, min_val])
            
        return False