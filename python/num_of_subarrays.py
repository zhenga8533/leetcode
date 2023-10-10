class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int

        Runtime: 447 ms (Beats 80.7%)
        Memory: 23.3 MB (Beats 98.19%)
        """

        total = 0
        sub = sum(arr[:k])
        index = k

        while index < len(arr):
            if sub / k >= threshold:
                total += 1
            
            sub -= arr[index - k]
            sub += arr[index]

            index += 1

        return total + (sub /k >= threshold)
        
