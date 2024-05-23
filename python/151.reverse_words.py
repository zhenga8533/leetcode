class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str

        Runtime: 8 ms (Beats 95.74%)
        Memory: 13.2 MB (Beats 99.60%)
        """

        return ' '.join(s.split()[::-1])
        
