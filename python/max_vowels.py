class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int

        Runtime: 163 ms (Beats 33.79%)
        Memory: 17.3 MB (Beats 41.1%)
        """

        vowels = ['a', 'e', 'i', 'o', 'u']
        window = s[0:k]
        count = 0
        for c in window:
            if c in vowels:
                count += 1
        larg = count
        
        for i in range(k, len(s)):
            count -= s[i - k] in vowels
            count += s[i] in vowels
            larg = max(larg, count)
        
        return larg
