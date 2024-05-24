class Solution:
    def reverseBits(self, n: int) -> int:
        rev = 0
        for _ in range(32):
            rev |= n&1
            rev <<= 1
            n >>= 1
        
        rev >>= 1
        return rev
        
