class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        n = len(s)

        def backtrack(start, arr):
            if start == n:
                ans.append(arr[:])
                return
            for i in range(start + 1, n + 1):
                ss = s[start:i]
                if ss == ss[::-1]:
                    backtrack(i, arr + [ss])
            
        backtrack(0, [])
        return ans
        
