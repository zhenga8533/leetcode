class Solution:
    def numSquares(self, n: int, mem = []) -> int:
        if len(mem) == 0:
            mem = [-1] * (n + 1)
        if n == 0:
            return 0
        if n < 0:
            return float("inf")
        if mem[n] != -1:
            return mem[n]
        
        ans = n

        i = 1
        while i * i <= n:
            ans = min(ans, self.numSquares(n - (i * i), mem))
            i += 1
        
        mem[n] = ans + 1
        return ans + 1
        
