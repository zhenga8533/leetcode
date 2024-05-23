class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        count1 = defaultdict(int)
        count2 = defaultdict(int)

        for c in word1:
            count1[c] += 1
        for c in word2:
            if count1[c] == 0:
                return False
            count2[c] += 1
        
        return sorted(count1.values()) == sorted(count2.values())
        
