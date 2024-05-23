class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Runtime: 39 ms (Beats 90.14%)
        # Memory: 16.5 MB (Beats 52.2%)
      
        for i in range(len(s)):
            if s.index(s[i]) != t.index(t[i]):
                return False
        
        return True
        
