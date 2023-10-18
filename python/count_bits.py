class Solution:
    def countBits(self, n: int) -> List[int]:
        # Runtime: 58 ms (Beats 98.29%)
        # Memory: 22.9 MB (Beats 98.26%)
      
        return [i.bit_count() for i in range(n+1)]
