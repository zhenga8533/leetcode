class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # Runtime: 89 ms (Beats 66.55%)
        # Memory: 17.6 MB (Beats 59.65%)
  
        n = len(arr)
        q = n // 4

        for i in range(n - q):
            if arr[i] == arr[i + q]:
                return arr[i]
        
