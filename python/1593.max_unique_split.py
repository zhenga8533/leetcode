class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)

        def backtrack(i, strs):
            if i == n:
                return 0
            
            splits = 0
            for j in range(i + 1, n + 1):
                sub = s[i:j]
                if sub not in strs:
                    strs.add(sub)
                    splits = max(splits, 1 + backtrack(j, strs))
                    strs.remove(sub)
            
            return splits
        
        return backtrack(0, set())
        
