class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]

        Runtime: 51 ms (Beats 62.93%)
        Memory: 17.3 MB (Beats 12.70%)
        """

        total = [0 for i in range(n + 1)]
        for i in range(n + 1):
            total[i] = "{0:b}".format(i).count('1')
        
        return total
        
