class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Runtime: 41 ms (Beats 59.71%)
        # Memory: 16.3 MB (Beats 54.93%)
      
        sum = ''
        i = len(a) - 1
        j = len(b) - 1
        carry = 0

        while (i >= 0 and j >= 0) or carry > 0:
            digit = carry
            if i >= 0:
                digit += int(a[i])
            if j >= 0:
                digit += int(b[j])
            carry = int(digit / 2)
            digit %= 2

            sum = str(digit) + sum

            i -= 1
            j -= 1
        
        if i >= 0:
            sum = a[0:i + 1] + sum
        elif j >= 0:
            sum = b[0:j + 1] + sum
        
        return sum
        
