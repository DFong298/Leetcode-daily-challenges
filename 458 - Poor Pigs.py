class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        n = 1 + minutesToTest // minutesToDie 
        for i in range(buckets):
            if n**i >= buckets:
                return i
        return 0