class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int

        Runtime: 526 ms (Beats 57.47%)
        Memory: 23.6 MB (Beats 86.34%)
        """

        area = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = max(area, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return area
        
