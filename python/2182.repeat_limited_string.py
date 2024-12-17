class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        chars = [0 for _ in range(26)]
        base = ord('a')

        for c in s:
            chars[ord(c) - base] += 1

        limited = ""
        i = 25
        counter = 0
        while i >= 0:
            if chars[i] == 0:
                i -= 1
                counter = 0
            elif counter == repeatLimit:
                exist = False
                for j in range(i - 1, -1, -1):
                    if chars[j] > 0:
                        limited += chr(base + j)
                        chars[j] -= 1
                        exist = True
                        break
                if not exist:
                    return limited
                counter = 0
            else:
                limited += chr(base + i)
                chars[i] -= 1
                counter += 1

        return limited
        
