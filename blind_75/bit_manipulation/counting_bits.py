class Solution:
    def countBits(self, n: int) -> List[int]:
        def hammingWeight(n: int) -> int:
            weight = 0

            for i in range(32):
                weight += n >> i & 1
            
            return weight
        
        ans = []
        for i in range(n + 1):
            ans.append(hammingWeight(i))

        return ans
