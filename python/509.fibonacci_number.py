class Solution:
    def rec(self, n: int, store:dict):
        if n in store:
            return store[n]
        
        store[n - 1] = self.rec(n - 1, store)
        store[n - 2] = self.rec(n - 2, store)
        return store[n - 1] + store[n - 2]

    def fib(self, n: int) -> int:
        store = {0: 0, 1: 1, 2: 1}
        return self.rec(n, store)
