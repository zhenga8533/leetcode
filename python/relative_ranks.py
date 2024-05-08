class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        order = score[:]
        order.sort(reverse=True)

        placement = []
        for i in score:
            index = order.index(i)
            placement.append(['Gold Medal', 'Silver Medal', 'Bronze Medal'][index] \
                if index < 3 else str(index + 1))

        return placement
        
