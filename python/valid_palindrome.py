class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Runtime: 41 ms (Beats 92.30%)
        # Memory: 17.7 MB (Beats 29.10%)
      
        test = ''.join(filter(str.isalnum, s)).lower()
        return test == test[::-1]
        
