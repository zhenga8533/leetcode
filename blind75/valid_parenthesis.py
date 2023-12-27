class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []

        for c in s:
            if c in ')}]':
                if len(stack) == 0 or stack.pop() != mapping[c]:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0
        
