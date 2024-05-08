class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        ans = nums[0]

        for num in nums:
            if total < 0:
                total = num
            else:
                total += num
            ans = max(ans, total)
        
        return ans
