class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool

        Runtime: 27ms (Beats 95.06% of users with Python)
        Memory: 13.35MB (Beats 13.98% of users with Python)
        """

        return str(x) == str(x)[::-1]
