class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        flipped = []
        n = len(image)

        for i in range(n):
            row = []
            for j in range(n - 1, -1, -1):
                row.append((image[i][j] + 1) % 2)
            flipped.append(row)

        return flipped
        
