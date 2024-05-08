class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        repeat = set()
        length = 0
        n = len(s)
        l = 0
        r = 0

        while r < n:
            while s[r] in repeat:
                repeat.remove(s[l])
                l += 1

            repeat.add(s[r])
            r += 1
            length = max(length, len(repeat))

        return length
        
