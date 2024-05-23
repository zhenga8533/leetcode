class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = [0] * 101
        maxFreq = 0
        maxCount = 0

        for num in nums:
            counter[num] += 1
            if counter[num] > maxFreq:
                maxFreq = counter[num]
                maxCount = 1
            elif counter[num] == maxFreq:
                maxCount += 1
        
        return maxCount * maxFreq
        
