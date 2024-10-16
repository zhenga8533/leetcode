class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [""] * numRows
        curr = 0
        inc = 1

        for c in s:
            rows[curr] += c

            curr += inc
            if curr == 0:
                inc = 1
            elif curr == numRows - 1:
                inc = -1
        
        return "".join(rows)
