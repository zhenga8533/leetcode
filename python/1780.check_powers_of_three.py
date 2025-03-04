class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while True:
            if n == 0:
                return True
            elif n % 3 == 2:
                return False
            n //= 3
        
