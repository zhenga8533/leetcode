class Solution:
    def dp(self, i, nums, n, bank):
            # base cases
            if i >= n - 2 and i < n:
                return nums[i]
            if i >= n - 1:
                return 0
            if i in bank:
                return bank[i]

            # store
            rob_2 = self.dp(i + 2, nums, n, bank)
            rob_3 = self.dp(i + 3, nums, n, bank)
            bank[i] = max(rob_2, rob_3) + nums[i]

            return bank[i]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        bank = {}
        
        return max(self.dp(0, nums, n, bank), self.dp(1, nums, n, bank))
        
