# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def my_round(self, x, d=0):
        return floor(x + 0.5)

    def guessNumber(self, n: int) -> int:
        # Runtime: 34 ms (Beats 78.26%)
        # Memory: 16.1 MB (Beats 79.67%)
      
        large = n
        num = self.my_round(large / 2 + 0.5)

        while True:
            g = guess(num)

            if g == 0:
                return num
            elif g == 1:
                num = self.my_round((large + num) / 2)
            else:
                large = num
                num = self.my_round(num / 2)
