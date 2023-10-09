class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int

        Runtime: 13 ms (Beats 79.16%)
        Memory: 13.1 MB (Beats 74.75%)
        """

        nums[:] = [num for num in nums if num != val]
        
        return len(nums)
        
