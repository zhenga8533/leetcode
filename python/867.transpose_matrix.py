class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        transposed = []

        for i in range(m):
            row = []
            for j in range(n):
                row.append(matrix[j][i])
            transposed.append(row)
        
        return transposed
