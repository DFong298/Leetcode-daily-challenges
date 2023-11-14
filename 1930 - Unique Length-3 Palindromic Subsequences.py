class Solution(object):
    def countPalindromicSubsequence(self, s) -> int:
        d = defaultdict(list)
        for i, c in enumerate(s):
            d[c].append(i)
        res = 0
        
        for c in d:
            if len(d[c]) < 2:
                continue
            a = d[c][0]
            b = d[c][-1]
            res += len(set(s[a+1:b]))

        return(res)
		