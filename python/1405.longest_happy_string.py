class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = []

        while a > 0 or b > 0 or c > 0:
            if len(result) >= 2 and result[-1] == result[-2]:
                if result[-1] == 'a':
                    if b >= c and b > 0:
                        result.append('b')
                        b -= 1
                    elif c > 0:
                        result.append('c')
                        c -= 1
                    else:
                        a = 0
                elif result[-1] == 'b':
                    if a >= c and a > 0:
                        result.append('a')
                        a -= 1
                    elif c > 0:
                        result.append('c')
                        c -= 1
                    else:
                        b = 0
                elif result[-1] == 'c':
                    if a >= b and a > 0:
                        result.append('a')
                        a -= 1
                    elif b > 0:
                        result.append('b')
                        b -= 1
                    else:
                        c = 0
            else:
                if a >= b and a >= c and a > 0:
                    result.append('a')
                    a -= 1
                elif b >= a and b >= c and b > 0:
                    result.append('b')
                    b -= 1
                elif c > 0:
                    result.append('c')
                    c -= 1
                else:
                    break

        return ''.join(result)
