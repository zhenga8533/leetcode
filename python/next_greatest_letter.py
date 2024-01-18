class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        l = 0
        r = n

        while l < r:
            m = (l + r) // 2

            if m + 1 < n and letters[m] <= target and letters[m + 1] > target:
                return letters[m + 1]
            elif letters[m] > target:
                r = m
            else:
                l = m + 1
        
        return letters[0]
        
