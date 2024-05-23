class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        Runtime: 822 ms (Beats 72.72%)
        Memory: 27.9 MB (Beats 48.90%)
        """

        a = float('inf')
        b = float('inf')

        for num in nums:
            if num <= a:
                a = num
            elif num <= b:
                b = num
            else:
                return True
        
        return False
        
