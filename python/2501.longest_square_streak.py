class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        track = {}
        streak = -1

        nums.sort()
        for num in nums:
            sqrt = int(num ** 0.5)

            if sqrt ** 2 == num and sqrt in track:
                track[num] = track[sqrt] + 1
                streak = max(streak, track[num])
            else:
                track[num] = 1

        return streak
        
