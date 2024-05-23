class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Runtime: 39 ms (Beats 66.59%)
        # Memory: 16.1 MB (Beats 87.18%)
      
        triangle = [[1]]

        for i in range(1, numRows):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            triangle.append(row)

        return triangle
        
