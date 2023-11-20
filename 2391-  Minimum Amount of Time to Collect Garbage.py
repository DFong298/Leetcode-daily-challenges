# horrible solution for horrible question

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        g, m, p = 0, 0, 0
        res = 0

        for j in range(len(garbage)):
            if 'G' in garbage[j]: g = j
            if 'M' in garbage[j]: m = j
            if 'P' in garbage[j]: p = j

        for i, s in enumerate(garbage):
            if i != 0:
                res += travel[i-1]
            res += s.count('G')   
            if i == g: break 

        for i, s in enumerate(garbage):
            if i != 0:
                res += travel[i-1]
            res += s.count('M')
            if i == m: break 

        for i, s in enumerate(garbage):
            if i != 0:
                res += travel[i-1]
            res += s.count('P') 
            if i == p: break 
            
        return res

        