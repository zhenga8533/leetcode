class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Runtime: 112 ms (Beats 97.9%)
        # Memory: 17.6 MB (Beats 81.18%)
      
        n = len(nums)
        total = int(n * (n + 1) / 2)
        
        for num in nums:
            total -= num
        
        return total
        
