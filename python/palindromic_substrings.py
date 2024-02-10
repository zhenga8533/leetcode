class Solution:
    def countPalindrome(self, s: str, n: int, l: int, r: int) -> int:
        count = 0

        while l >= 0 and r < n and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        
        return count

    def countSubstrings(self, s: str) -> int:
        substrings = 0
        n = len(s)

        for i in range(len(s)):
            substrings += self.countPalindrome(s, n, i, i + 1)
            substrings += self.countPalindrome(s, n, i, i)


        return substrings
        
