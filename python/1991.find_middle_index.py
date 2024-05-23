class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        before = 0
        after = sum(nums)

        for i, num in enumerate(nums):
            after -= num
            if before == after:
                return i
            before += num

        return -1
