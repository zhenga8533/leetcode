class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool

        Runtime: 101 ms (Beats 99.77%)
        Memory: 14 MB (Beats 21.83%)
        """

        possible = 0

        if (len(flowerbed) == 1):
            if not flowerbed[0]:
                possible = 1
        else:
            if not flowerbed[0] and not flowerbed[1]:
                flowerbed[0] = 1
                possible += 1
            if not flowerbed[len(flowerbed) - 1] and not flowerbed[len(flowerbed) - 2]:
                flowerbed[len(flowerbed) - 1] = 1
                possible += 1
        for i in range(1, len(flowerbed) - 1):
            if not (flowerbed[i] or flowerbed[i - 1] or flowerbed[i + 1]):
                flowerbed[i] = 1
                possible += 1

        return possible >= n
        
