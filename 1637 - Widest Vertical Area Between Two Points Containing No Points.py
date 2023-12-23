class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(reverse=True, key=lambda x: x[0])
        return max(p1[0]-p2[0] for p1, p2 in zip(points, points[1:]))