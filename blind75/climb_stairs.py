class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        l = 0
        r = 1

        for i in range(1, n + 1):
            current = r + l
            l = r
            r = current
        
        return r
        
