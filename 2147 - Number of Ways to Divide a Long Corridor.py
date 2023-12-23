class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        s_count = 0
        p_count = 0
        p = 0
        curr = 0

        for i in range(len(corridor)):
            if corridor[i] == 'S':
                s_count += 1
                if s_count & 1:
                    p = p_count
                else:
                    if s_count == 2:
                        curr = 1
                    else:
                        curr = ((1+p)*curr) % MOD
                    p_count = 0
            else:
                p_count += 1
        
        if s_count & 1: return 0

        return curr % MOD