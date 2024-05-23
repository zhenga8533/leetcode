class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        Runtime: 130 ms (Beats 31.79%)
        Memory: 14.5 MB (Beats 66.71%)
        """

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                
