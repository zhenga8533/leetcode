class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Runtime: 49 ms (Beats 87.27%)
        # Memory: 16.6 MB (Beats 32.12%)
      
        chars = defaultdict(int)

        for c in magazine:
            chars[c] += 1
        
        for c in ransomNote:
            if c in chars and chars[c] > 0:
                chars[c] -= 1
            else:
                return False

        return True
        
