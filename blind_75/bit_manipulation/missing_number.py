class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = int(n * (n + 1) / 2)
        
        for num in nums:
            total -= num
        
        return total
        
