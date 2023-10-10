class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int

        Runtime: 11 ms (Beats 93.22%)
        Memory: 13.2 MB (Beats 74.75%)
        """

        index = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1

        return index
        
