class Solution:
    def isPalindrome(self, s: str) -> bool:
        test = ''.join(filter(str.isalnum, s)).lower()
        return test == test[::-1]
        
