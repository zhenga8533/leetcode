class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        table = defaultdict(int)

        for i in range(n):
            partner = target - nums[i]
            if partner in table:
                return [table[partner], i]
            table[nums[i]] = i
        
