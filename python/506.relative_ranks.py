class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        order = score[:]
        order.sort(reverse=True)

        def find(arr, i):
            l = 0
            r = len(arr) - 1
            
            while l <= r:
                m = (l + r) // 2
                if arr[m] == i:
                    return m
                elif arr[m] < i:
                    r = m - 1
                else:
                    l = m + 1
            
            return -1

        placement = []
        for i in score:
            index = find(order, i)
            placement.append(['Gold Medal', 'Silver Medal', 'Bronze Medal'][index] \
                if index < 3 else str(index + 1))

        return placement
        
