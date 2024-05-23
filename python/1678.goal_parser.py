class Solution:
    def interpret(self, command: str) -> str:
        goal = {
            'G': 'G',
            '()': 'o',
            '(al)': 'al'
        }
        s = ''
        sym = ''

        for c in command:
            sym += c
            if sym in goal:
                s += goal[sym]
                sym = ''
        
        return s

        
