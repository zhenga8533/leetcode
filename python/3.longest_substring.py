class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        p1 = 0
        p2 = 0
        cset = set()

        while p2 < len(s):
            c = s[p2]
            if c in cset:
                longest = max(longest, len(cset))
                cset.remove(s[p1])
                p1 += 1
            else:
                cset.add(c)
                p2 += 1
        
        return max(longest, len(cset))
        