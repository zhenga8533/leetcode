class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(n):
            swapped = False
            for j in range(n - 1):
                if nums[j] > nums[j + 1]:
                    if bin(nums[j]).count('1') != bin(nums[j + 1]).count('1'):
                        return False

                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True
            
            if not swapped:
                return True

        return True
