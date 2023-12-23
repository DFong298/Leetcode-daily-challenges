class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        hor = len(matrix)
        vert = len(matrix[0])
        res = [[0]*hor for _ in range(vert)]

        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                res[i][j] = matrix[j][i]
        
        return res