class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Runtime: 517 ms (Beats 69.29%)
        # Memory: 29.5 MB (Beats 52.49%)
      
        indexes = defaultdict(int)

        for i, num in enumerate(nums):
            if num in indexes and abs(i - indexes[num]) <= k:
                return True
            else:
                indexes[num] = i

        return False
