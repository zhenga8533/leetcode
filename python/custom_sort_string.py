class Solution:
    def customSortString(self, order: str, s: str) -> str:
        def custom_sort(c):
            return order.index(c) if c in order else len(order)
        
        sorted_s = sorted(s, key=custom_sort)
        
        return ''.join(sorted_s)
