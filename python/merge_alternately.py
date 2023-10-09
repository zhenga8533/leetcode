class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str

        Runtime: 20 ms (Beats 15.8%)
        Memory: 13.5 MB (Beats 11.99%)
        """
        
        altered = ""

        if len(word1) > len(word2):
            for i in range(len(word2)):
                altered += word1[i] + word2[i]
            altered += word1[len(word2):len(word1)]
        else:
            for i in range(len(word1)):
                altered += word1[i] + word2[i]
            altered += word2[len(word1):len(word2)]
        
        return altered
