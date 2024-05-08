class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        ans = nums[l]

        while l <= r:
            if nums[l] < nums[r]:
                return min(ans, nums[l])
            
            mid = (l + r) // 2
            ans = min(ans, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        
        return ans
