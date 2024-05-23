class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]

        Runtime: 115 ms (Beats 99.22%)
        Memory: 13.9 MB (Beats 8.21%)
        """

        set1 = set(nums1)
        set2 = set(nums2)
        
        return [list(set1.difference(set2)), list(set2.difference(set1))]
        
