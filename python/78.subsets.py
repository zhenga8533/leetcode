class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def backtrack(start, arr):
            ans.append(arr)
            for i in range(start, n):
                backtrack(i + 1, arr + [nums[i]])
        backtrack(0, [])

        return ans
        
