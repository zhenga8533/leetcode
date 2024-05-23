class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str

        Runtime: 18 ms (Beats 45.27%)
        Memory: 13.4 MB (Beats 46.65%)
        """

        if len(str1) < len(str2):
            str1, str2 = str2, str1
        
        L, S = len(str1), len(str2)
        
        for i in range(S, 0, -1):
            if (L/i) == int(L/i) and (S/i) == int(S/i):
                c = str2[:i]
                if c*int(L/i) == str1 and c*int(S/i) == str2: 
                    return c
                
        return ""
