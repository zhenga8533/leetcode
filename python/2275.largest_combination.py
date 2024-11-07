class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        count = 0

        for i in range(32):
            count = max(
                sum(1 for c in candidates if c & (1 << i)),
                count
            )

        return count
        
