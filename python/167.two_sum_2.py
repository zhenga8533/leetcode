class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Runtime: 117 ms (Beats 69.57%)
        # Memory: 17.2 MB (Beats 23.35%)
      
        l = 0
        r = len(numbers) - 1
        total = numbers[l] + numbers[r]

        while total != target:
            if total > target:
                r -= 1
            else:
                l += 1
            total = numbers[l] + numbers[r]

        return [l + 1, r + 1]
