class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Runtime: 31 ms (Beats 69.52%)
        Memory: 13.2 MB (Beats 88.6%)
        """

        i = 2

        while i < len(nums):
            num = nums[i]
            if num == nums[i - 1] and num == nums[i - 2]:
                nums.pop(i)
            else:
                i += 1

        return len(nums)
        
