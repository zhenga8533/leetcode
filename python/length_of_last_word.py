class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Runtime: 36 ms (Beats 71.2%)
        # Memory: 16.2 MB (Beats 89.76%)
      
        return len(s.rstrip().split(' ')[-1])
        
