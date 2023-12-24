class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        table = set(nums)
        longest = 0

        for num in table:
            if num - 1 not in table:
                count = 1
                while num + count in table:
                    count += 1
                longest = max(longest, count)
        
        return longest
        
