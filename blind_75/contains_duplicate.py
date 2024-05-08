class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sett = set()

        for num in nums:
            if num in sett:
                return True
            sett.add(num)
        
        return False
        
