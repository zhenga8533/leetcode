class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]

        Runtime: 8 ms (Beats 99.25%)
        Memory: 13.3 MB (Beats 17.14%)
        """

        greatest = max(candies)
        will = []

        for candy in candies:
            if candy + extraCandies >= greatest:
                will.append(True)
            else:
                will.append(False)
        
        return will
        
