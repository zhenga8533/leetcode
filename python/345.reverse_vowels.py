class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str

        Runtime: 50 ms (Beats 49.41%)
        Memory: 20.8 MB (Beats 5.12%)
        """

        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowelAndPos = []
        rev = list(s)

        for i, c in enumerate(s):
            if c in vowels:
                vowelAndPos.append([c, i])
        
        for v in range(len(vowelAndPos)):
            rev[vowelAndPos[len(vowelAndPos) - v - 1][1]] = vowelAndPos[v][0]
        
        return "".join(rev)
        
