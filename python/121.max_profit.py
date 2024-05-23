class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        Runtime: 769 ms (Beats 59.70%)
        Memory: 22.4 MB (Beats 63.32%)
        """

        p1 = 0
        p2 = 0
        sell = 0

        while p2 < len(prices):
            current = prices[p2] - prices[p1]
            if prices[p1] < prices[p2]:
                sell = max(sell, current)
            else:
                p1 = p2
            p2 += 1

        return sell
        
