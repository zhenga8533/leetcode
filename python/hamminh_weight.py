class Solution:
    def hammingWeight(self, n: int) -> int:
        # Runtime: 35 ms (Beats 79.77%)
        # Memory: 16.2 MB (Beats 27.70%)
      
        count = 0

        while n > 0:
            count += 1
            n = n & (n-1)
        
        return count
        
