class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Runtime: 30 ms (Beats 96.36%)
        # Memory: 16 MB (Beats 91.20%)

        if n == 0:
            return False

        while n != 1:
            n /= 2
            if not n.is_integer():
                return False
        
        return True
        
