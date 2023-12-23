class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i, p in enumerate(points[:-1]):
            res += max(abs(p[0] - points[i+1][0]), abs(p[1] - points[i+1][1]))

        return res