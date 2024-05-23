class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]

        Runtime: 77 ms (Beats 19.1%)
        Memory: 14.5 MB (Beats 48.66%)
        """

        i = 0

        while i < len(asteroids) - 1:
            if asteroids[i] > 0 and asteroids[i + 1] < 0:
                ab = abs(asteroids[i + 1])
                if ab == asteroids[i]:
                    del asteroids[i]
                    del asteroids[i]
                elif ab > asteroids[i]:
                    del asteroids[i]
                else:
                    del asteroids[i + 1]
                if i > 0:
                    i -= 1
            else:
                i += 1
        
        return asteroids
