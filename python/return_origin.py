class Solution:
    def judgeCircle(self, moves: str) -> bool:
        v, h = 0, 0

        for move in moves:
            if move == 'U':
                v += 1
            elif move == 'D':
                v -= 1
            elif move == 'L':
                h -= 1
            elif move == 'R':
                h += 1
        
        return v == 0 and h == 0
        
