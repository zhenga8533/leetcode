class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        unique = defaultdict(int)
        total = 0

        for num in nums:
            unique[num] += 1
            if unique[num] == 2:
                total -= num
            elif unique[num] == 1:
                total += num
        
        return total
        
