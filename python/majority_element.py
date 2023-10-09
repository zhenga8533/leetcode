class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Runtime: 124 ms (Beats 42.18%)
        Memory: 14.8 MB (Beats 63.1%)
        """

        nums.sort()
        n = len(nums)
        return nums[n//2]
        
