class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        total = 0
        curr = 0
        count = defaultdict(int)
        count[0] = 1

        for num in nums:
            curr += num
            if curr - goal in count:
                total += count[curr - goal]
            count[curr] += 1
        
        return total
