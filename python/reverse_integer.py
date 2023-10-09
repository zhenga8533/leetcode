class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int

        Runtime: 16ms (Beats 57.39% of users with Python)
        Memory: 12.98MB (Beats 98.71% of users with Python)
        """

        neg = -1 if x < 0 else 1
        rev = int(str(x * neg)[::-1]) * neg

        return rev if rev < 2**31 - 1 and rev > -(2 ** 31) else 0
        
