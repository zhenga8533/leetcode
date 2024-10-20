class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []

        for c in expression:
            if c == ")":
                expr = []
                
                while True:
                    val = stack.pop()
                    if val == "(":
                        break
                    else:
                        expr.append(val == "t")
                
                if stack:
                    operator = stack.pop()
                    ret = expr[0]

                    if operator == '&':
                        for b in expr:
                            ret &= b
                    elif operator == '|':
                        for b in expr:
                            ret |= b
                    else:
                        ret = not ret
                    
                    stack.append('t' if ret else 'f')
            elif c != ",":
                stack.append(c)
        
        return stack[-1] == 't'
        
