# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        lo, hi = 0, n - 1

        # find the peak
        while lo < hi:
            mid = (hi + lo) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid+1):
                lo = peak = mid+1
            else:
                hi = mid

        lo, hi = 0, peak

        # maybe target in left side of peak?
        while lo <= hi:
            mid = (lo + hi) // 2
            if mountain_arr.get(mid) < target:
                lo = mid + 1
            elif mountain_arr.get(mid) > target:
                hi = mid - 1
            else:
                return mid

        # nvm its in right side (maybe?)
        lo, hi = peak, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if mountain_arr.get(mid) > target:
                lo = mid + 1
            elif mountain_arr.get(mid) < target:
                hi = mid - 1
            else:
                return mid

        # ok nvm its not in the arr lol
        return -1
