class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = [1]

        for i in range(rowIndex + 1):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = prev[j - 1] + prev[j]
            prev = row
        
        return prev
        
