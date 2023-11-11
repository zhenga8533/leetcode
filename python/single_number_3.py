class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Runtime: 51 ms (Beats 98.32%)
        # Memory: 18.5 MB (Beats 10.46%)
      
        singles = set()

        for num in nums:
            if num in singles:
                singles.remove(num)
            else:
                singles.add(num)
        
        return list(singles)
        
