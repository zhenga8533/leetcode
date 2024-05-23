class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Runtime: 304 ms (Beats 100%)
        Memory: 15.1 MB (Beats 99.35%_
        """

        before = 0
        current = 0
        longest = 0
        remove = True
        for num in nums:
            if not num:
                longest = max(longest, before + current)
                before = current
                current = 0
                remove = False
            else:
                current += 1
        longest = max(longest, before + current) - remove
        
        return longest
        
