class Solution:
    def reverseBits(self, n: int) -> int:
        # Runtime: 32 ms (Beats 93.9%)
        # Memory: 16.2 MB (Beats 34.35%)
      
        rev = 0
        for _ in range(32):
            rev |= n&1
            rev <<= 1
            n >>= 1
        
        rev >>= 1
        return rev
        
