class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int

        Runtime: 15 ms (Beats 74.63%)
        Memory: 13.5 MB (Beats 14.26%)
        """

        altitude = 0
        large = 0

        for g in gain:
            altitude += g
            large = max(large, altitude)
        
        return large
        
