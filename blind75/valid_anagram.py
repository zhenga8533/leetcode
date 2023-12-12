class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = defaultdict(int)

        for c in s:
            chars[c] += 1
        
        for c in t:
            chars[c] -= 1

            if chars[c] == 0:
                del chars[c]
        
        return len(chars) == 0
        
