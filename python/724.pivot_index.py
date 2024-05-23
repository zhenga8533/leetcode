class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Runtime: 92 ms (Beats 99.9%)
        Memory: 14.4 MB (Beats 57.23%)
        """

        lsum = 0
        rsum = sum(nums)

        for i in range(len(nums)):
            if lsum == rsum - nums[i]:
                return i
            else:
                lsum += nums[i]
                rsum -= nums[i]

        return -1
        
