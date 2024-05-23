class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Runtime: 43 ms (Beats 94.11%)
        # Memory: 16.7 MB (Beats 89.14%)
      
        chars = defaultdict(int)

        for c in s:
            chars[c] += 1
        
        for c in t:
            chars[c] -= 1

            if chars[c] == 0:
                del chars[c]
        
        return len(chars) == 0
        
