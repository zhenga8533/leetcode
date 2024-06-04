class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = set()
        length = 0

        for c in s:
            if c in counter:
                counter.remove(c)
                length += 2
            else:
                counter.add(c)
        
        return length + (len(counter) > 0)
        
