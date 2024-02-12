class Solution:
    def arrangeCoins(self, n: int) -> int:
        steps = 0

        while n > 0:
            steps += 1
            n -= steps
        
        return steps - (n < 0)
        
