class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        curr_max = 1
        for i in range(len(arr)-1):
            if arr[i+1] >= curr_max + 1:
                curr_max += 1

        return curr_max