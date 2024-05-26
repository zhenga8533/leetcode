class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        tested = 0

        for i in range(len(batteryPercentages)):
            if batteryPercentages[i] - tested > 0:
                tested += 1

        return tested
