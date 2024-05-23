class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Runtime: 37 ms (Beats 61.63%)
        # Memory: 16.1 MB (Beats 75.73%)
      
        s = s.split(' ')
        n = len(s)
        if n != len(pattern) or len(set(s)) != len(set(pattern)):
            return False
        
        trace = {}
        for i in range(n):
            c = pattern[i]

            if c not in trace:
                trace[c] = s[i]
            elif trace[c] != s[i]:
                return False
        
        return True
        
