class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        lc = word[0]
        count = 1

        for c in word[1:]:
            if c != lc or count == 9:
                comp += str(count) + lc
                lc = c
                count = 1
            else:
                count += 1

        return comp + str(count) + lc
        
