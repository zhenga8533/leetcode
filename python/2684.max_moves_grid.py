class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * m
        moves = 0

        for x in range(1, n):
            lt = 0
            found = False

            for y in range(m):
                curr = -1
                nlt = dp[y]
                
                if y - 1 >= 0 and lt != -1 and grid[y][x] > grid[y-1][x-1]:
                    curr = max(curr, lt + 1)
                if dp[y] != -1 and grid[y][x] > grid[y][x-1]:
                    curr = max(curr, dp[y] + 1)
                if y + 1 < m and dp[y+1] != -1 and grid[y][x] > grid[y+1][x-1]:
                    curr = max(curr, dp[y+1] + 1)
                
                dp[y] = curr
                found = found or (dp[y] != -1)
                lt = nlt
            
            if not found:
                break
            moves = x

        return moves
        
