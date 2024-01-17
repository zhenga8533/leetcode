class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr.sort()
        occurences = set()
        n = len(arr)
        i = 0

        while i < n:
            count = 1
            while i < n - 1 and arr[i] == arr[i + 1]:
                i += 1
                count += 1
            
            if count in occurences:
                return False
            occurences.add(count)
            i += 1
        
        return True
