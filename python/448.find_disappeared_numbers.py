class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        missing = set(range(1, n + 1))
        
        for num in nums:
            missing.discard(num)

        return list(missing)
        
