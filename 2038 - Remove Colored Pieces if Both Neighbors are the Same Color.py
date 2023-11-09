class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a = 0
        b = 0
        
        for i in range(1, len(colors)-1):
            if colors[i] ==  colors[i-1] == colors[i+1]:
                if colors[i] == 'A':
                    a += 1
                elif colors[i] == 'B':
                    b += 1
                
        return a > b