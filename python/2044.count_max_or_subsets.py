class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def backtrack(index: int, curr: int) -> None:
            if index == len(nums):
                if curr == maximum:
                    self.count += 1
                return
            
            backtrack(index + 1, curr | nums[index])
            backtrack(index + 1, curr)
        
        maximum = 0
        for num in nums:
            maximum |= num

        self.count = 0
        backtrack(0, 0)
        
        return self.count
        
