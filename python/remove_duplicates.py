class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Runtime: 55 ms (Beats 76.88%)
        Memory: 14.8 MB (Beats 45.53%)
        """
        
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[count] = nums[i]
                count += 1
        return count
