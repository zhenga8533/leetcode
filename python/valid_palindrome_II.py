class Solution:
    def validPalindrome(self, s: str, d=0) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                if d > 0:
                    return False
                return self.validPalindrome(s[l + 1:r + 1], d + 1) or \
                    self.validPalindrome(s[l:r], d + 1)
            else:
                l += 1
                r -= 1
        
        return True
        
