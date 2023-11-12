class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Runtime: 375 ms (Beats 80.42%)
        # Memory: 31.2 MB (Beats 64.35%)
      
        table = set(nums)
        longest = 0

        for num in table:
            if num - 1 not in table:
                count = 1
                while num + count in table:
                    count += 1
                longest = max(longest, count)
        
        return longest
        
