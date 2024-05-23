class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        total = 0
        l, r = 0, 0
        p = False

        while r < n:
            total += nums[r]

            while total >= target:
                p = True
                ans = min(ans, r - l + 1)
                total -= nums[l]
                l += 1
            
            r += 1
        
        return ans if p else 0
