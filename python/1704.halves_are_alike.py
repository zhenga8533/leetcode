class Solution:
    def countVowels(self, s: str) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        count = 0

        for c in s:
            if c in vowels:
                count += 1

        return count

    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()

        return self.countVowels(s[0:len(s) // 2]) == self.countVowels(s[len(s) // 2:len(s)])
