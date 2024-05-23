class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        Runtime: 14 ms (Beats 69.20%)
        Memory: 13.6 MB (Beats 33.13%)
        """

        s = list(s)
        t = list(t)

        while len(s):
            if s[0] in t:
                ind = t.index(s[0])
                del t[0:ind + 1]
                del s[0]
            else:
                return False
        
        return True
        
