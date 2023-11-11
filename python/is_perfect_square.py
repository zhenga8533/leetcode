class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Runtime: 36 ms (Beats 74.28%)
        # Memory: 16.2 MB (Beats 65.33%)
      
        return (num ** 0.5).is_integer()
        
