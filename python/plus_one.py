class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]

        Runtime: 8 ms (Beats 95.36%)
        Memory: 13.5 MB (Beats 17.9%)
        """

        ans = []
        digits[len(digits) - 1] += 1
        rem = 0

        for i in range(len(digits) - 1, -1, -1):
            digit = digits[i] + rem
            ans.append(digit % 10)
            rem = digit / 10
        if (rem != 0):
            ans.append(1)

        return ans[::-1]
        
