class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        n = len(nums)

        def find_min():
            curr_min = float('inf')
            index = 0
            for i in range(n):
                if nums[i] < curr_min:
                    curr_min = nums[i]
                    index = i
            return index

        for _ in range(k):
            i = find_min()
            nums[i] *= multiplier
        return nums
        
