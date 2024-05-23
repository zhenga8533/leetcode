class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        
        Runtime: 8 ms (Beats 97.9%)
        Memory: 13.5 MB (Beats 34.44%)
        """

        pre = ""

        for i in range(len(strs[0])):
            cc = strs[0][i]
            for s in strs:
                if i > len(s) - 1 or s[i] != cc:
                    return pre
            pre += cc
        
        return pre
        
