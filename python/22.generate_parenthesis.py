class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Runtime: 41 ms (Beats 59.56%)
        # Memory: 16.4 MB (Beats 99%)
      
        ans = []
        self.generate(ans, 0, 0, "", n)
        return ans
    
    def generate(self, ans: List[str], l: int, r: int, s: str, n: int):
        if len(s) == n * 2:
            ans.append(s)
            return

        if l < n:
            self.generate(ans, l + 1, r, s + '(', n)
            
        if r < l:
            self.generate(ans, l, r + 1, s + ')', n)
