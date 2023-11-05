class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # Runtime: 33 ms (Beats 84.95%)
        # Memory: 16.1 MB (Beats 76.44%)
      
        if len(nums) == 0:
            return nums

        # variables
        ranges = []
        l = nums[0]
        last = nums[0]

        # loop to get ranges
        for num in nums[1:]:
            if num - 1 != last:
                ranges.append(f'{l}->{last}' if l != last else str(l))
                l = num
            
            last = num
        ranges.append(f'{l}->{last}' if l != last else str(l))

        return ranges
        
