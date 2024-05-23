class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool

        Runtime: 10 ms (Beats 90.45%)
        Memory: 13.3 MB (Beats 64.91%)
        """

        stack = []
        containers = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        vals = containers.values()

        for c in s:
            if c in containers:
                stack.append(c)
            elif c in vals:
                if len(stack) == 0 or c != containers[stack.pop()]:
                    return False

        return len(stack) == 0
        
