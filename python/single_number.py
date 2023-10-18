class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Runtime: 84 ms (Beats 97%)
        Memory: 15.4 MB (Beats 76.33%)
        """

        xor = 0
        for num in nums:
            xor ^= num
        
        return xor
        
