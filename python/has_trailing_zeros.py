class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        uno = False

        for num in nums:
            if num % 2 == 0:
                if uno:
                    return True
                else:
                    uno = True
        
        return False
        
