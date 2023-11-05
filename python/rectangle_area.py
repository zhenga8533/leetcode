class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # Runtime: 46 ms (Beats 88.85%)
        # Memory: 16.2 MB (Beats 79.41%)
      
        # base area
        a = (ax2 - ax1) * (ay2 - ay1)
        b = (bx2 - bx1) * (by2 - by1)

        # bounds
        left = max(ax1, bx1)
        right = min(ax2, bx2)
        top = min (ay2, by2)
        bottom = max(ay1, by1)
        
        # overlap
        overlap = 0 if right - left < 0 or top - bottom < 0 \
            else (right - left) * (top - bottom)

        return a + b - overlap
        
