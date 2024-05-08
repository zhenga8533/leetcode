class Solution:
    def hammingWeight(self, n: int) -> int:
        weight = 0

        for i in range(32):
            weight += n >> i & 1
        
        return weight
        
