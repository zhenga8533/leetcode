class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        ans = []
        nums.sort()

        for i in range(len(nums) // 2):
            ans.append(nums[2 * i + 1])
            ans.append(nums[2 * i])

        return ans
        
