class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int

        Runtime: 12 ms (Beats 74.34%)
        Memory: 13.2 MB (Beats 67.31%)
        """

        fin = len(haystack)
        if (len(needle) > fin):
            return -1

        haystack += needle
        index = haystack.index(needle)

        return -1 if index >= fin else index
        
