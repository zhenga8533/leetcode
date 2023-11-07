class Solution:
    def addDigits(self, num: int) -> int:'
        # Runtime: 31 ms (Beats 95.21%)
        # Memory: 16.3 MB (Beats 29.57%)
  
        while num > 9:
            temp = num
            num = 0

            while temp > 0:
                num += temp % 10
                temp = int(temp / 10)

        return num
        
