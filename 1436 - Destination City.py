class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s = set()
        t = set()
        for p in paths:
            s.add(p[0])
            t.add(p[1])
        return next(iter(t-s))
