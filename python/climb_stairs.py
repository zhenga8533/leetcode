class Solution:
    def climbStairs(self, n: int) -> int:
        # Runtime: 30 ms (Beats 92.76%)
        # Memory: 16.2 MB (Beats 40.90%)
      
        if n <= 3:
            return n

        l = 0
        r = 1

        for i in range(1, n + 1):
            current = r + l
            l = r
            r = current
        
        return r
        
