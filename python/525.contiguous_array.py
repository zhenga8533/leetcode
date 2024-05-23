class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        table = {}
        curr_sum = 0
        max_len = 0

        for i, num in enumerate(nums):
            curr_sum += 1 if num == 1 else -1
            if curr_sum == 0:
                max_len = i + 1
            elif curr_sum in table:
                max_len = max(max_len, i - table[curr_sum])
            else:
                table[curr_sum] = i
            
        return max_len
