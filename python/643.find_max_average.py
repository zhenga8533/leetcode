class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float

        Runtime: 895 ms (Beats 85.64%)
        Memory: 22.9 MB (Beats 19.76%)
        """

        window = nums[0:k]
        larg = sum(window)
        curr = larg
        for i in range(k, len(nums)):
            curr -= nums[i - k]
            curr += nums[i]
            larg = max(larg, curr)
        
        return larg / float(k)
        
