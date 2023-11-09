class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start = sorted([s[0] for s in flowers])
        end = sorted([e[1] for e in flowers])

        ans = []

        for p in people:
            ans.append(bisect_right(start, p) - bisect_left(end, p))
        return ans