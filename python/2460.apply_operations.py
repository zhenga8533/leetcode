class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        res = []
        zeros = 0

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

                if nums[i] == 0:
                    zeros += 1
                else:
                    res.append(nums[i])
            elif nums[i] == 0:
                zeros += 1
            else:
                res.append(nums[i])
        
        res.append(nums[-1])
        return res + [0] * zeros
        
