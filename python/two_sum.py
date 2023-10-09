class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Runtime: 36ms (Beats 82.82%of users with Python)
        Memory: 14.07MB (Beats 78.77%of users with Python)
        """

        comps = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in comps:
                return [comps[complement], i]
            comps[nums[i]] = i
        
        return []
        
