class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n, m = len(img), len(img[0])
        def smooth(ci, cj):
            cnt = tot = 0
            for i in (ci-1, ci, ci+1):
                for j in (cj-1, cj, cj+1):
                    if 0 <= i < n and 0 <= j < m:
                        cnt += 1
                        tot += img[i][j]
            return tot // cnt
        
        return [[smooth(i, j) for j in range(m)] for i in range(n)]