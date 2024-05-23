class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []

        row = []
        for num in nums:
            if len(row) != 0 and num - row[0] > k:
                return []
            row.append(num)
            
            if len(row) == 3:
                ans.append(row)
                row = []

        return ans
