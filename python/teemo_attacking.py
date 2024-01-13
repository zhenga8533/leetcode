class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0

        for i in range(1, len(timeSeries)):
            total += duration

            diff = timeSeries[i] - timeSeries[i - 1]
            if diff < duration:
                total -= duration - diff

        return total + duration
