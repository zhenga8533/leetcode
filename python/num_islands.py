class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Runtime: 282 ms (Beats 68.54%)
        # Memory: 19 MB (Beats 54.82%)
      
        def countLand(row, col):
            if grid[row][col] == "0":
                return
            grid[row][col] = "0"

            dirs = [
                (max(0, row - 1), col),
                (min(len(grid) - 1, row + 1), col),
                (row, max(0, col - 1)),
                (row, min(len(grid[0]) - 1, col + 1))
            ]
            for dir in dirs:
                countLand(dir[0], dir[1])

        islands = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    countLand(row, col)
                    islands += 1
        
        return islands
        
