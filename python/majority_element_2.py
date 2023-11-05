class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Runtime: 106 ms (Beats 79.2%)
        # Memory: 17.5 MB (Beats 95.43%)
      
        n = int(len(nums) / 3)
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        for key in list(count.keys()):
            if count[key] <= n:
                del count[key]
        
        return list(count.keys())
        
