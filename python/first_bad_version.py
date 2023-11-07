# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # Runtime: 40 ms (Beats 41.64%)
        # Memory: 16.1 MB (Beats 93.81%)
      
        l = 1
        r = n

        while l <= r:
            i = int((l + r) / 2)

            if isBadVersion(i):
                r = i - 1
            else:
                l = i + 1
        
        return l
        
