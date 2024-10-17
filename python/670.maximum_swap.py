class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = [int(c) for c in str(num)]
        last = {digit: i for i, digit in enumerate(digits)}
        
        for i, digit in enumerate(digits):
            for d in range(9, digit, -1):
                if last.get(d, -1) > i:
                    j = last[d]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int(''.join(map(str, digits)))
        
        return num
