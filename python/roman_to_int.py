class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int

        Runtime: 29ms (Beats 58.97%)
        Memory: 13.2MB (Beats 65.21%)
        """

        symbols = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        sum = symbols[s[len(s) - 1]]
        for i in range(len(s) - 1):
            val = symbols[s[i]]
            sum += val if val >= symbols[s[i + 1]] else -val

        return sum
