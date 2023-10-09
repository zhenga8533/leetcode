class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Runtime: 491 ms (Beats 11.3%)
        Memory: 13.9 MB (Beats 41.91%)
        """

        start = 0
        for end in range(len(nums)):
            k -= not nums[end]
            if k < 0:
                k += not nums[start]
                start += 1
            print(nums[start:end + 1], start, end, k)
        return end - start + 1
        
