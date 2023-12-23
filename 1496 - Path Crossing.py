class Solution:
    def isPathCrossing(self, path: str) -> bool:
        curr = [0, 0]
        s = set()
        s.add((0, 0))

        for p in path:
            if p == 'N':
                curr[1] += 1
            elif p == 'S':
                curr[1] -= 1
            elif p == 'W':
                curr[0] -= 1
            elif p == 'E':
                curr[0] += 1
            if tuple(curr) in s:
                return True
            else: s.add(tuple(curr))

        return False
