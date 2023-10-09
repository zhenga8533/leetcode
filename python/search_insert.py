class Solution(object):
    def searchInsert(self, nums, target):
        """
        Runtime: 24ms (Beats 88.01%of users with Python)
        Memory: 14.00MB (Beats 28.78%of users with Python)

        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        last = len(nums)
        pos = len(nums) / 2

        while True:
            if nums[pos] == target:
                return pos
            elif pos == 0:
                return 1 if target > nums[pos] else 0
            elif pos == len(nums):
                return pos
            elif nums[pos] < target:
                if pos == len(nums) - 1 or target < nums[pos + 1]:
                    return pos + 1
                pos = (pos + last) / 2
            else:
                if target > nums[pos - 1]:
                    return pos
                last = pos
                pos /= 2
        
