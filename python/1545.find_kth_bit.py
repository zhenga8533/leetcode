class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'
        
        mid = (1 << (n - 1))
        
        if k == mid:
            return '1'
        elif k < mid:
            return self.findKthBit(n - 1, k)
        else:
            return '0' if self.findKthBit(n - 1, mid - (k - mid)) == '1' else '1'
