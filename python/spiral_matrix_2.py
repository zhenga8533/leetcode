class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Runtime: 34 ms (Beats 87.51%)
        # Memory: 16.1 MB (Beats 86.17%)
      
        # positional variables
        r = 0
        c = -1
        num = 1

        # directional variables
        direction = 1
        change = n
        count = 1

        # spiral matrix
        spiral = [[0 for _ in range(n)] for _ in range(n)]

        while change > 0:
            # go until limit in one of four directions
            for i in range(change):
                c += (direction % 2) * direction
                r += int(direction / 2)
                spiral[r][c] = num
                num += 1
            
            # change direction after loop
            direction = 2 if direction == 1 else \
                -1 if direction == 2 else \
                -2 if direction == -1 else 1

            # change direction after first travel and every other travel after
            count += 1
            if count % 2 == 0:
                count = 0
                change -= 1

        return spiral
