class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        commons = [0] * 26
        for c in words[0]:
            commons[ord(c) - 97] += 1
        
        for word in words[1:]:
            count = [0] * 26
            for c in word:
                count[ord(c) - 97] += 1
            for i in range(26):
                commons[i] = min(count[i], commons[i])
        
        res = []
        for i in range(26):
            res += [chr(i + 97)] * commons[i]
        
        return res
        
