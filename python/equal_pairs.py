class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

        Runtime: 477 ms (Beats 46.98%)
        Memory: 17.7 MB (Beats 37.33%)
        """

        trans = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
        count = 0
        for row in grid:
            for col in trans:
                if row == col:
                    count += 1
        return count
        
