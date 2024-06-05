class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Runtime: 54 ms (Beats 80.66%)
        Memory: 15 MB (Beats 18.81%)
        """
        
        index = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[index] = nums[i]
                index += 1

        return index