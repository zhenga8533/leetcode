class Solution:
    def gcd(self, a, b):
        if not b:
            return a
        
        return self.gcd(b, a % b)

    def fractionAddition(self, expression: str) -> str:
        neg = False
        bottom = False

        numer = 0
        denom = 1
        last = 0
        n = len(expression)

        for i in range(n):
            c = expression[i]

            if c == "-":
                neg = True
                bottom = False
            elif c == "+":
                neg = False
                bottom = False
            elif c == "/":
                bottom = True
            elif bottom:
                if i + 1 < n and expression[i + 1] == "0":
                    continue
                if c == "0":
                    c = "10"

                temp = last * denom
                numer *= int(c)
                denom *= int(c)
                numer += temp
            else:
                if c == "0":
                    last = 10
                else:
                    last = int(c)
                    
                if neg:
                    last = -last
        
        gcd = self.gcd(numer, denom)
        return f"{int(numer / gcd)}/{int(denom / gcd)}"
            
        
